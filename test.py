import requests

URL = "http://127.0.0.1:8000"

# Testing Miles
send_data = {"type": "miles", "distance": "5.4"}

time_request = requests.post(url=URL, json=send_data)

data = float(time_request.json())

print("Converted to kilometers:", data)

send_data2 = {"type": "kilometers", "distance": "2"}

request2 = requests.post(url=URL, json=send_data2)

data2 = float(request2.json())
print("Converted to Miles:", data2)
