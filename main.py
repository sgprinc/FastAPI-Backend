# FastAPI imports
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Type and set imports
from datetime import datetime
from typing import Union

# Database imports
from sqlalchemy.orm import Session
from database import SessionLocal

# Object model imports
import responseSchemas as schemas
from dataBroker import DataBroker

# Initialize the FastAPI app and the data broker instance
app = FastAPI()
dataBroker = DataBroker()

# Allow CORS since we are running the frontent from a different port
origins = ["http://localhost",
           "http://localhost:3000", "http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependance function for a database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints

# Query all stations in the database


@app.get("/stations/", response_model=list[schemas.Station])
def get_stations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_stations = dataBroker.get_stations(db=db, skip=skip, limit=limit)
    return db_stations

# Query an station by station Id


@app.get("/station/{station_id}", response_model=schemas.Station)
def get_station(station_id: int, db: Session = Depends(get_db)):
    db_station = dataBroker.get_station(db=db, station_id=station_id)
    if db_station is None:
        raise HTTPException(
            status_code=404, detail="Station data with the given station Id could not be found.")
    return db_station

# Query all machines from a given station


@app.get("/stationmachines/{station_id}", response_model=list[schemas.Machine])
def get_stationmachines(station_id: int, db: Session = Depends(get_db)):
    db_stationMachines = dataBroker.get_stationMachines(
        db=db, station_id=station_id)
    if db_stationMachines is None:
        raise HTTPException(
            status_code=404, detail="Station not found or no machines for such station")
    return db_stationMachines

# Query all readings from a given machine, and bounded by a timerange


@app.get("/readings/", response_model=list[schemas.Reading])
def get_readings(machine_id: int,
                 start_date: Union[datetime, None] = datetime.min,
                 end_date: Union[datetime, None] = datetime.max,
                 db: Session = Depends(get_db)):
    db_readings = dataBroker.get_readings(db, machine_id, start_date, end_date)
    if db_readings is None:
        raise HTTPException(
            status_code=404, detail="No readings found under the given machine Id.")
    return db_readings

# Query all machines


@app.get("/machines/", response_model=list[schemas.Machine])
def get_machines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_machines = dataBroker.get_machines(db, skip=skip, limit=limit)
    return db_machines

# Query a machine by machine Id


@app.get("/machine/{machine_id}", response_model=schemas.Machine)
def get_machines(machine_id: int, db: Session = Depends(get_db)):
    db_machine = dataBroker.get_machine(db, machine_id)
    if db_machine is None:
        raise HTTPException(
            status_code=404, detail="Machine data with the given Id could not be found.")
    return db_machine
