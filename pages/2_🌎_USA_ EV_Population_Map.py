#!pip install -r requirements.txt

#Importing the necessary packages
import requests, json
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import folium
import os
import numpy as np

from sklearn import preprocessing
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from get_stations import get_stations
from get_vehicles import get_vehicles

if 'vehicles_df' not in st.session_state:
    st.session_state.vehicles_df = get_vehicles()

if 'stations_json' not in st.session_state:
    st.session_state.stations_json = get_stations()

stations_json = st.session_state["stations_json"]
vehicles_df = st.session_state["vehicles_df"]

def create_map():

    # Create the Folium map
    global map

    map = folium.Map(location=[35.3, -97.6], zoom_start=4)

    
    #return map


def add_data_to_map(map):

    #Create a marker cluster to optimize loading the map
    marker_cluster = MarkerCluster()

    # Add markers with popups for each location to the MarkerCluster layer




    for entry in stations_json:
        coordinates = entry['geometry.coordinates']
        station_name = entry['properties.station_name']
        intersection_directions = entry['properties.intersection_directions']
        ev_dc_fast_ports = entry['properties.ev_dc_fast_num']
        ev_level1_ports = entry['properties.ev_level1_evse_num']
        ev_level2_ports = entry['properties.ev_level2_evse_num']
        popup_text = f"<h4>Station Name:</h6><b>{station_name}<br><h6>Directions:</h6>{intersection_directions}<h6>DC Fast Ports:</h6>{ev_dc_fast_ports}<br><h6>Level 1 Ports:</h6>{ev_level1_ports}<br><h6>Level 2 Ports:</h6>{ev_level2_ports}</b><br>"
        folium.Marker(location=[coordinates[1], coordinates[0]],
                      popup=popup_text,
                      icon=folium.Icon(prefix='fa', icon='fa-bolt')
                      ).add_to(marker_cluster)

    marker_cluster.add_to(map)

    # Logarithmic scaling
    vehicles_df["Count_log"] = np.log1p(vehicles_df["Count"])

    state_geo = requests.get("https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json").json()


    # Create choropleth map with logarithmic scale and tooltips
    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=vehicles_df,
        columns=["State", "Count_log"],
        key_on="feature.properties.name",
        fill_color="YlGnBu",
        fill_opacity=0.7,
        line_opacity=0.7,
        highlight=True,
        legend_name="Electric Vehicle Registrations(2022) - Logarithmic scale",
        tooltip=folium.GeoJsonTooltip(
            fields=["State", "Fuel Type", "Count"],
            aliases=["State:", "Fuel Type:", "Number of registered vehicles:"],
            localize=True,
            sticky=False,
            labels=True,
            style="""background-color: #F0EFEF;
                        border: 2px solid black;
                        border-radius: 3px;
                        box-shadow: 3px;
                    """,
            max_width=800 ),
        popup_text = ["Count"]
        ).add_to(map)


    folium.LayerControl().add_to(map)



def main():
    # Check if map already exists in directory
    if os.path.exists("ev_charging_map.html"):

        print("Map html file already exists")
        # Display the HTML file using st.components.v1.html
        with open("ev_charging_map.html", "r") as file:

            map_html = file.read()
        st.components.v1.html(map_html, height=800, scrolling=True)
    
    else:
        print("Map html file does not exist, running function to create map()....")
        st.empty()
        create_map()
        add_data_to_map(map)
        # Save the Folium map as an HTML file
        map.save("ev_charging_map.html")
        print("Saving new map file")
        #map = create_map()
        # Display the HTML file using st.components.v1.html
        print("Opening new map file")
        with open("ev_charging_map.html", "r") as file:
            map_html = file.read()
        
        st.components.v1.html(map_html, height=800, scrolling=True)

if __name__ == "__main__":
    main()




#Trigger data update to remove existing map and load a new one
if st.button("Refresh Map"):
    st.empty()
    os.remove("ev_charging_map.html")
    main()

if st.button("Fetch new data and map"):
    st.empty()
    if os.path.exists("ev_charging_map.html"):
        os.remove("ev_charging_map.html")
        get_stations()
        get_vehicles()
        main()

    else:
        get_stations()
        get_vehicles()
        main()
