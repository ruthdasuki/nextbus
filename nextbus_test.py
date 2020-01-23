from nextbus import get_routes, get_direction, get_stops, get_timepoint_departure


def test_get_routes():
    route = "METRO Green Line"
    assert get_routes(route) == 902


def test_get_direction():
    route_value = 902
    direction = "east"
    assert get_direction(route_value, direction) == 2


def test_get_stops():
    route_value = 902
    direction_value = 2
    bus_stop_name = "Target Field Station Platform 1"
    assert get_stops(route_value, direction_value, bus_stop_name) == "TF12"


def test_get_timepoint_departure():
    route_value = 902
    direction_value = 2
    stop_value = "TF12"
    assert get_timepoint_departure(route_value, direction_value, stop_value)
