import streamlit as st
import altair as alt

from get_stations import get_stations
from get_vehicles import get_vehicles
from convertjsontodf import convertjsontodf


if 'vehicles_df' not in st.session_state:
    st.session_state.vehicles_df = get_vehicles()

if 'stations_json' not in st.session_state:
    st.session_state.stations_json = get_stations()

if 'stations_df' not in st.session_state:
    st.session_state.stations_df = convertjsontodf() 

vehicles_df = st.session_state["vehicles_df"]
stations_json = st.session_state["stations_json"]
stations_df = st.session_state["stations_df"]


# Create interactive data selector

with st.spinner("Loading Data..."):
    # State selector
    selected_states = st.multiselect("Please select a State(s)", ["All States"] + list(vehicles_df['State'].unique()))

    # Markdown spacer
    st.write("##")

    # Show dataframe based on selection
    filtered_vehicles_df = vehicles_df if "All States" in selected_states else vehicles_df[vehicles_df['State'].isin(selected_states)]

    # Markdown spacer
    st.write("##")

    dash_4 = st.container()

    with dash_4:
        col1, col2 = st.columns(2)

    with col1:
        # Check if the filtered dataframe is empty or if 'Electric' and 'PHEV' are present in 'Fuel Type'
        if filtered_vehicles_df.empty or not set(['Electric', 'PHEV']).issubset(filtered_vehicles_df['Fuel Type']):
            st.write("No data available for the selected State(s) and Fuel Type(s).")
        else:
            # Display filtered data based on selection
            pivoted_df = filtered_vehicles_df.pivot_table(index='Year', columns='Fuel Type', values='Count', fill_value=0)

            # Reset the index to make 'Year' a column again and rename the columns to remove the multi-level indexing if necessary
            pivoted_df.reset_index(inplace=True)
            pivoted_df.columns.name = None

            # Ensure 'Year' is the first column and handle cases where 'Electric' or 'PHEV' might be missing after pivot
            pivoted_df = pivoted_df.reindex(columns=['Year', 'Electric', 'PHEV'], fill_value=0)

            # Show the pivoted dataframe
            st.write("Number of Registered Electric Vehicles(_PHEVs are Plug In Hybrid Vehicles_):", pivoted_df)

    # Markdown spacer
    st.write("##")


    #Display bar chart
    #st.bar_chart(data = filtered_vehicles_df, x='State', y='Count', color='Fuel Type')
    selected_vehicles = filtered_vehicles_df.groupby(['Fuel Type'])['Count'].sum().reset_index()

    with col2:
            chart = alt.Chart(selected_vehicles).mark_arc().encode(
                theta= alt.Theta(field="Count", type="quantitative"),
                color= alt.Color(field="Fuel Type", type="nominal"),
            )
            st.altair_chart(chart,use_container_width=True)


    #Show dataframe based on selection
    filtered_stations_df = stations_df if "All States" in selected_states else stations_df[stations_df['state'].isin(selected_states)]

    # Display filtered data based on selection
    st.write("Charging stations from selected state:", filtered_stations_df)





