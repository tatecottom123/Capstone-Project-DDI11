from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Dict, List

# uvicorn FastAPI:app --reload

log_model = joblib.load("log_model.joblib")
forest_model = joblib.load("forest_model.joblib")
forest_model_fail_type = joblib.load("forest_model_fail_type.joblib")
forest_model_maint_status = joblib.load("forest_model_maint_status.joblib")
lab_enc = joblib.load("lab_enc.joblib")
lab_enc_maint_status = joblib.load("lab_enc_maint_status.joblib")

app = FastAPI()

class EngineData(BaseModel):
    # test_var:int
    engine_temp: float
    oil_pressure: float
    fuel_consumption: float
    vibration_level: float
    rpm: float
    engine_load: float
    coolant_temp: float
    exhaust_temp: float
    running_period: float
    fuel_consumption_per_hour: float
    maintenance_status_Critical: bool
    maintenance_status_Normal: bool 
    maintenance_status_Requires_Maintenance: bool
    engine_type_2_stroke_Low_Speed: bool
    engine_type_2_stroke_Medium_Speed: bool
    engine_type_4_stroke_High_Speed: bool
    engine_type_4_stroke_Medium_Speed: bool
    fuel_type_Diesel: bool
    fuel_type_HFO: bool
    manufacturer_Caterpillar: bool
    manufacturer_MAN_B_W: bool
    manufacturer_Mitsubishi: bool
    manufacturer_Rolls_Royce: bool
    manufacturer_Wartsila: bool
    manufacturer_Yanmar: bool

class EngineMaintData(BaseModel):
    engine_temp: float
    oil_pressure: float
    fuel_consumption: float
    vibration_level: float
    rpm: float
    engine_load: float
    coolant_temp: float
    exhaust_temp: float
    running_period: float
    fuel_consumption_per_hour: float
    engine_type_2_stroke_Low_Speed: bool
    engine_type_2_stroke_Medium_Speed: bool
    engine_type_4_stroke_High_Speed: bool
    engine_type_4_stroke_Medium_Speed: bool
    fuel_type_Diesel: bool
    fuel_type_HFO: bool
    manufacturer_Caterpillar: bool
    manufacturer_MAN_B_W: bool
    manufacturer_Mitsubishi: bool
    manufacturer_Rolls_Royce: bool
    manufacturer_Wartsila: bool
    manufacturer_Yanmar: bool


@app.get("/hello")
def say_hello():
    return {"message": "Hello"}

@app.get("/engine_temp/{engine_temp}")
def get_temp(engine_temp:int):
    return {"engine_temp" : engine_temp}

@app.get("/getengine_temp/{engine_temp}")
def get_engine_temp(engine_temp: float):
    return {"engine_temp": engine_temp}

#@app.get("/predict")
#def get_predict():
#    return {"message": "Please use POST method to predict"}

@app.post("/predict_test")
def predict_test(test_bar:Dict = Body(...)):
    return {"message": test_bar}

@app.post("/predict")
def failure_predictor(data: List[EngineData]):
    # return "Request Received"
    dataframe = pd.DataFrame([item.model_dump() for item in data])

    print("Request Received")
    try:
        prediction = forest_model.predict_proba(dataframe)
        encoded_fail_type_prediction = forest_model_fail_type.predict(dataframe)
        fail_type_prediction = lab_enc.inverse_transform(encoded_fail_type_prediction)
        print()
        y_pred = [1 if i > 0.5 else 0 for i in prediction[:, 1]]
        if y_pred[0] == 1:
            return {"prediction": f"{y_pred[0]}", "message": "The Engine has Failed!", "Test": f"{prediction}", "Fail Type": f"{fail_type_prediction[0]}"} 
        else:
            return {"prediction": f"{y_pred[0]}", "message": "The Engine is Running Properly!"}

        # return {"prediction": f"{prediction[0]}", "message": "The Engine has Failed!", "Test": f"{y_pred}"} 
    except Exception as e:
        return {"Error is": f"{str(e)}", "message": "No message"}
    
@app.post("/predictMaint")
def maint_predictor(data: List[EngineMaintData]):
    # return "Request Received"
    dataframe2 = pd.DataFrame([item.model_dump() for item in data])

    print("Request Received")
    try:
        prediction_maint = forest_model_maint_status.predict_proba(dataframe2)
        encoded_maint_status_prediction = forest_model_maint_status.predict(dataframe2)
        maint_status_prediction = lab_enc_maint_status.inverse_transform(encoded_maint_status_prediction)
        #print()
        #y_pred = [1 if i > 0.5 else 0 for i in prediction_maint[:, 1]]
        #if y_pred[0] == 1:
        if maint_status_prediction != "Normal":
            return {"prediction": f"{maint_status_prediction}", "message": "The Engine has an issue!", "Test": f"{prediction_maint}", "Maintenance Status": f"{maint_status_prediction[0]}"} 
        else:
            return {"prediction": f"{maint_status_prediction}", "message": "The Engine is Running Properly!"}

        # return {"prediction": f"{prediction[0]}", "message": "The Engine has Failed!", "Test": f"{y_pred}"} 
    except Exception as e:
        return {"Error is": f"{str(e)}", "message": "No message"}
   