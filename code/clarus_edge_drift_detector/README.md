# Clarus_edge_inference

# My Flask API

This project is a simple API built with Flask, Dockerized for easy deployment.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker](#docker)
- [License](#license)

## Project Structure

```
clarus_edge_drift_detector/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├──src/
│      ├── __init__.py
│      ├── concept_drift.py
│      ├── read_data.py
│
├── Dockerfile
├── requirements.txt
├── run.py
├── README.md
```

## Installation

### Prerequisites

- Python 3.9+
- Docker (optional, for containerization)

### Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/CLARUS-Project/clarus_edge_deploy.git
   cd clarus_edge_deploy/code/clarus_edge_drift_detector
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python run.py
   ```

The application will be available at `http://localhost:5000`.

## Usage

### API Endpoints

- **GET /**

  Returns a welcome message.

  ```json
  {
    "message": "API is up!"
  }
  ```

- **GET /api/detect_data_drift**

  Returns if data drift is detected.

  Drift detected: True/False
 

### Docker

#### Build the Docker Image

To build the Docker image, run the following command from the project directory:

```bash
docker build -t clarus_edge_drift_detector:latest .
```

#### Run the Docker Container

To run the Docker container, execute:

```bash
docker run -p 5000:5000 --name clarus_edge_drift_detector --rm clarus_edge_drift_detector:latest
```

The application will be available at `http://localhost:5000`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This README file provides a clear and comprehensive guide for users on how to set up, run, and use the Flask API both locally and with Docker. Adjust the repository URL and other specific details as necessary.