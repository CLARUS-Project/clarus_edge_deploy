"""
This module trigger the airflow DAG when data drift is detected to retrain the model. 
"""
import requests
import re

def trigger_dag(retrain=False, df_retrain=None):
    # Define URLs
    login_url = "http://host.docker.internal:8080/login/"
    trigger_dag_url = "http://host.docker.internal:8080/api/v1/dags/RedWine_MLOps_lifecycle/dagRuns"

    # Create a session
    session = requests.Session()

    # Get the login page to fetch the CSRF token
    login_page = session.get(login_url)
    login_page_html = login_page.text

    # Extract the CSRF token using regex
    csrf_token_pattern = r'<input[^>]*name="csrf_token"[^>]*value="([^"]+)"'
    if csrf_token_pattern:
        csrf_token = re.search(csrf_token_pattern, login_page_html).group(1)
    else:
        raise ValueError("CSRF token not found in the HTML.")

    # Prepare login data with CSRF token
    login_data = {
        "username": "airflow",
        "password": "airflow",
        "csrf_token": csrf_token
    }

    # Perform the login
    login_response = session.post(login_url, data=login_data)

    # Check if login was successful
    if login_response.status_code != 200:
        print("Login failed")
        exit(1)

    # Headers for the API request
    headers = {
        "Content-Type": "application/json"
    }

    # Payload for the API request
    payload = {
        "conf": {"retrain": retrain}  # You can pass any configuration parameters here
    }

    # Trigger the DAG
    trigger_response = session.post(trigger_dag_url, json=payload, headers=headers)

    # Check if the trigger was successful
    if trigger_response.status_code == 200:
        print("DAG triggered successfully")
    else:
        print(f"Failed to trigger DAG: {trigger_response.text}")

    # Get the DAG run status
    dag_run_status_response = session.get(trigger_dag_url, headers=headers)

    # Check if the status retrieval was successful
    if dag_run_status_response.status_code == 200:
        dag_runs = dag_run_status_response.json()
        print("DAG Runs:", dag_runs)
    else:
        print(f"Failed to retrieve DAG run status: {dag_run_status_response.text}")
