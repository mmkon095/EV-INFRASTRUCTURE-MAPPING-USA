# EV-INFRASTRUCTURE-GAPS-USA

As the adoption of electric vehicles (EVs) continues to grow in the United States, the need for an efficient and well-distributed charging infrastructure becomes increasingly crucial. However, the expansion of EV charging stations has not been uniform across all regions, leading to potential infrastructure gaps that hinder the widespread adoption of electric vehicles. The goal of this Data Engineering project is to assess the current state of EV infrastructure in the United States and identify areas with inadequate charging station coverage.


The Problem Involves the Following Key Objectives:

1. Data Collection: Gather comprehensive data on electric charging station locations, their capacities, and other relevant attributes from various sources, including public databases, charging station operators, and third-party APIs.

2. Electric Vehicle Ownership Data: Obtain data on electric vehicle ownership across different regions in the United States to understand the distribution and penetration of electric vehicles.

3. Geospatial Analysis: Perform geospatial analysis to visualize the distribution of existing charging stations and electric vehicle ownership on a map, identifying areas with high and low coverage.

4. Infrastructure Gap Identification: Utilize data analysis techniques to identify regions or areas that exhibit inadequate charging station coverage relative to the number of electric vehicles present. This analysis should consider population density, driving patterns, and other relevant factors.

5. Quantify the Impact of Gaps: Quantify the potential impact of infrastructure gaps on EV adoption rates and the overall transition to electric mobility in different regions.

6. Recommendation for Expansion: Based on the analysis results, propose data-driven recommendations for the strategic expansion of EV charging infrastructure to bridge the identified gaps effectively.



## Expected Deliverables:

The deliverables for this project will include:

* A comprehensive dataset of charging station locations and attributes, as well as electric vehicle ownership data in the United States.

* Data visualizations and geospatial maps illustrating the distribution of charging stations and electric vehicles.

* Analysis reports identifying regions with infrastructure gaps and assessing their impact on EV adoption.

* Data-driven recommendations for charging station expansion to enhance the overall EV infrastructure.


## Benefits and Implications:

This project's findings and recommendations will have several benefits and implications:

* Policymakers can use the results to inform infrastructure investment decisions and target regions in need of additional charging stations to promote EV adoption.

* Charging station operators can identify opportunities for expanding their networks to meet the rising demand for electric vehicle charging services.

* Electric vehicle manufacturers and businesses can tailor marketing and distribution strategies based on the identified regions with higher EV adoption potential.

* The project will contribute valuable insights to the ongoing efforts to create a sustainable and well-connected electric vehicle charging infrastructure nationwide.

## About the datasets:

EV Population dataset : This dataset shows the Battery Electric Vehicles (BEVs) that are currently registered through Washington State Department of Licensing (DOL) [API from the State of Washington Data Portal](https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2)

* geocoded_column - The center of the ZIP Code for the registered vehicle.
* make - The manufacturer of the vehicle, determined by decoding the Vehicle Identification Number (VIN)
* model - The model of the vehicle, determined by decoding the Vehicle Identification Number (VIN).
* model_year - The model year of the vehicle, determined by decoding the Vehicle Identification Number (VIN).
* city - The city in which the registered owner resides.
* state - This is the geographic region of the country associated with the record. These addresses may be located in other states.
* zip_code - The 5 digit zip code in which the registered owner resides.
* ev_type - This distinguishes the vehicle as all electric or a plug-in hybrid.
* cafv_type - This categorizes vehicle as Clean Alternative Fuel Vehicles (CAFVs) based on the fuel requirement and electric-only range requirement in House Bill 2042 as passed in the 2019 legislative session.
* electric_range - Describes how far a vehicle can travel purely on its electric charge.
* electric_utility - This is the electric power retail service territories serving the address of the registered vehicle.

EV Stations dataset: This dataset shows all US publicly available, planned and temporarily unavailable electric charging locations. [API from the National Renewable Energy Laboratory (NREL) website and developer network](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/all/)

* geometry.coordinates - GPS coordinates of the station
* access_days_time - Hours of operation for the station
* cards_accepted - A space-separated list of payment methods accepted 
* date_last_confirmed - The date the station's details were last confirmed
* open_date - The date that the station began offering the fuel.
* expected_date - For planned stations, the date the station is expected to open or start carrying alternative fuel. For temporarily unavailable stations, the date the station is expected to reopen. This date is estimated.
* station_name - The name of the station.
* station_phone - The phone number of the station.
* facility_type - The type of facility at which the station is located
* city - The city of the station's location.
* intersection_directions - Brief additional information about how to locate the station.
* state - The two character code for the U.S. state or Canadian province/territory of the station's location.
* stree_address - The street address of the station's location.
* zip_code - The ZIP code (postal code) of the station's location
* ev_connector_types - An array of strings identifying the connector types available at this station
* ev_network - The name of the EV charging network.
* ev_pricing - Information about whether and how much users must pay to use the EVSE port.
