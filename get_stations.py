#!pip install -r requirements.txt

#Importing the necessary packages
import requests, json, time
from requests.adapters import HTTPAdapter
from requests.exceptions import ChunkedEncodingError, RequestException
from urllib3.util import Retry
#from config import *
import streamlit as st

stationsurl = st.secrets["stationsurl"]



@st.cache_data(ttl=604800) #cache for 7 days
def get_stations():

    # 1. Create a session
    session = requests.Session()

    # 2. Set up retry rules
    retries = Retry(
        total=5,            # Total number of retries
        connect=5,
        read=5,
        backoff_factor=1,   # Wait 1s, 2s, 4s between retries
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        raise_on_status=False
    )

    # 3. Mount the retry strategy to the session
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

   # Establish connection to NLR API client
    for attempt in range(3):
        try:
            response_stations = session.get(
                stationsurl,
                timeout=(10, 300)
            )

            response_stations.raise_for_status()

            # Parse and load geojson records
            parse_stations = response_stations.json()

            break

        except (ChunkedEncodingError, RequestException) as e:
            if attempt == 2:
                st.error(f"Unable to download station data: {e}")
                raise

            time.sleep(2 ** attempt)

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
