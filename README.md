# Microservice-A Unit Converter

## Description
This microservice takes a mile or kilometer value and
returns a value that is converted to the other unit.

Miles -> Kilometers

Kilometers -> Miles

## Prerequisites
The microservice runs a server where the user can use http requests to convert values.
The server runs using uvicorn and fastAPI.

- Must have python 3.x installed
- Must have Fastapi installed
- Must have uvicorn installed


## Setup
1. Download main.py from this repo.
2. Install the required dependencies if needed.
3. In a terminal located at the local directory of the main.py file, run the code ```uvicorn main:app --reload```
4. If you change the name of the file, change the name main to the file name when running the server.
5. To change the server address, add URL after the code mentioned above.


## Request Data Instruction

1. By using any http request service, you can request a conversion from the URL where the 
microservice service is running. 
2. The default server runs on a local host ```127.0.0.1:8000```
3. In this case, using a post request at ```127.0.0.1:8000``` with the proper data will return a converted number.
4. Here is an example request using python and requests module.
```
send_data = {"type": "miles", "distance": "5.4"}
time_request = requests.post(url=URL, json=send_data)
```

## Receive Data Instruction
When requesting data using the instructions above, fastAPI will automatically return
a response with the required data.
In the example above it would be stored in time_request.
To convert this json to usable data use a json converter. Here is an example in python.
```
data = float(time_request.json())
```
This will make it so the variable data has the converted value in a float.

## UML Diagram

![Microservice A.png](..%2F..%2F..%2FDownloads%2FMicroservice%20A.png)