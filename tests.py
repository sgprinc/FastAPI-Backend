from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_all_stations():
    response = client.get("/stations/")
    assert response.status_code == 200, f"Query to '/stations' returned code {response.status_code}"
    assert response.json() != {}, f"Response from querying '/stations' was empty"

def test_station_by_id():
    validStationId = 1
    response = client.get(f"/station/{validStationId}")
    assert response.status_code == 200, f"Query to '/station/stationId' with a supposed valid value returned code {response.status_code}"
    assert response.json() != {}, f"Response from querying '/station/stationId' was empty"

    invalidStationId = -1
    response = client.get(f"/station/{invalidStationId}")
    assert response.status_code == 404, f"Query to '/station/stationId' with a supposed invalid value returned code {response.status_code}"    

def test_measurements_unbounded():
    machineId = 427712
    response = client.get(f"/measurements/", params={"machine_id": machineId})
    assert response.status_code == 200, f"Query to '/measurements/' returned code {response.status_code}"
    assert response.json() != {}, f"Response from querying '/measurements/' was empty"


def test_measurements_bounded():
    machineId = 427038
    start_date = "2021-11-07 23:56:00"
    end_date = "2021-11-07 23:59:59"
    response = client.get(f"/measurements/", params={"machine_id": machineId, "start_date": start_date, "end_date":end_date})
    assert response.status_code == 200, f"Query to '/measurements/' returned code {response.status_code}"
    assert response.json() != {}, f"Response from querying '/measurements/' was empty"    
    assert len(response.json()) == 3, f"Response from querying '/measurements/' for a known id and timerange returned an unexpected amount of data"    


def test_all_machines():
    response = client.get("/machines/")
    assert response.status_code == 200, f"Query to '/machines' returned code {response.status_code}"
    assert response.json() != {}, f"Response from querying '/machines' was empty"

def test_machine_by_id():
    validMachineId = 427038
    response = client.get(f"/machine/{validMachineId}")
    assert response.status_code == 200, f"Query to '/machine/machineId' with a supposed valid value returned code {response.status_code}"
    assert response.json() != {}, f"Response from querying '/machine/machineId' was empty"

    invalidMachineId = -999999
    response = client.get(f"/machine/{invalidMachineId}")
    assert response.status_code == 404, f"Query to '/machine/machineId' with a supposed invalid value returned code {response.status_code}"    


if __name__ == "__main__":
    # Run some tests on the station endpoints
    test_all_stations()
    test_station_by_id()    
    
    # Run some tests on the measurements endpoints
    test_measurements_unbounded()
    test_measurements_bounded()
    
    # Run some tests on the machine endpoints
    test_all_machines()
    test_machine_by_id()

    # If all tests pass, we should be able to print (rudimentary, but works)
    print("All good in the hood!")