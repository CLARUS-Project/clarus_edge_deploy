"""
This module provides the read_data function. 
The function implements the logic to ingest the data and transform it into a pandas format. If any additional auxiliary 
functions are required to accomplish this step, they can be defined within the same script or separated into different 
scripts and included in the concept drift directory.
"""

import pandas as pd
import os

def read_data() -> pd.DataFrame:
    """
    The function implements the logic to ingest the data and transform it into a pandas format.

    In this code example, two csv files are retrieved.

    Return:
        Two Pandas DataFrame representing the reference data and the new data that are going to be compare to identify concept drift.
    """
    script_dir = os.path.dirname(__file__)
    path_data_ref = os.path.join(script_dir, 'winequality-red-ref.csv')
    df_ref = pd.read_csv(path_data_ref)

    path_data_new = os.path.join(script_dir, 'winequality-red-new.csv')
    df_new = pd.read_csv(path_data_new)

    return df_ref, df_new

