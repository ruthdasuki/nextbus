Metro Transit NextBus Program
==============================


What Is The Program?
-------------

This is a simple Python 3.7 application that provides the time of arrival based on user input on Bus Route, Bus Stop Name, and Direction. The program utilizes Metro Transit's public API: https://svc.metrotransit.org/nextrip and make various requests to get the information from the API.

Prerequisites
---------------

The program utilizes the following Python modules that require the user to install before running the program:
1. requests

```
pip3 install requests
```

2. sys

```
pip3 install sys
```

3. ratelimit: https://pypi.org/project/ratelimit/

```
pip3 install ratelimit
```


How To Use The Program?
---------------

1. Clone the Python program on: https://github.com/ruthdasuki/target_case_studies_api
2. Go to the directory that the program is on.
3. Use command line to enter the following information: python3 target_case_studies_api.py [BUS ROUTE] [BUS STOP NAME] [DIRECTION]


Testing
-------

1. Install pytest

```
pip3 install pytest
```

2. Navigate to file target_case_studies_api_test.py
3. In order for the pytest to run, in target_case_studies_api.py, comment out the following code:

```
route = str(sys.argv[1])
bus_stop_name = str(sys.argv[2])
direction = str(sys.argv[3])
```
4. If you want to run the test in PyCharm, set the Configuration to pytest and run the tests.


Versioning
-------
I used git for Versioning. For the versions available, see the git repository.


Test Cases
-------

## Valid Test Cases

### Valid arguments to return calculation for next bus
python3 nextbus.py "Franklin Av - Riverside Av - U of M - 8th St SE" "Hennepin Ave and 22nd St" "east"
Result: 3 Min

### Valid arguments to return next bus arrival time
python3 nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "south"
Result: 10:36

### Partial bus route name
python3 nextbus.py "Franklin" "Hennepin Ave and 22nd St" "east"
Result: 8 Min


## Invalid Test Cases

### Invalid number of arguments
python3 nextbus.py "METRO Blue ll" "Target Field Station Platform 1"
Result: Please enter the following command: python3 nextbus.py [BUS ROUTE] [BUS STOP NAME] [DIRECTION]

### Invalid bus route
python3 nextbus.py "METRO Blue ll" "Target Field Station Platform 1" "south"
Result: Error: the route for METRO Blue ll cannot be found.

### Invalid bus stop name
python3 nextbus.py "METRO Blue Line" "Target Field Station Platform 3" "south"
Result: Error: the bus stop name Target Field Station Platform 3 for route METRO Blue Line cannot be found.

python3 nextbus.py 1 2 3
Result: Error: the direction 3 for route 1 cannot be found.

### Invalid direction
python3 nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "east"
Result: Error: the direction east for route METRO Blue Line cannot be found.


### No available bus
python3 nextbus.py "Express - Target - Hwy 252 and 73rd Av P&R - Mpls" "Target North Campus Building F" "south"
Result: The service is not available on route Express - Target - Hwy 252 and 73rd Av P&R - Mpls south on Target North Campus Building F