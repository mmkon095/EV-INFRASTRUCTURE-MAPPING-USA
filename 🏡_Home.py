import streamlit as st

st.set_page_config(layout="wide", page_title="EV Charging Station Dashboard", page_icon="⚡")

#!pip install -r requirements.txt

#Importing the necessary packages
import os
import requests, json
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import folium
from millify import millify

from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from streamlit_extras.metric_cards import style_metric_cards
import altair as alt
from folium.plugins import HeatMap

from get_stations import get_stations
from convertjsontodf import jsontodf
from get_vehicles import get_vehicles

#vehicles_df = get_vehicles()
#stations_json = get_stations()


if 'vehicles_df' not in st.session_state:
    st.session_state.vehicles_df = get_vehicles()

if 'stations_json' not in st.session_state:
    st.session_state.stations_json = get_stations()

if 'stations_df' not in st.session_state:
    st.session_state.stations_df = jsontodf() 

vehicles_df = st.session_state["vehicles_df"]
stations_json = st.session_state["stations_json"]
stations_df = st.session_state["stations_df"]




# creates the container for page title
dash_1 = st.container()

with dash_1:
    st.markdown("<h2 style='text-align: center; font-family: Arial, Helvetica, sans-serif;'>EV Dashboard</h2>", unsafe_allow_html=True)
    st.write("")
    st.markdown(f"<p style='font-family: Arial, Helvetica, sans-serif;'>From the year 2020 to 2022, the number of registered electric vehicles in the US has more than doubled in size by a whopping <span style='color: #007bff;'><b>114%</b></span>. To cater to the growing number of EVs, a substantial network of charging stations for both private users and fleet operations is essential. Individuals and organizations looking into electric vehicles (EVs), including fully electric and plug-in hybrid models, require access to charging facilities. Typically, this begins with home-based or fleet-based charging setups. Workplace and public charging points further support the shift to EVs by providing convenient charging solutions in frequently visited places. There are currently <b><span style='color: #007bff;'>{len(stations_json)} charging stations</b></span> that are publicly available across the states in the US.</p>", unsafe_allow_html=True)
    st.write("")


# creates the container for metric card
dash_2 = st.container()




#Get the % change for any column by year and the specificed aggregate
def get_pct_change():
    #Group by years and calculate the specified metric
    yearly_total_count = vehicles_df.groupby(['Year'])['Count'].sum()
    #Calculate the % change
    yearly_change = yearly_total_count.pct_change() * 100
    #grp_years.fillna(0, inplace=True)
    #grp_years = grp_years.apply(lambda x: f"{x:.1f}%" if pd.notnull(x) else "NaN")

    return yearly_change, yearly_total_count

#load pct_change function variables
yearly_change, yearly_total_count = get_pct_change()

#st.write(state_yearly_totals[2020])

with dash_2:
    # Calculate Total Vehicle Counts by Year

    #Total Vehicle Counts in 2020
    vehicles_df_2020 = vehicles_df[(vehicles_df['Year'] != 2021) & (vehicles_df['Year'] != 2022)]

    #Total Vehicle Counts in 2021
    vehicles_df_2021 = vehicles_df[(vehicles_df['Year'] != 2020) & (vehicles_df['Year'] != 2022)]

    #Total Vehicle Counts in 2022
    vehicles_df_2022 = vehicles_df[(vehicles_df['Year'] != 2020) & (vehicles_df['Year'] != 2021)]

    


    col1, col2, col3 = st.columns(3)

    #create column span
    with col1:
        col1.metric(label="Number of registered EV's in 2020", value= "$"+millify(yearly_total_count[2020], precision=2), delta=0, delta_color="off")
        st.write("")
        st.write("")
        
        vehicle_types_count_2020 = vehicles_df_2020.groupby(['Fuel Type'])['Count'].sum().reset_index()
        chart = alt.Chart(vehicle_types_count_2020).mark_arc().encode(
            theta= alt.Theta(field="Count", type="quantitative"),
            color= alt.Color(field="Fuel Type", type="nominal"),
        )
        st.altair_chart(chart,use_container_width=True)

    with col2:
        col2.metric(label="Number of registered EV's in 2021", value= "$"+millify(yearly_total_count[2021], precision=2), delta=(millify(yearly_change[2021])+"%") )
        st.write("")
        st.write("")
        
        vehicle_types_count_2021 = vehicles_df_2021.groupby(['Fuel Type'])['Count'].sum().reset_index()
        chart = alt.Chart(vehicle_types_count_2021).mark_arc().encode(
            theta= alt.Theta(field="Count", type="quantitative"),
            color= alt.Color(field="Fuel Type", type="nominal"),
        )
        st.altair_chart(chart,use_container_width=True)

    with col3:
        col3.metric(label="Number of registered EV's in 2022", value= "$"+millify(yearly_total_count[2022], precision=2), delta=(millify(yearly_change[2022])+"%") )
        st.write("")
        st.write("")
        
        vehicle_types_count_2022 = vehicles_df_2022.groupby(['Fuel Type'])['Count'].sum().reset_index()
        chart = alt.Chart(vehicle_types_count_2022).mark_arc().encode(
            theta= alt.Theta(field="Count", type="quantitative"),
            color= alt.Color(field="Fuel Type", type="nominal"),
        )
        st.altair_chart(chart,use_container_width=True)

    #style the metric card
    style_metric_cards(border_left_color="#DBF227", background_color=("#000000"))


