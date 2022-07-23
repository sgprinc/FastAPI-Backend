from datetime import datetime
from typing import Union
from sqlalchemy.orm import Session
from databaseModels import *


class DataBroker:

    def get_station(self, db: Session, station_id: int):
        return db.query(Station).filter(Station.stationId == station_id).first()

    def get_stations(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Station).offset(skip).limit(limit).all()

    def get_stationMachines(self, db: Session, station_id: int):
        return db.query(Machine).where(Machine.stationId == station_id).all()

    def get_readings(self, db: Session, machine_id: int, start_date: Union[datetime, None], end_date:  Union[datetime, None]):
        return db.query(Reading).filter(Reading.machineId == machine_id).filter(Reading.timestamp.between(start_date, end_date)).all()

    def get_machine(self, db: Session, machine_id: int):
        return db.query(Machine).filter(Machine.machineId == machine_id).first()

    def get_machines(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Machine).offset(skip).limit(limit).all()
