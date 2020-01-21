import requests
from requests.exceptions import HTTPError

bus_route = input("Enter your BUS ROUTE: ")
#bus_stop_name = input("Enter your BUS STOP NAME: ")
#direction = input("Enter your DIRECTION: ")

getRoutes = "https://svc.metrotransit.org/NexTrip/Routes?format=json"
getRoutes_response = requests.get(getRoutes).json()
route = int(getRoutes_response[0]["Route"])

getDirections = f"https://svc.metrotransit.org/NexTrip/Directions/{route}?format=json"
# takes Route number
getDirections_response = requests.get(getDirections).json()
direction = int(getDirections_response[1]["Value"])

getStops = f"https://svc.metrotransit.org/NexTrip/Stops/{route}/{direction}?format=json"
# take Route number and Direction
getStops_response = requests.get(getStops).json()
stop = getStops_response[1]["Value"]

getTimepointDepartures = f"https://svc.metrotransit.org/NexTrip/{route}/{direction}/{stop}?format=json"
# take Route number, direction, stop value
getTimepointDepartures_response = requests.get(getTimepointDepartures).json()
nextBus = getTimepointDepartures_response[0]["DepartureText"]
# “METRO Blue Line” “Target Field Station Platform 1” “south”

