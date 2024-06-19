import mlflow
from mlflow.tracking import MlflowClient
import os

def check_and_download_new_model(current_version, model_name, model_stage='Production', download_path='./model'):
    """
    Checks if there is a new model version in production in MLflow and downloads it if the version is newer than the current one.

    Parameters:
    - current_version (int): The current version of the model.
    - model_name (str): The name of the model in MLflow.
    - model_stage (str): The stage of the model to check (default is 'Production').
    - download_path (str): The directory path to download the new model.

    Returns:
    - bool: True if a new model version was downloaded, False otherwise.
    """
    client = MlflowClient()
    
    # Get the latest version of the model in the specified stage
    latest_versions = client.get_latest_versions(model_name, stages=[model_stage])
    
    if not latest_versions:
        print(f"No models found in stage: {model_stage}")
        return False
    
    latest_model = latest_versions[0]
    latest_version = int(latest_model.version)
    
    if latest_version > current_version:
        print(f"New model version {latest_version} found. Current version: {current_version}. Downloading...")
        
        # Create the download directory if it doesn't exist
        os.makedirs(download_path, exist_ok=True)
        
        # Download the new model
        model_uri = f"models:/{model_name}/{latest_version}"
        mlflow.pyfunc.load_model(model_uri, dst_path=download_path)
        
        print(f"Model version {latest_version} downloaded to {download_path}")
        return True
    else:
        print(f"Current model version ({current_version}) is up-to-date.")
        return False