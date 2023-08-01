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

* geocoded_column
* make
* model
* model_year
* city
* state
* zip_code
* ev_type
* cafv_type
* electric_range
* electric_utility

EV Stations dataset: This dataset shows all US publicly available electric charging locations.[API from the National Renewable Energy Laboratory (NREL) website and developer network](https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/all/)

* geometry.coordinates
* access_code
* access_days_time
* cards_accepted
* date_last_confirmed
* open_date
* expected_date
* station_name
* station_phone
* facility_type
* city
* intersection_directions
* state
* stree_address
* zip_code
* ev_connector_types
* ev_network
* ev_pricing
