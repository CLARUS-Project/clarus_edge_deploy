"""
This module runs all the functions needed for the concept drift detection. 
"""
from app.src.read_data import read_data
from app.src.concept_drift import concept_drift, update_csv_rows   
from flask import current_app as app 
from flask import jsonify

@app.route('/')
def hello_world():
    return jsonify({"message": "API is up!"})

@app.route('/api/detect_data_drift', methods=['GET'])
def detect_data_drift():
    # Get the data of reference and new data
    df_ref, df_new = read_data()
    df_detect = update_csv_rows(df_new)
    # Detect the concept drift
    drift_detected = concept_drift(df_ref, df_detect)
    return jsonify({"message": f"Drift detected: {drift_detected}"})