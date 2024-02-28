#Importing the necessary packages
import os
import requests, json
from bs4 import BeautifulSoup
from config import *

import streamlit as st
import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt
from millify import millify

from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from streamlit_extras.metric_cards import style_metric_cards
import altair as alt
from folium.plugins import HeatMap

from get_stations import get_stations
from get_vehicles import get_vehicles

if 'vehicles_df' not in st.session_state:
    st.session_state.vehicles_df = get_vehicles()

if 'stations_json' not in st.session_state:
    st.session_state.stations_json = get_stations()

vehicles_df = st.session_state["vehicles_df"]
stations_df = st.session_state["stations_df"]

import streamlit as st

# Your HTML content as a multi-line string
html_content = """
<style>
    .charging-info {
        font-family: Arial,Helvetica, sans-serif;
        margin-bottom: 20px;
    }

    .charging-info h2 {
        color: white;
    }

    .charging-info p {
        color: white;
    }

    .charging-category {
        margin-bottom: 15px;
    }

    .charging-category h3 {
        color: #007bff;
    }

    .charging-category p {
        color: white;
    }
</style>

<div class="charging-info">
    <h2>EV Charging Equipment Categories:</h2>
    <p>EV charging equipment is categorized by charging speed, which depends on the battery's depletion level, capacity, type, vehicle's charger capacity, and charging equipment specifications. Charging duration can range from under 20 minutes with DC fast chargers to over 20 hours with Level 1 chargers. Selecting equipment involves considering several factors like networking, payment options, and maintenance.</p>
    
<div class="charging-category">
    <h3>Level 1 Charging</h3>
    <p>Offers about 5 miles of range per hour of charging using a 120V AC plug. Comes standard with EVs, connecting via a NEMA connector to a household outlet and an SAE J1772 connector to the vehicle. It's a common home charging option, providing about 40 miles of range for an 8-hour charge. Less than 1% of U.S. public charging ports are Level 1.</p>
    </div>

<div class="charging-category">
    <h3>Level 2 Charging</h3>
    <p>Provides roughly 25 miles of range per hour of charging, using either 240V (residential) or 208V (commercial) power. It's a frequent choice for home, public, and workplace charging, offering faster charging speeds. Most U.S. public EV charging ports are Level 2.</p>
    </div>

<div class="charging-category">
    <h3>DC Fast Charging</h3>
    <p>Offers 100 to 200+ miles of range per 30 minutes of charging. It's crucial for quick charging along busy routes and is expanding due to federal initiatives and fleet adoption. There are three main types of DC fast chargers: CCS, CHAdeMO, and J3400 (NACS).</p>
    </div>
</div>

"""

st.markdown(html_content, unsafe_allow_html=True)

st.write("")



equipment_sum_df = stations_df.groupby('state').agg({
    'ev_dc_fast_ports': 'sum',
    'ev_level1_ports': 'sum',
    'ev_level2_ports': 'sum'
}).reset_index()

# Step 2: Convert the DataFrame to a long format
melted_df = equipment_sum_df.melt(id_vars=['state'], value_vars=['ev_dc_fast_ports', 'ev_level1_ports', 'ev_level2_ports'], var_name='port_type', value_name='sum')

# Step 3: Pivot to get the desired shape
equipment_sum_df = melted_df.pivot(index='port_type', columns='state', values='sum')


st.write(equipment_sum_df)


st.write("##")
st.write("##")
st.write("##")

st.markdown("<h2 style='text-align: left; font-family: Arial, Helvetica, sans-serif;'>Utility-Related Laws and Incentives</h2>", unsafe_allow_html=True)


st.markdown("<p style='font-family: Arial, Helvetica, sans-serif; font-color: white;'>Utilities are responsible for supplying power and maintaining the infrastructure needed for essential services, giving consumers access to electricity, natural gas, water, and more. With the rising popularity of plug-in electric vehicles (PEVs), electric utilities are becoming more pivotal in supporting PEV adoption by expanding charging infrastructure and ensuring there is enough power available. They offer various incentives to residential, commercial, and multi-unit dwellings to encourage the purchase of alternative fuel vehicles and the installation of electric vehicle charging stations. These incentives can include reduced rates for electricity usage during off-peak hours, cash-back rebates, grants, loans, and other support services for PEVs and their charging equipment. These efforts not only motivate customers to embrace new and alternative technologies but also enhance customer involvement and contribute to the sustainable increase in energy demand.</p>", unsafe_allow_html=True)

st.markdown("<p style='font-family: Arial, Helvetica, sans-serif; font-color: white;'>The U.S. Department of Transportation’s (DOT) Federal Highway Administration (FHWA) National Electric Vehicle Infrastructure (NEVI) Formula Program provides funding to states to strategically deploy electric vehicle (EV) charging stations and to establish an interconnected network to facilitate data collection, access, and reliability. Funding is available for up to 80% of eligible project costs.</p>", unsafe_allow_html=True)


#container for 4th set of visualizations
dash_4 = st.container()

vehicles_df_2022 = vehicles_df[(vehicles_df['Year'] != 2020) & (vehicles_df['Year'] != 2021)]

registered_vehicles_by_state = vehicles_df_2022.groupby('State')['Count'].sum().sort_values(ascending=False)

charging_stations_by_state = stations_df.groupby('state').size()


with dash_4:

    # create columns for both graph
    col1,col2 = st.columns(2)

    # Creating a DataFrame for the analysis
    infrastructure_gap_df = pd.DataFrame({
        'Charging_Stations': charging_stations_by_state,
        'Registered_Vehicles': registered_vehicles_by_state
    })#.fillna(0)

    # Calculating the ratio of registered vehicles to charging stations
    infrastructure_gap_df['Station_to_Vehicles_Ratio'] = infrastructure_gap_df['Charging_Stations'] / infrastructure_gap_df['Registered_Vehicles']

    # Sorting the DataFrame by the ratio in descending order to identify potential gaps
    infrastructure_gap_df = infrastructure_gap_df.sort_values('Station_to_Vehicles_Ratio', ascending=True)



    with col1:
        st.write("")
        st.write("Top 10 states with the lowest ratio of Charging Stations to Registered Vehicles:")
        st.write(infrastructure_gap_df.head(10))


    with col2:
        st.write("")
        st.write("Top 10 states with the highest ratio of Charging Stations to Registered Vehicles:")
        st.write(infrastructure_gap_df.tail(10))



