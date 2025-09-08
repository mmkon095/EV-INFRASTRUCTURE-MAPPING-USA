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
from sodapy import Socrata

socratadomain = st.secrets["socratadomain"]
socratadatasetidentifier = st.secrets["socratadatasetidentifier"]
socratatoken = st.secrets["socratatoken"]

@st.cache_data
def get_vehicle_coords():
    socrata_domain = socratadomain
    socrata_dataset_identifier = socratadatasetidentifier
    socrata_token = socratatoken
    client = Socrata(socrata_domain, socrata_token)
    results = client.get(socrata_dataset_identifier, limit=1000000, select="geocoded_column,state,model,make,model_year,ev_type")

    vehiclecoords_df = pd.DataFrame.from_dict(results)

    coordinates_df = pd.json_normalize(vehiclecoords_df['geocoded_column'])

    # Create new columns for longitude and latitude
    vehiclecoords_df['longitude'] = coordinates_df['coordinates'].apply(lambda x: x[0] if isinstance(x, list) else None)
    vehiclecoords_df['latitude'] = coordinates_df['coordinates'].apply(lambda x: x[1] if isinstance(x, list) else None)

    #Drop rows with null longitude and latitude values
    vehiclecoords_df.dropna(subset=['longitude','latitude'], inplace=True)

    #Drop the mixed geocoded column
    vehiclecoords_df.drop(columns=['geocoded_column'], inplace=True)

    '''
    #Map state column values from abbreviations to full state name
    
    abbrv_to_state = {
          'CT': 'Connecticut',
          'ME': 'Maine',
          'MA': 'Massachusetts',
          'NH': 'New Hampshire',
          'NJ': 'New Jersey',
          'NY': 'New York',
          'PA': 'Philadephia',
          'RI': 'Rhode Island',
          'VT': 'Vermont',
          'AL': 'Alabama',
          'AR': 'Arkansas',
          'DC': 'District of Columbia',
          'DE': 'Delaware',
          'FL': 'Florida',
          'GA': 'Georgia',
          'KY': 'Kentucky',
          'LA': 'Louisiana',
          'MD': 'Maryland',
          'MS': 'Mississippi',
          'NC': 'North Carolina',
          'SC': 'South Carolina',
          'TN': 'Tennessee',
          'VA': 'Virginia',
          'WV': 'West Virginia',
          'IL': 'Illinois',
          'IN': 'Indiana',
          'IA': 'Iowa',
          'KS': 'Kansas',
          'MI': 'Michigan',
          'MN': 'Minnesota',
          'MO': 'Missouri',
          'OH': 'Ohio',
          'ND': 'North Dakota',
          'NE': 'Nebraska',
          'SD': 'South Dakota',
          'WI': 'Wisconsin',
          'AZ': 'Arizona',
          'NM': 'New Mexico',
          'OK': 'Oklahoma',
          'TX': 'Texas',
          'AK': 'Alaska',
          'CA': 'California',
          'CO': 'Colorado',
          'HI': 'Hawaii',
          'ID': 'Idaho',
          'NV': 'Nevada',
          'MT': 'Montana',
          'OR': 'Oregon',
          'UT': 'Utah',
          'WA': 'Washington',
          'WY': 'Wyoming',
    }

    vehiclecoords_df['state'] = vehiclecoords_df['state'].map(abbrv_to_state)

    '''
    return vehiclecoords_df