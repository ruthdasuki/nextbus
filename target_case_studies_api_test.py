import target_case_studies_api
from target_case_studies_api.target_case_studies_api import nextBus

route = "METRO Blue Line"
bus_stop_name = "Target Field Station Platform 1"
direction = "south"

def test_one():
    assert nextBus == "13:01"