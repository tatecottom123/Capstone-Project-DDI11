import requests
import streamlit as st
import pandas as pd
from PIL import Image

# streamlit run streamlit_app.py

st.sidebar.header("Midterm Project Home")
category = st.sidebar.selectbox("Choose Category", ["Home","Dataset", "Questions?", "Data Analysis Graphs", "Predicting Engine Maintenance Status", "Predicting Engine Failure", "Feature Importance", "Future Study", "Credits"])

if category == "Home":

    st.title("Preventative Maintenance for Marine Engines: Predicting Engine Failure ")
    engine_image = Image.open('Images/Mitsubishi-Marine-Engine.png')
    st.image(engine_image, caption = "A Mitsubishi Marine Engine")
    st.write("Engine failures can be expensive and can result in downtime. The goal of this project was to build a prediction model based on a dataset to allow user input to see if a engine would fail. These predictions provide insights into what can cause an engine to fail and can be used to monitor engine health.")

if category == "Dataset":
    
    st.title("Preventative Maintenance for Marine Engines Dataset")
    df = pd.read_csv("marine_engine_data.csv")
    st.write("5200 Rows, 17 Columns")
    st.dataframe(df)
    st.markdown("* timestamp: The date of the information in that row")
    st.markdown("* engine_id: Engine Identifier")
    st.markdown("* engine_temp: The temperature of the Engine in Celsius")
    st.markdown("* oil_pressure: Oil pressure in bars. 1 bar is 14.5 psi")
    st.markdown("* fuel_consumption: Liters per Hour")
    st.markdown("* vibration_level: Millimeters per Second")
    st.markdown("* Engine Revolutions per Minute (rev/min)")
    st.markdown("* engine_load: Percent the Engine is working at (%)")
    st.markdown("* coolant_temp: Temperature of Engine Coolant in Celsius")
    st.markdown("* exhaust_temp: Temperature of the Exhaust in Celsius")
    st.markdown("* running_period: Hours per Week Engine has been running (0 - 168)")
    st.markdown("* maintenance_status: Warning that Engine needs Maintenance")
    st.markdown("* failure_mode: If the Engine has Failed, informs of type of Failure")
    st.markdown("* engine_type: The type of Engine")
    st.markdown("* fuel_type: The type of Fuel that the Engine uses")
    st.markdown("* manufacturer: The Manufacturer that produced the Engine")

if category == "Questions?":
    
    st.title("Questions?")
    st.write("The following are some questions I had prior to starting my initial data analysis:")
    st.markdown("* What are the most important factors that determine engine failure?")
    st.markdown("* Do any columns have less of an impact on engine failures?")
    st.markdown("* Do engines from any manufacturer have a higher chance to fail?")

