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

