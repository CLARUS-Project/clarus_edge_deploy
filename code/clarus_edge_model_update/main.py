from app.mlflow_registry import check_and_download_new_model

current_version = 1
model_name = 'my_model'
download_path = './model'

# Check if there is a new model version in MLflow and download it if it is newer than the current version
new_model_downloaded = check_and_download_new_model(current_version, model_name, download_path=download_path)
# If a new model was downloaded
if new_model_downloaded:
    print(f"New model downloaded: {new_model_downloaded}")
    # Update inference model with the new model
