# EV-INFRASTRUCTURE-GAPS-USA


![EVEY2](https://github.com/mmkon095/EV-INFRASTRUCTURE-GAPS-USA/assets/80499087/a28dfa97-840d-43e7-97ea-3e0384894c73)

<br/>

# Project Description
As the adoption of electric vehicles (EVs) continues to grow in the United States, the need for an efficient and well-distributed charging infrastructure becomes increasingly crucial. However, the expansion of EV charging stations has not been uniform across all regions, leading to potential infrastructure gaps that hinder the widespread adoption of electric vehicles. The goal of this Data Engineering project is to assess the current state of EV infrastructure in the United States and map areas with inadequate charging station coverage.


The Problem Involves the Following Key Objectives:

1. Data Collection: Gather comprehensive data on electric charging station locations, their capacities, and other relevant attributes from various sources, including public databases, charging station operators, and third-party APIs.

2. Electric Vehicle Ownership Data: Obtain data on electric vehicle ownership across different regions in the United States to understand the distribution and penetration of electric vehicles.

3. Geospatial Analysis: Perform geospatial analysis to visualize the distribution of existing charging stations and electric vehicle ownership on a map, identifying areas with high and low coverage.

4. Infrastructure Gap Identification: Utilize data analysis techniques to identify regions or areas that exhibit inadequate charging station coverage relative to the number of electric vehicles present.

5. Quantify the Impact of Gaps: Quantify the potential impact of infrastructure gaps on EV adoption rates and the overall transition to electric mobility in different regions.

6. Recommendation for Expansion: Based on the analysis results, propose data-driven recommendations for the strategic expansion of EV charging infrastructure to bridge the identified gaps effectively.

<br/>

## Expected Deliverables:

The deliverables for this project will include:

* A comprehensive dataset of charging station locations and attributes, as well as electric vehicle ownership data in the United States.

* Data visualizations and geospatial maps illustrating the distribution of charging stations and electric vehicles.

* Analysis reports identifying regions with infrastructure gaps and assessing their impact on EV adoption.

* Data-driven recommendations for charging station expansion to enhance the overall EV infrastructure.

<br/>

## Benefits and Implications:

This project's findings and recommendations will have several benefits and implications:

* Policymakers can use the results to inform infrastructure investment decisions and target regions in need of additional charging stations to promote EV adoption.

* Charging station operators can identify opportunities for expanding their networks to meet the rising demand for electric vehicle charging services.

* Electric vehicle manufacturers and businesses can tailor marketing and distribution strategies based on the identified regions with higher EV adoption potential.

* The project will contribute valuable insights to the ongoing efforts to create a sustainable and well-connected electric vehicle charging infrastructure nationwide.

  <br/>

## About the datasets:

EV Population dataset : This dataset shows the registered Battery Electric Vehicles (BEVs) and Plug In Hybrid Electric Vehicles (PHEV) that are light-duty vehicles in the year 2022  [Available on the US Dept of Energy's Alternative Fuels Data Center](https://afdc.energy.gov/vehicle-registration?year=2022)

* Fuel Type - Electric or Plug-In Hybrid Electric
* Count - Count of vehicles registered
* state - This is the geographic region of the country associated with the record


  <br/>

EV Stations dataset: This dataset shows all US publicly available, planned and temporarily unavailable electric charging locations. [API from the National Renewable Energy Laboratory (NREL) website and developer network](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/all/)

* geometry.coordinates - GPS coordinates of the station
* access_days_time - hours of operation for the station
* cards_accepted - a space-separated list of payment methods accepted 
* date_last_confirmed - the date the station's details were last confirmed
* open_date - the date that the station began offering the fuel.
* expected_date - for planned stations, the date the station is expected to open or start carrying alternative fuel. For temporarily unavailable stations, the date the station is expected to reopen. This date is estimated.
* station_name - the name of the station.
* station_phone - the phone number of the station.
* facility_type - the type of facility at which the station is located
* city - the city of the station's location.
* intersection_directions - brief additional information about how to locate the station.
* state - the two character code for the U.S. state or Canadian province/territory of the station's location.
* stree_address - the street address of the station's location.
* zip_code - the ZIP code (postal code) of the station's location
* ev_connector_types - an array of strings identifying the connector types available at this station
* ev_network - the name of the EV charging network.
* ev_pricing - information about whether and how much users must pay to use the EVSE port.
* ev_level1_evse_num - the number of Level 1 EVSE ports available at the station
* ev_level2_evse_num - the number of Level 2 EVSE ports available at the station
* ev_dc_fast_num - the number of DC Fast EVSE ports available at the station

  <br/>

  ## Architecture

  ## Data Model

  ## ETL Pipeline
