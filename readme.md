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
