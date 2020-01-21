import requests
import json

url = "https://svc.metrotransit.org/NexTrip/Routes?format=json"

print(requests.get(url).json())
