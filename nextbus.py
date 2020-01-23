import requests
import sys
from ratelimit import limits

# Configure global vairables
THREE_MINUTES = 180


# API call for all routes
# @limits(calls=1, period=THREE_MINUTES)
def get_routes(route):
    getRoutes = "https://svc.metrotransit.org/NexTrip/Routes?format=json"
    getRoutes_response = requests.get(getRoutes)

    if getRoutes_response.status_code == 200:
        for i in range(len(getRoutes_response.json())):
            if route in getRoutes_response.json()[i]["Description"]:
                route_value = int(getRoutes_response.json()[i]["Route"])
                break
        else:
            print(f"ERROR: The route for {route} cannot be found.")
            exit()
    else:
        print(f"ERROR: {getRoutes_response.status_code}")

    return route_value


# API call for direction
# @limits(calls=1, period=THREE_MINUTES)
def get_direction(route, route_value, direction):
    getDirections = f"https://svc.metrotransit.org/NexTrip/Directions/{route_value}?format=json"
    getDirections_response = requests.get(getDirections)

    if getDirections_response.status_code == 200:
        for i in range(len(getDirections_response.json())):
            if direction.upper() in getDirections_response.json()[i]["Text"]:
                direction_value = int(getDirections_response.json()[i]["Value"])
                break
        else:
            print(f"ERROR: The direction {direction} for route {route} cannot be found.")
            exit()
    else:
        print(f"ERROR: {getDirections_response.status_code}")
    return direction_value


# API call for bus stop
# @limits(calls=1, period=THREE_MINUTES)
def get_stops(route, route_value, direction_value, bus_stop_name):
    getStops = f"https://svc.metrotransit.org/NexTrip/Stops/{route_value}/{direction_value}?format=json"
    getStops_response = requests.get(getStops)

    if getStops_response.status_code == 200:
        for i in range(len(getStops_response.json())):
            if bus_stop_name == getStops_response.json()[i]["Text"]:
                stop_value = getStops_response.json()[i]["Value"]
                break
        else:
            print(f"ERROR: The bus stop name {bus_stop_name} for route {route} cannot be found.")
            exit()
    else:
        print(f"ERROR: {getStops_response.status_code}")
    return stop_value


# API call for next bus
# @limits(calls=1, period=THREE_MINUTES)
def get_timepoint_departure(route, route_value, direction, direction_value, bus_stop_name, stop_value):
    getTimepointDepartures = f"https://svc.metrotransit.org/NexTrip/{route_value}/{direction_value}/{stop_value}?format=json"
    getTimepointDepartures_response = requests.get(getTimepointDepartures)

    if getTimepointDepartures_response.status_code == 200:
        if len(getTimepointDepartures_response.json()) == 0:
            print(f"ERROR: The service is not available on route {route} {direction} on {bus_stop_name}")
            exit()
        else:
            for i in range(len(getTimepointDepartures_response.json())):
                if getTimepointDepartures_response.json()[i]["Actual"]:
                    nextBus = getTimepointDepartures_response.json()[i]["DepartureText"]
                if not getTimepointDepartures_response.json()[i]["Actual"]:
                    nextBus = getTimepointDepartures_response.json()[0]["DepartureText"]
    else:
        print(f"Error: {getTimepointDepartures_response.status_code}")
    return nextBus


def main():
    # Check number of arguments
    if len(sys.argv) != 4:
        print("ERROR: Please enter the following command: python3 nextbus.py [BUS ROUTE] [BUS STOP NAME] [DIRECTION]")
        exit()
    else:
        # Assign arguments to variables
        route = str(sys.argv[1])
        bus_stop_name = str(sys.argv[2])
        direction = str(sys.argv[3])

        valid_direction = ["north", "east", "west", "south"]

        if direction not in valid_direction:
            print(f"ERROR: Please enter a valid DIRECTION as in {valid_direction}")
            exit()
        else:
            # Call all the functions
            route_value = get_routes(route)
            direction_value = get_direction(route, route_value, direction)
            stop_value = get_stops(route, route_value, direction_value, bus_stop_name)
            nextBus = get_timepoint_departure(route, route_value, direction, direction_value, bus_stop_name, stop_value)

            # End result
            print(nextBus)


if __name__ == "__main__":
    main()