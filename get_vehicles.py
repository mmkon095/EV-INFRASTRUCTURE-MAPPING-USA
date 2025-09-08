#!pip install -r requirements.txt

#Importing the necessary packages
import requests, json
from bs4 import BeautifulSoup
#from config import *

import streamlit as st
import pandas as pd


from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static



def fetch_and_parse(url, headers=None):
    """Fetches content from a URL and returns parsed HTML."""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")
    else:
        print("Failed to fetch the webpage")
        return None

def extract_vehicle_data(soup, year):
    """Extracts vehicle registration data from the parsed HTML."""
    if soup is None:
        return []
    
    data_table = soup.find("table", {"id": "vehicle_registration"})
    rows = data_table.find_all("tr") if data_table else []

    vehicle_data = []
    for row in rows[1:]:  # Skip header rows
        columns = row.find_all("td")
        state = columns[0].text.strip()
        ev_count = columns[1].text.strip().replace(",", "")
        phev_count = columns[2].text.strip().replace(",", "")

        vehicle_data.extend([
            {"State": state, "Fuel Type": "Electric", "Count": ev_count, "Year": year},
            {"State": state, "Fuel Type": "PHEV", "Count": phev_count, "Year": year}
        ])

    return vehicle_data

def process_vehicle_data(data):
    """Converts and cleans vehicle data."""
    df = pd.DataFrame(data)
    df['Count'] = df['Count'].astype('int')
    df = df[df['State'] != 'United States']
    return df

@st.cache_data
def get_vehicles():
    """Main function to fetch and process vehicle registration data."""
    headers = {'User-Agent': 'Mozilla/5.0 ...'}
    all_data = []

    for year in range(2020, 2024):
        url = f"https://afdc.energy.gov/vehicle-registration?year={year}"
        soup = fetch_and_parse(url, headers)
        year_data = extract_vehicle_data(soup, year)
        all_data.extend(year_data)

    vehicles_df = process_vehicle_data(all_data)
    
    #vehicles_df = vehicles_df.pivot_table(index=['State', 'Fuel Type'], 
    #                      columns='Year', 
    #                      values='Count', 
    #                      fill_value=0)


    return vehicles_df

if __name__ == "__main__":
    vehicles_df = get_vehicles()
    print(vehicles_df.tail())