st.write("")

st.write("")

#container for top 10 states with registered EVs and charging stations
dash_3 = st.container()
with dash_3:
    st.write("")
    st.write("")

    # create columns for both graph
    col1,col2 = st.columns(2)

    #Aggregating only the number of registered vehicles in 2022 by state
    vehicles_df_2022 = vehicles_df[(vehicles_df['Year'] != 2020) & (vehicles_df['Year'] != 2021)]

    registered_vehicles_by_state = vehicles_df_2022.groupby('State')['Count'].sum().sort_values(ascending=False)

    top_states_ev_2022 = registered_vehicles_by_state.nlargest(10)

    top_states_ev_2022 = pd.DataFrame(top_states_ev_2022).reset_index()

    

    #Aggregating the number of charging stations available by state
    
    charging_stations_by_state = stations_df.groupby('state').size()
    top_charging_stations_by_state = charging_stations_by_state.nlargest(10)
    top_charging_stations_by_state = pd.DataFrame(top_charging_stations_by_state).reset_index()


    with col1:
        chart = alt.Chart(top_states_ev_2022).mark_bar().encode(
                x=alt.X('Count:Q', title='Number of Registered EVs'),
                y=alt.Y('State:N', sort='-x', title='State')   
            ).properties(
                title="Top 10 States with the most registered EVs in 2022"
            )
                 
        st.altair_chart(chart,use_container_width=True)

    with col2:
        chart = alt.Chart(top_charging_stations_by_state).mark_bar().encode(
                x=alt.X('0:Q', title='Number of Charging Stations'),
                y=alt.Y('state:N', sort='-x', title='State')
        ).properties(
                title="Top 10 States with the most charging stations (to date)"
        )
        
        st.altair_chart(chart,use_container_width=True)


# Aggregating the number of charging stations by state
charging_stations_by_state = stations_df.groupby('state').size()

#Aggregating only the number of registered vehicles in 2022
vehicles_df_2022 = vehicles_df[(vehicles_df['Year'] != 2020) & (vehicles_df['Year'] != 2021)]

registered_vehicles_by_state = vehicles_df_2022.groupby('State')['Count'].sum().sort_values(ascending=False).reset_index()



# Creating a plot
# Analyzing the distribution of charging stations across states

# Aggregating the number of charging stations by state with the adjusted state names
charging_stations_distribution = stations_df['state'].value_counts()


# Pivot the concatenated dataframe to get 'State' and 'Fuel Type' as indexes, and 'Year' as columns
pivot_df = vehicles_df.pivot_table(index=['State', 'Fuel Type'], columns='Year', values='Count', aggfunc='sum').reset_index()


# First, sum up counts by state and year
state_yearly_totals = vehicles_df.groupby(['State', 'Year'])['Count'].sum().unstack()


# Then calculate the growth rate from 2020 to 2022 for each state
state_growth = (state_yearly_totals[2022] - state_yearly_totals[2020]) / state_yearly_totals[2020] * 100


# Fuel Type distribution
fuel_type_popularity = vehicles_df.groupby(['Fuel Type', 'Year'])['Count'].sum().unstack()


#Identify the states with the highest number of electric vehicles:
electric_vehicles_2022 = vehicles_df[(vehicles_df['Year'] == 2022) & (vehicles_df['Fuel Type'] == 'Electric')]
top_states_ev_2022 = electric_vehicles_2022.groupby('State')['Count'].sum().sort_values(ascending=False)


#Calculate the year-over-year percentage change in vehicle counts:
yearly_change = vehicles_df.pivot_table(values='Count', index=['State', 'Fuel Type'], columns='Year').pct_change(axis='columns') * 100


# Total Vehicle Counts by Year
total_vehicles_by_year = pivot_df.sum(numeric_only=True)




