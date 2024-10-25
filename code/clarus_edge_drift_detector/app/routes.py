"""
This module runs all the functions needed for the concept drift detection. 
"""
from app.src.read_data import read_data
from app.src.concept_drift import concept_drift   
from flask import current_app as app 
from flask import jsonify
from app.trigger_dag_airflow import trigger_dag

@app.route('/')
def hello_world():
    return jsonify({"message": "API is up!"})

@app.route('/api/detect_data_drift', methods=['GET'])
def detect_data_drift():
    # Get the data of reference and new data
    df_ref, df_new = read_data()
    # Detect the concept drift
    drift_detected = concept_drift(df_ref, df_new)
    # Trigger the retraining:
    if drift_detected==True:
        trigger_dag()
        return jsonify({"message": "Drift detected and retraining triggered"})
    else:
        return jsonify({"message": "Drift NOT detected"})
