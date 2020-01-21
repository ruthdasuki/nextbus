import requests

route = input("Enter your BUS ROUTE: ")
bus_stop_name = input("Enter your BUS STOP NAME: ")
direction = input("Enter your DIRECTION: ")


def get_routes(route):
    getRoutes = "https://svc.metrotransit.org/NexTrip/Routes?format=json"
    getRoutes_response = requests.get(getRoutes)

    if getRoutes_response.status_code == 200:
        for i in range(len(getRoutes_response.json())):
            if route == getRoutes_response.json()[i]["Description"]:
                route = int(getRoutes_response.json()[i]["Route"])
    return route

route = get_routes(route)


def get_direction(route, direction):
    global direction_value
    getDirections = f"https://svc.metrotransit.org/NexTrip/Directions/{route}?format=json"
    getDirections_response = requests.get(getDirections)

    if getDirections_response.status_code == 200:
        for i in range(len(getDirections_response.json())):
            if direction.upper() in getDirections_response.json()[i]["Text"]:
                direction_value = int(getDirections_response.json()[i]["Value"])
    return direction_value


direction_value = get_direction(route, direction)


def get_stops(route, direction_value, bus_stop_name):
    global stop_value
    getStops = f"https://svc.metrotransit.org/NexTrip/Stops/{route}/{direction_value}?format=json"
    getStops_response = requests.get(getStops)

    if getStops_response.status_code == 200:
        for i in range(len(getStops_response.json())):
            if bus_stop_name == getStops_response.json()[i]["Text"]:
                stop_value = getStops_response.json()[i]["Value"]
    return stop_value

stop_value = get_stops(route, direction_value, bus_stop_name)


def get_timepoint_departure(route, direction_value, stop_value):
    global nextBus
    getTimepointDepartures = f"https://svc.metrotransit.org/NexTrip/{route}/{direction_value}/{stop_value}?format=json"
    getTimepointDepartures_response = requests.get(getTimepointDepartures)

    if getTimepointDepartures_response.status_code == 200:
        for i in range(len(getTimepointDepartures_response.json())):
            if getTimepointDepartures_response.json()[i]["Actual"]:
                nextBus = getTimepointDepartures_response.json()[i]["DepartureText"]
            if not getTimepointDepartures_response.json()[i]["Actual"]:
                nextBus = getTimepointDepartures_response.json()[0]["DepartureText"]
        return nextBus


nextBus = get_timepoint_departure(route, direction_value, stop_value)
print(nextBus)

# “METRO Blue Line” “Target Field Station Platform 1” “south”