if category == "Data Analysis Graphs":
    
    st.title("Data Analysis Graphs")

    tab1, tab2, tab3, tab4 = st.tabs(["Manufacturer/Engines", "Failure Mode/Engines", "Maintenance Status/Engines", "Engine Type/Number of Engines"])

    with tab1:

        manufac_vs_failures = Image.open('Images/manufacturer_vs_failures.png')
        st.image(manufac_vs_failures)

    with tab2:

        failmode_vs_engines = Image.open('Images/failure_mode_vs_engines.png')
        st.image(failmode_vs_engines)

    with tab3:

        maintstat_vs_engines = Image.open('Images/maintenance_status_vs_engines.png')
        st.image(maintstat_vs_engines)

    with tab4:

        enginetype_vs_num_engines = Image.open('Images/engine_type_vs_engines.png')
        st.image(enginetype_vs_num_engines)

    tab5, tab6, tab7, tab8 = st.tabs(["Fuel Type/Engines", "Time Running/Fuel Cons./Week", "Time Running/Fuel Cons./Hour", "Fuel Cons./Week/Fuel Cons./Hour"])

    with tab5:

        fueltype_vs_engines = Image.open('Images/fuel_vs_engines.png')
        st.image(fueltype_vs_engines)

    with tab6:

        engine_running_vs_fuel_cons_week = Image.open('Images/engine_running_vs_fuel_consumption_week.png')
        st.image(engine_running_vs_fuel_cons_week)

    with tab7:

        engine_running_vs_fuel_cons_hour = Image.open('Images/engine_running_vs_fuel_consumption_hour.png')
        st.image(engine_running_vs_fuel_cons_hour)

    with tab8:

        fuelconsweek_vs_fuelconshour = Image.open('Images/fuel_consumption_week_vs_fuel_consumption_hour.png')
        st.image(fuelconsweek_vs_fuelconshour)

    tab9, tab10, tab11, tab12 = st.tabs(["Engine Load/Coolant Temp", "Engine Load/Vibration Level", "Engine Load/Fuel Cons/Week", "Engine Load/Oil Pressure"])

    with tab9:

        engineload_vs_coolant_temp = Image.open('Images/engine_load_vs_coolant_temp.png')
        st.image(engineload_vs_coolant_temp)

    with tab10:

        engineload_vs_vibration = Image.open('Images/engine_load_vs_vibration_level.png')
        st.image(engineload_vs_vibration)

    with tab11:

        engineload_vs_fuelcons_week = Image.open('Images/engine_load_vs_fuel_consumption_week.png')
        st.image(engineload_vs_fuelcons_week)

    with tab12:

        engineload_vs_oil_pressure = Image.open('Images/engine_load_vs_oil_pressure.png')
        st.image(engineload_vs_oil_pressure)

    tab13, tab14, tab15, tab16 = st.tabs(["Engine Load/Engine Temp", "Oil Pressure/Coolant Temp", "Engine Temp/Coolant Temp", "Vibration Level/Oil Pressure"])

    with tab13:

        engineload_vs_enginetemp = Image.open('Images/engine_load_vs_engine_temp.png')
        st.image(engineload_vs_enginetemp)

    with tab14:

        oilpressure_vs_coolant_temp = Image.open('Images/oil_pressure_vs_coolant_temp.png')
        st.image(oilpressure_vs_coolant_temp)

    with tab15:

        enginetemp_vs_coolant_temp = Image.open('Images/engine_temp_vs_coolant_temp.png')
        st.image(enginetemp_vs_coolant_temp)

    with tab16:

        vibration_level_vs_oil_pressure = Image.open('Images/vibration_level_vs_oil_pressure.png')
        st.image(vibration_level_vs_oil_pressure)

    tab17, tab18, tab19 = st.tabs(["Oil Pressure/Fuel Cons./Week", "Oil Pressure/Engine Temp", "Correlations Heatmap"])

    with tab17:

        oilpressure_vs_fuel_cons_week = Image.open('Images/oil_pressure_vs_fuel_consumption_week.png')
        st.image(oilpressure_vs_fuel_cons_week)

    with tab18:

        oilpressure_vs_engine_temp = Image.open('Images/oil_pressure_vs_engine_temp.png')
        st.image(oilpressure_vs_engine_temp)

    with tab19:

        heatmap = Image.open('Images/correlations_heatmap.png')
        st.image(heatmap)

if category == "Feature Importance":

    st.title("Feature Importance")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Maintenance Status")
        feat_imp_maint_status = Image.open('Images/Feature_Importance_Maint_Status.png')
        st.image(feat_imp_maint_status)

    with col2:
        st.header("Failure Type")
        feat_imp_fail_type = Image.open('Images/Feature_Importance_Fail_Type.png')
        st.image(feat_imp_fail_type)

    st.write("The numbers under Importance all add up to 1. The greater the number the more importance that feature is considered to be.")

