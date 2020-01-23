import nextbus
import unittest


class TestNextBus(unittest.TestCase):
    # Assign global variables
    global route, route_value, direction, direction_value, bus_stop_name, stop_value

    # Variables for successful results
    route = "METRO Blue Line"
    route_value = 902
    direction = "east"
    direction_value = 2
    bus_stop_name = "Target Field Station Platform 1"
    stop_value = "TF12"

    def test_get_routes_1(self):
        assert nextbus.get_routes(route) == 901

    def test_get_routes_2(self):

        # Invalid bus route
        route = "METRO Blue Ll"

        with self.assertRaises(SystemExit) as cm:
            nextbus.get_routes(route)

        the_exception = cm.exception
        self.assertEqual(the_exception.code, None)

    def test_get_direction_1(self):
        assert nextbus.get_direction(route, route_value, direction) == 2

    def test_get_direction_2(self):

        # Invalid direction on certain bus route
        direction = "south"

        with self.assertRaises(SystemExit) as cm:
            nextbus.get_direction(route, route_value, direction)

        the_exception = cm.exception
        self.assertEqual(the_exception.code, None)

    def test_get_stops_1(self):
        assert nextbus.get_stops(route, route_value, direction_value, bus_stop_name) == "TF12"

    def test_get_stops_2(self):

        # Invalid bus stop name
        bus_stop_name = "Target Field Station Platform 3"

        with self.assertRaises(SystemExit) as cm:
            nextbus.get_stops(route, route_value, direction_value, bus_stop_name)

        the_exception = cm.exception
        self.assertEqual(the_exception.code, None)

    def test_get_timepoint_departure_1(self):
        assert nextbus.get_timepoint_departure(route, route_value, direction, direction_value, bus_stop_name,
                                               stop_value)

    def test_get_timepoint_departure_2(self):

        # Variables for not available service
        route = "METRO Green Line Bus"
        route_value = 992
        bus_stop_name = "Ramp B/5th St Transit Center"
        stop_value = "5GAR"
        direction = "east"
        direction_value = 2

        with self.assertRaises(SystemExit) as cm:
            nextbus.get_timepoint_departure(route, route_value, direction, direction_value, bus_stop_name, stop_value)

        the_exception = cm.exception
        self.assertEqual(the_exception.code, None)


if __name__ == '__main__':
    unittest.main()
