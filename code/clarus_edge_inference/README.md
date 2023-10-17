# Clarus_edge_inference

## Deployment instructions

**Build and start the docker-containers.** To this end, inside the directory *clarus_edge_inference* run the following command:

```
docker-compose up
```

## Usage

In a new terminal outside the docker container open a python terminal runing the following command. 

```
python3
```

Then, run the inference task. You can use the following example.

```
import requests

data = {
    "datos" : "{'fixed acidity':6.2,'volatile acidity':0.66,'citric acid':0.48,'residual sugar':1.2,'chlorides':0.029,'free sulfur dioxide': 29,'total sulfur dioxide': 75, 'density': 0.98, 'pH': 3.33, 'sulphates': 0.39, 'alcohol': 12.8}",

    "model" : 'runs:/518ed535f2994ea383060fe3161717f1/model'
}

resp = requests.get(url = 'http://172.16.56.43:381/predict',params = data)
resp.text
```

**Note:** If the inference is going to be done inside a docker container service in the same docker-compose.yml the ip adress can be replaces as follows:

```
resp = requests.get(url = 'http://edge_inference:381/predict',params = data)
```