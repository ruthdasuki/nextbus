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

1. Clone the Python program on: https://github.com/ruthdasuki/nextbus
2. Go to the directory that the program is in.
3. Use command line to enter the following information: python3 nextbus.py [BUS ROUTE] [BUS STOP NAME] [DIRECTION]


Testing
-------

1. Install unittest

```
pip3 install unittest
```

2. In command line, enter the following command:

```
python3 nextbus_test.py
```


Versioning
-------
The program uses git for Versioning. For the versions available, see the git repository.


Scaling
-------
The program utilizes ratelimit to limit only ONE API call to Metro Transit public every THIRTY seconds. As the website specifically points out, "Third party applications should not update departure information more frequently than every 30 seconds. Applications making excessive calls and updating more frequently than 30 seconds will be subject to restriction."

When desire to use, uncomment the following code before each function:

```
# @limits(calls=1, period=THIRTY_SECONDS)
```

Test Cases
-------

### Valid Test Cases

The bus has arrived

```
python3 nextbus.py "Franklin Av - Riverside Av - U of M - 8th St SE" "Hennepin Ave and 22nd St" "east"
Due
```

Calculation for next bus

```
python3 nextbus.py "Franklin Av - Riverside Av - U of M - 8th St SE" "Hennepin Ave and 22nd St" "east"
3 Min
```

Next bus arrival time

```
python3 nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "south"
10:36
```


### Invalid Test Cases

Invalid number of arguments

```
python3 nextbus.py "METRO Blue ll" "Target Field Station Platform 1"
ERROR: Please enter the following command: python3 nextbus.py [BUS ROUTE] [BUS STOP NAME] [DIRECTION]
```

Invalid direction

```
python3 nextbus.py "Franklin Av - Riverside Av - U of M - 8th St SE" "Hennepin Ave and 22nd St" 2
ERROR: Please enter a valid DIRECTION as in ['north', 'east', 'west', 'south']
```

```
python3 nextbus.py 1 2 3
ERROR: Please enter a valid DIRECTION as in ['north', 'east', 'west', 'south']
```

Invalid bus route

```
python3 nextbus.py "METRO Blue ll" "Target Field Station Platform 1" "south"
ERROR: The route for METRO Blue ll cannot be found.
```

Invalid bus stop name

```
python3 nextbus.py "METRO Blue Line" "Target Field Station Platform 3" "south"
ERROR: The bus stop name Target Field Station Platform 3 for route METRO Blue Line cannot be found.
```

Invalid direction

```
python3 nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "east"
ERROR: The direction east for route METRO Blue Line cannot be found.
```

No available bus

```
python3 nextbus.py "Express - Target - Hwy 252 and 73rd Av P&R - Mpls" "Target North Campus Building F" "south"
The service is not available on route Express - Target - Hwy 252 and 73rd Av P&R - Mpls south on Target North Campus Building F
```
