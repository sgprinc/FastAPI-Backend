from sqlalchemy import Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from settings import *


class Station(Base):
    __tablename__ = STATIONS_TBL_NAME

    stationId = Column(Integer, primary_key=True, index=True)
    location = Column(String, unique=False, index=True)
    description = Column(String, unique=False, index=True)

    machines = relationship("Machine", back_populates="origin")


class Reading(Base):
    __tablename__ = READINGS_TBL_NAME

    index = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, unique=False, index=False)
    machineId = Column(String, ForeignKey("Machines.machineId"))
    reading = Column(Float, unique=False, index=False)

    machine = relationship("Machine", back_populates="readings")


class Machine(Base):
    __tablename__ = MACHINES_TBL_NAME

    machineId = Column(Integer, primary_key=True, index=True)
    machineName = Column(String, unique=False, index=True)
    stationId = Column(Integer, ForeignKey("Stations.stationId"))
    unit = Column(String, unique=False, index=False)

    origin = relationship("Station", back_populates="machines")
    readings = relationship("Reading", back_populates="machine")
