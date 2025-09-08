#!pip install -r requirements.txt

#Importing the necessary packages
import requests, json
#from config import *
import streamlit as st

stationsurl = st.secrets["stationsurl"]



@st.cache_data
def get_stations():
    #Establish connection to NREL API client
    response_stations = requests.get(stationsurl)
    #Parse and load geojson records from client
    parse_stations = json.loads(response_stations.text)

    #Extract features from geojson records
    features = parse_stations['features']

    # Define the list of properties to keep
    properties_to_keep = [
        'geometry.coordinates',
        'properties.access_days_time',
        'properties.cards_accepted',
        'properties.date_last_confirmed',
        'properties.open_date',
        'properties.expected_date',
        'properties.station_name',
        'properties.station_phone',
        'properties.facility_type',
        'properties.city',
        'properties.intersection_directions',
        'properties.state',
        'properties.street_address',
        'properties.zip',
        'properties.ev_connector_types',
        'properties.ev_network',
        'properties.ev_pricing',
        'properties.ev_dc_fast_num',
        'properties.ev_level1_evse_num',
        'properties.ev_level2_evse_num'
                ]


    # Filter and modify the data
    stations_json = []

    stations_to_exclude = ['UCSD - Pangea - DCFC', 'POLESTAR AUTO DC FAST 02', 'Davenport - 4', 'Davenport - 3', 'Orlando - 4', 'Home2Suites Asheville Airport', 'SemaConnect Bangalore - 7','Community Field Road Parking Lot','Brixmor Santa Paula Center (Santa Paula, CA)']

    for entry in features:
        # Check if 'geometry.coordinates' property exists
        if 'geometry' in entry and 'coordinates' in entry['geometry']:
            if 'state' in entry['properties'] and entry['properties']['state'] and entry['properties']['state'] not in ['QC', 'PR', 'BC', 'ON']:
                # Check if station_name is not in the exclusion list
                if 'station_name' in entry['properties'] and entry['properties']['station_name'] not in stations_to_exclude:
                    # Create a new dictionary with only the required properties
                    filtered_entry = {}
                    for prop in properties_to_keep:
                        value = entry
                        for key in prop.split('.'):
                            if key in value:
                                value = value[key]
                            else:
                                value = None
                                break
                        filtered_entry[prop] = value
                    stations_json.append(filtered_entry)

    return stations_json

if __name__ == "__main__":
    stations_json = get_stations()
    #print(vehicles_df.head())