if category == "Predicting Engine Maintenance Status":

    st.subheader("Select your parameters to predict Maintenance Status:")

    options = [True, False]
    default_false = options.index(False)

    engine_temp = st.slider('Engine Temperature (Celsius)', 50.0,120.0, 83.92)
    oil_pressure = st.slider('Oil Pressure (bars)(1 bar = 14.5 psi)', 5.0, 8.0, 7.0)
    fuel_consumption_per_hour = st.slider('Fuel Consumption per Hour (Liters)', 100.0, 800.0, 116.0)
    fuel_consumption = st.slider('Fuel Consumption per Week (Liters)', 1000.0, 13000.0, 6444.0)
    vibration_level = st.slider('Vibration Level (mm/s)', 2.0, 5.0, 4.0)
    rpm = st.slider('RPM (rev/min)', 700.0, 2300.0, 1487.5)
    engine_load = st.slider('Engine Load (% Engine is Working at)', 1.0, 100.0, 63.92)
    coolant_temp = st.slider('Coolant Temperature (Celsius)', 60.0, 110.0, 78.2)
    exhaust_temp = st.slider('Exhaust Temperature (Celsius)', 420.0, 460.0, 450.0)
    running_period = st.slider('Running Period (Hours per Week (0 - 168))', 0.0, 180.0, 120.1)

    engine_type_box = st.selectbox('Select Engine Type', ["2 Stroke Medium-Speed", "2 Stroke Low-Speed", "4 Stroke Medium-Speed", "4 Stroke High-Speed"])

    if engine_type_box == "2 Stroke Low-Speed":
        engine_type_2_stroke_Low_Speed = True
        engine_type_2_stroke_Medium_Speed = False
        engine_type_4_stroke_Medium_Speed = False
        engine_type_4_stroke_High_Speed = False

    elif engine_type_box == "2 Stroke Medium-Speed":
        engine_type_2_stroke_Low_Speed = False
        engine_type_2_stroke_Medium_Speed = True
        engine_type_4_stroke_Medium_Speed = False
        engine_type_4_stroke_High_Speed = False

    elif engine_type_box == "4 Stroke Medium-Speed":
        engine_type_2_stroke_Low_Speed = False
        engine_type_2_stroke_Medium_Speed = False
        engine_type_4_stroke_Medium_Speed = True
        engine_type_4_stroke_High_Speed = False
    
    elif engine_type_box == "4 Stroke High-Speed":
        engine_type_2_stroke_Low_Speed = False
        engine_type_2_stroke_Medium_Speed = False
        engine_type_4_stroke_Medium_Speed = False
        engine_type_4_stroke_High_Speed = True

    fuel_type_box = st.selectbox('Select Fuel Type', ["Diesel", "HFO"])

    if fuel_type_box == "Diesel":
        fuel_type_Diesel = True
        fuel_type_HFO = False

    elif fuel_type_box == "HFO":
        fuel_type_Diesel = False
        fuel_type_HFO = True

    manufacturer_box = st.selectbox('Select Engine Manufacturer', ["Caterpillar", "MAN B&W", "Mitsubishi", "Rolls-Royce", "Wärtsilä", "Yanmar"])

    if manufacturer_box == "Caterpillar":
        manufacturer_Caterpillar = True
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = False
        manufacturer_Yanmar = False

    elif manufacturer_box == "MAN B&W":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = True
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = False
        manufacturer_Yanmar = False

    elif manufacturer_box == "Mitsubishi":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = True
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = False
        manufacturer_Yanmar = False

    elif manufacturer_box == "Rolls-Royce":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = True
        manufacturer_Wartsila = False
        manufacturer_Yanmar = False

    elif manufacturer_box == "Wärtsilä":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = True
        manufacturer_Yanmar = False

    elif manufacturer_box == "Yanmar":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = False
        manufacturer_Yanmar = True

    user_input = [{'engine_temp': float(engine_temp),
                'oil_pressure': float(oil_pressure),
                'fuel_consumption': float(fuel_consumption),
                'vibration_level': float(vibration_level),
                'rpm': float(rpm),
                'engine_load': float(engine_load),
                'coolant_temp': float(coolant_temp),
                'exhaust_temp': float(exhaust_temp),
                'running_period': float(running_period),
                'fuel_consumption_per_hour': float(fuel_consumption_per_hour),
                'engine_type_2_stroke_Low_Speed': bool(engine_type_2_stroke_Low_Speed),
                'engine_type_2_stroke_Medium_Speed': bool(engine_type_2_stroke_Medium_Speed),
                'engine_type_4_stroke_High_Speed': bool(engine_type_4_stroke_High_Speed),
                'engine_type_4_stroke_Medium_Speed': bool(engine_type_4_stroke_Medium_Speed),
                'fuel_type_Diesel': bool(fuel_type_Diesel),
                'fuel_type_HFO': bool(fuel_type_HFO),
                'manufacturer_Caterpillar': bool(manufacturer_Caterpillar),
                'manufacturer_MAN_B_W': bool(manufacturer_MAN_B_W),
                'manufacturer_Mitsubishi': bool(manufacturer_Mitsubishi),
                'manufacturer_Rolls_Royce': bool(manufacturer_Rolls_Royce),
                'manufacturer_Wartsila': bool(manufacturer_Wartsila),
                'manufacturer_Yanmar': bool(manufacturer_Yanmar)
                        }]
    # test_var = st.slider("Test", 1, 10, 5)
    # user_input = [{"test_var":test_var}]

    # test_json = {"test_bar":200.0}

    response = requests.post("http://127.0.0.1:8000/predictMaint", json=user_input)
    #response = requests.post("http://127.0.0.1:8000/predict_test", json=test_json)

    st.write("Ran request")

    if response.status_code == 200:
        prediction_hd = response.json()
        st.write(prediction_hd)
        st.write(f'Prediction: {prediction_hd["message"]}')
        st.write(response.status_code)
    else:
        st.write(f"Error: {response.status_code} - {response.text}")
        st.write(response.status_code)    

