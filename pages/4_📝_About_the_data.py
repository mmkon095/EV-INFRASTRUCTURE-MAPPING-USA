import streamlit as st
from get_stations import get_stations
from get_vehicles import get_vehicles
from convertjsontodf import jsontodf


if 'vehicles_df' not in st.session_state:
    st.session_state.vehicles_df = get_vehicles()

if 'stations_json' not in st.session_state:
    st.session_state.stations_json = get_stations()

if 'stations_df' not in st.session_state:
    st.session_state.stations_df = jsontodf() 

vehicles_df = st.session_state["vehicles_df"]
stations_json = st.session_state["stations_json"]
stations_df = st.session_state["stations_df"]


st.markdown("## About the Data:")

st.write("")



st.subheader('Charging Stations Data:')
st.markdown("The data pertaining to electric vehicle charging stations is sourced from the National Renewable Energy Laboratory's developer network. It includes information such as latitude, longitude, station name, state, directions etc......")

#st.write(stations_df.head())
st.dataframe(stations_df, use_container_width=True)

st.write("")

# Displaying a data table
st.subheader('Electric Vehicles Data:')
st.markdown("The data pertaining to electric vehicle population counts is sourced from the US Department of Energy's Alternative Fuels' Data Center. It includes information on the type of the electric vehicles, state and the total number registered in each state")

#st.write(vehicles_df.head())
vehicles_df = vehicles_df[['State','Fuel Type','Count','Year']]
st.dataframe(vehicles_df, use_container_width=True)
