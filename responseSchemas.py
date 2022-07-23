from datetime import datetime
from pydantic import BaseModel
from typing import Union

class Station(BaseModel):
    stationId: int
    location: str
    description: Union[str, None] = None
    
    class Config:
        orm_mode = True

class Reading(BaseModel):
    timestamp: datetime
    machineId: int    
    reading: float

    class Config:
        orm_mode = True

class Machine(BaseModel):
    machineId: str
    machineName: str
    stationId: str    
    unit: str

    class Config:
        orm_mode = True