if category == "Predicting Engine Failure":

    st.subheader("Select your parameters to predict if the engine has failed:")

    options = [True, False]
    default_false = options.index(False)

    engine_temp = st.slider('Engine Temperature (Celsius)', 50.0,120.0, 83.92)
    oil_pressure = st.slider('Oil Pressure (bars)(1 bar = 14.5 psi)', 5.0, 8.0, 7.0)
    fuel_consumption_per_hour = st.slider('Fuel Consumption per Hour (Liters)', 100.0, 800.0, 116.0)
    fuel_consumption = st.slider('Fuel Consumption per Week (Liters)', 1000.0, 13000.0, 6444.0)
    vibration_level = st.slider('Vibration Level (mm/s)', 2.0, 5.0, 4.0)
    rpm = st.slider('RPM (rev/min)', 700.0, 2300.0, 1487.5)
    engine_load = st.slider('Engine Load (% Engine is Working at)', 1.0, 100.0, 63.92)
    coolant_temp = st.slider('Coolant Temperature (Celsius)', 60.0, 110.0, 78.2)
    exhaust_temp = st.slider('Exhaust Temperature (Celsius)', 420.0, 460.0, 450.0)
    running_period = st.slider('Running Period (Hours per Week (0 - 168))', 0.0, 180.0, 120.1)

    maintenance_box = st.selectbox('Select Maintenance Status', ["Normal", "Requires Maintenance", "Critical"])

    if maintenance_box == "Normal":
        maintenance_status_Normal = True
        maintenance_status_Requires_Maintenance = False
        maintenance_status_Critical = False

    elif maintenance_box == "Requires Maintenance":
        maintenance_status_Normal = False
        maintenance_status_Requires_Maintenance = True
        maintenance_status_Critical = False

    elif maintenance_box == "Critical":
        maintenance_status_Normal = False
        maintenance_status_Requires_Maintenance = False
        maintenance_status_Critical = True

    engine_type_box = st.selectbox('Select Engine Type', ["2 Stroke Medium-Speed", "2 Stroke Low-Speed", "4 Stroke Medium-Speed", "4 Stroke High-Speed"])

    if engine_type_box == "2 Stroke Low-Speed":
        engine_type_2_stroke_Low_Speed = True
        engine_type_2_stroke_Medium_Speed = False
        engine_type_4_stroke_Medium_Speed = False
        engine_type_4_stroke_High_Speed = False

    elif engine_type_box == "2 Stroke Medium-Speed":
        engine_type_2_stroke_Low_Speed = False
        engine_type_2_stroke_Medium_Speed = True
        engine_type_4_stroke_Medium_Speed = False
        engine_type_4_stroke_High_Speed = False

    elif engine_type_box == "4 Stroke Medium-Speed":
        engine_type_2_stroke_Low_Speed = False
        engine_type_2_stroke_Medium_Speed = False
        engine_type_4_stroke_Medium_Speed = True
        engine_type_4_stroke_High_Speed = False
    
    elif engine_type_box == "4 Stroke High-Speed":
        engine_type_2_stroke_Low_Speed = False
        engine_type_2_stroke_Medium_Speed = False
        engine_type_4_stroke_Medium_Speed = False
        engine_type_4_stroke_High_Speed = True

    fuel_type_box = st.selectbox('Select Fuel Type', ["Diesel", "HFO"])

    if fuel_type_box == "Diesel":
        fuel_type_Diesel = True
        fuel_type_HFO = False

    elif fuel_type_box == "HFO":
        fuel_type_Diesel = False
        fuel_type_HFO = True

    manufacturer_box = st.selectbox('Select Engine Manufacturer', ["Caterpillar", "MAN B&W", "Mitsubishi", "Rolls-Royce", "Wärtsilä", "Yanmar"])

    if manufacturer_box == "Caterpillar":
        manufacturer_Caterpillar = True
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = False
        manufacturer_Yanmar = False

    elif manufacturer_box == "MAN B&W":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = True
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = False
        manufacturer_Yanmar = False

    elif manufacturer_box == "Mitsubishi":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = True
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = False
        manufacturer_Yanmar = False

    elif manufacturer_box == "Rolls-Royce":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = True
        manufacturer_Wartsila = False
        manufacturer_Yanmar = False

    elif manufacturer_box == "Wärtsilä":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = True
        manufacturer_Yanmar = False

    elif manufacturer_box == "Yanmar":
        manufacturer_Caterpillar = False
        manufacturer_MAN_B_W = False
        manufacturer_Mitsubishi = False
        manufacturer_Rolls_Royce = False
        manufacturer_Wartsila = False
        manufacturer_Yanmar = True

    user_input = [{'engine_temp': float(engine_temp),
                'oil_pressure': float(oil_pressure),
                'fuel_consumption': float(fuel_consumption),
                'vibration_level': float(vibration_level),
                'rpm': float(rpm),
                'engine_load': float(engine_load),
                'coolant_temp': float(coolant_temp),
                'exhaust_temp': float(exhaust_temp),
                'running_period': float(running_period),
                'fuel_consumption_per_hour': float(fuel_consumption_per_hour),
                'maintenance_status_Critical': bool(maintenance_status_Critical),
                'maintenance_status_Normal': bool(maintenance_status_Normal),
                'maintenance_status_Requires_Maintenance': bool(maintenance_status_Requires_Maintenance),
                'engine_type_2_stroke_Low_Speed': bool(engine_type_2_stroke_Low_Speed),
                'engine_type_2_stroke_Medium_Speed': bool(engine_type_2_stroke_Medium_Speed),
                'engine_type_4_stroke_High_Speed': bool(engine_type_4_stroke_High_Speed),
                'engine_type_4_stroke_Medium_Speed': bool(engine_type_4_stroke_Medium_Speed),
                'fuel_type_Diesel': bool(fuel_type_Diesel),
                'fuel_type_HFO': bool(fuel_type_HFO),
                'manufacturer_Caterpillar': bool(manufacturer_Caterpillar),
                'manufacturer_MAN_B_W': bool(manufacturer_MAN_B_W),
                'manufacturer_Mitsubishi': bool(manufacturer_Mitsubishi),
                'manufacturer_Rolls_Royce': bool(manufacturer_Rolls_Royce),
                'manufacturer_Wartsila': bool(manufacturer_Wartsila),
                'manufacturer_Yanmar': bool(manufacturer_Yanmar)
                        }]
    # test_var = st.slider("Test", 1, 10, 5)
    # user_input = [{"test_var":test_var}]

    # test_json = {"test_bar":200.0}

    response = requests.post("http://127.0.0.1:8000/predict", json=user_input)
    #response = requests.post("http://127.0.0.1:8000/predict_test", json=test_json)

    # st.write(user_input)
    st.write("Ran request")

    if response.status_code == 200:
        prediction_hd = response.json()
        st.write(prediction_hd)
        st.write(f'Prediction: {prediction_hd["message"]}')
        st.write(response.status_code)
    else:
        st.write(f"Error: {response.status_code} - {response.text}")
        st.write(response.status_code)

if category == "Future Study":

    st.title("Future Study")

    st.markdown("* Other types of engines besides marine engines")
    st.markdown("* Engine datasets with more data included")
    st.markdown("* Look at manufacturers not included in this dataset")
    st.markdown("* Focus on a single manufacturer and its engines")
    st.markdown("* Try to compare costs of engines")

if category == "Credits":
    st.title("Credits")
    st.markdown("* Image on Home is from here: https://engine-genset.mhi.com/marine-engines")
    st.markdown("* My dataset was found on Kaggle.com from user Fijabi J. Adekunle: https://www.kaggle.com/datasets/jeleeladekunlefijabi/preventive-maintenance-for-marine-engines")
    st.markdown("* Referenced for unit of measurements of columns in dataset: https://www.kaggle.com/code/jeleeladekunlefijabi/predictive-maintenance-for-marine-engines-notebook")
    st.markdown("* Lastly Chad for all of his help.")

    st.write("Contact Info: tate.cottom@spaceforce.mil")