import requests

getRoutes = "https://svc.metrotransit.org/NexTrip/Routes?format=json"
getDirections = "https://svc.metrotransit.org/NexTrip/Directions/5?format=json"
getStops = "https://svc.metrotransit.org/NexTrip/Stops/5/4?format=json"
getDepartures = "https://svc.metrotransit.org/NexTrip/11167?format=json"
getTimepointDepartures = "https://svc.metrotransit.org/NexTrip/5/4/7SOL?format=json"

print(requests.get(getRoutes).json())
print(requests.get(getDirections).json())
print(requests.get(getStops).json())
print(requests.get(getDepartures).json())
print(requests.get(getTimepointDepartures).json())

