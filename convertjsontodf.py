import pandas as pd
import streamlit as st
from get_stations import get_stations


stations_json = get_stations()


@st.cache_data

def jsontodf():
    

    #Store records into pandas dataframe
    stations_df = pd.json_normalize(stations_json)

    #Rename the columns
    stations_df = stations_df.rename(columns={'geometry.coordinates': 'coordinates',
                                         'properties.access_days_time': 'availability',
                                         'properties.cards_accepted': 'payment_methods',
                                         'properties.date_last_confirmed': 'date_last_confirmed',
                                         'properties.open_date': 'opening_date',
                                         'properties.expected_date': 'expected_opening_date',
                                         'properties.station_name': 'station_name',
                                         'properties.station_phone': 'station_phone',
                                         'properties.facility_type': 'facility_type',
                                         'properties.city': 'city',
                                         'properties.intersection_directions': 'directions',
                                         'properties.state': 'state',
                                         'properties.street_address': 'street_address',
                                         'properties.zip': 'zipcode',
                                         'properties.ev_connector_types': 'ev_connector_types',
                                         'properties.ev_network': 'ev_network',
                                         'properties.ev_pricing': 'pricing',
                                         'properties.ev_dc_fast_num': 'ev_dc_fast_ports',
                                         'properties.ev_level1_evse_num': 'ev_level1_ports',
                                         'properties.ev_level2_evse_num': 'ev_level2_ports'})

    #Map state column values from abbreviations to full state name
    abbrv_to_state = {
                    'CT': 'Connecticut',
                    'ME': 'Maine',
                    'MA': 'Massachusetts',
                    'NH': 'New Hampshire',
                    'NJ': 'New Jersey',
                    'NY': 'New York',
                    'PA': 'Pennsylvania',
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

    stations_df['state'] = stations_df['state'].map(abbrv_to_state)

    return stations_df