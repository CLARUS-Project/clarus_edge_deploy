"""
This module provides the concept_drift function. 
The function implements the logic to identify if there exists a concept drift between 
the data provided by the read_data function.
"""

import pandas as pd
import json
import os
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset


def concept_drift(df_ref:pd.DataFrame, df_new:pd.DataFrame) -> bool:
    """
    This module provides the concept_drift function. 

    Return:
        HTML containing a report of the results regarding the concept drift analysis.
    """
    statistical_test = 'ks'
    statistical_threshold = 0.05
                
    report = Report(metrics=[
        DataDriftPreset(stattest=statistical_test, stattest_threshold=statistical_threshold),
    ])

    report.run(reference_data=df_ref, current_data=df_new)

    report_df = pd.DataFrame(json.loads(report.json()))
    n_vars_cd = report_df['metrics'].iloc[0]['result']['number_of_drifted_columns']
    
    report.save_html('reports/data_drift_report.html')
    if n_vars_cd > 0:
        print(f'Detected CONCEPT DRIFT for {n_vars_cd} variables')
        return True
    return False

def update_csv_rows(new_data_point_df:pd.DataFrame, n_rows:int=20) -> pd.DataFrame:
    """
    Updates a CSV file to keep only the last X rows, appending a new data point DataFrame.

    Parameters:
    - file_name (str): The name of the CSV file to update.
    - new_data_point_df (pd.DataFrame): A DataFrame representing the new data point to append.
    """
    # Get the path to the CSV file
    script_dir = os.path.dirname(__file__)
    path_data_new = os.path.join(script_dir, 'winequality-red-detect.csv')
    # Load existing data from the CSV file
    try:
        df_detect = pd.read_csv(path_data_new)
    except FileNotFoundError:
        # If the file does not exist, create an empty DataFrame with columns from the new data point
        df_detect = pd.DataFrame(columns=new_data_point_df.columns)
    
    # Append the new data point
    df_detect = pd.concat([df_detect, new_data_point_df], ignore_index=True)
    
    # Keep only the last 20 rows
    df_detect = df_detect.tail(n_rows)
    
    # Save the updated data back to the CSV file
    df_detect.to_csv(path_data_new, index=False)
    
    return df_detect
