# Preventative Maintenance for Marine Engines: Predicting Engine Failure

![alt text](Images/Mitsubishi-Marine-Engine.png)

Engine failures can be expensive and can result in downtime. The goal of this project was to build a prediction model based on a dataset to allow user input to see if a engine would fail. These predictions provide insights into what can cause an engine to fail and can be used to monitor engine health.

# Table of Contents

- Dataset
- Questions?
- Data Analysis Graphs
- Predicting Engine Maintenance Status
- Predicting Engine Failure
- Feature Importance
- Future Study
- Credits

# Dataset

![alt text](Images/dataset_picture.png)

- 5200 Rows, 17 Columns

- timestamp: The date of the information in that row
- engine_id: Engine Identifier
- engine_temp: The temperature of the Engine in Celsius
- oil_pressure: Oil pressure in bars. 1 bar is 14.5 psi
- fuel_consumption: Liters per Hour
- vibration_level: Millimeters per Second
- Engine Revolutions per Minute (rev/min)
- engine_load: Percent the Engine is working at (%)
- coolant_temp: Temperature of Engine Coolant in Celsius
- exhaust_temp: Temperature of the Exhaust in Celsius
- running_period: Hours per Week Engine has been running (0 - 168)
- maintenance_status: Warning that Engine needs Maintenance
- failure_mode: If the Engine has Failed, informs of type of Failure
- engine_type: The type of Engine
- fuel_type: The type of Fuel that the Engine uses
- manufacturer: The Manufacturer that produced the Engine

# Questions?

The following are some questions I had prior to starting my initial data analysis:

- What are the most important factors that determine engine failure?
- Do any columns have less of an impact on engine failures?
- Do engines from any manufacturer have a higher chance to fail?

# Data Analysis Graphs

![alt text](Images/manufacturer_vs_failures.png)
![alt text](Images/failure_mode_vs_engines.png)
![alt text](Images/maintenance_status_vs_engines.png)
![alt text](Images/engine_type_vs_engines.png)
![alt text](Images/fuel_vs_engines.png)
![alt text](Images/engine_running_vs_fuel_consumption_hour.png)
![alt text](Images/engine_running_vs_fuel_consumption_week.png)
![alt text](Images/fuel_consumption_week_vs_fuel_consumption_hour.png)
![alt text](Images/engine_load_vs_coolant_temp.png)
![alt text](Images/engine_load_vs_vibration_level.png)
![alt text](Images/engine_load_vs_fuel_consumption_week.png)
![alt text](Images/engine_load_vs_oil_pressure.png)
![alt text](Images/engine_load_vs_engine_temp.png)
![alt text](Images/oil_pressure_vs_coolant_temp.png)
![alt text](Images/engine_temp_vs_coolant_temp.png)
![alt text](Images/vibration_level_vs_oil_pressure.png)
![alt text](Images/oil_pressure_vs_fuel_consumption_week.png)
![alt text](Images/oil_pressure_vs_engine_temp.png)
![alt text](Images/correlations_heatmap.png)

# Predicting Engine Maintenance Status

On this page is the Maintenance Status Prediction Model. Here you can move the sliders and change the options in the select boxes and at the bottom of the page you will get a prediction of what kind of maintenance status you can expect to see with a engine that has all of those settings. The Prediction Model used is a Random Forest Model.

![alt text](Images/maint_status_streamlit.png)

# Predicting Engine Failure

On this page is the Failure Prediction Model. Here you can move the sliders and change the options in the select boxes and at the bottom of the page you will get a prediction of the failure you can expect to see with a engine that has all of those settings. The Prediction Model used is a Random Forest Model.

![alt text](Images/failure_mode_streamlit.png)

# Feature Importance

![alt text](Images/Feature_Importance_Maint_Status.png)
![alt text](Images/Feature_Importance_Fail_Type.png)

- The numbers under Importance all add up to 1. The greater the number the more importance that feature is considered to be.

# Future Study

- Other types of engines besides marine engines
- Engine datasets with more data included
- Look at manufacturers not included in this dataset
- Focus on a single manufacturer and its engines
- Try to compare costs of engines

# Credits

- Image on Home is from here: https://engine-genset.mhi.com/marine-engines
- My dataset was found on Kaggle.com from user Fijabi J. Adekunle: https://www.kaggle.com/datasets/jeleeladekunlefijabi/preventive-maintenance-for-marine-engines
- Referenced for unit of measurements of columns in dataset: https://www.kaggle.com/code/jeleeladekunlefijabi/predictive-maintenance-for-marine-engines-notebook
- Lastly Chad for all of his help.
- Contact Info: tate.cottom@spaceforce.mil