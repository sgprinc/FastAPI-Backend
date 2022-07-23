from settings import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from enum import Enum

engine = create_engine(DB_URL, connect_args=DB_ARGS)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


class DatabaseHandler():
    # Create and populate the tables
    def populate_database(self):
        Base.metadata.create_all(bind=engine)
        loader = DataLoader()
        stationsData = loader.loadJSON(
            STATIONS_DATA, dataToLoad=DataTypes.STATION)
        machinesData = loader.loadJSON(
            MACHINES_DATA, dataToLoad=DataTypes.MACHINE)
        readingsData = loader.loadCSV(READINGS_DATA)

        self.populate_table(STATIONS_TBL_NAME, stationsData)
        self.populate_table(MACHINES_TBL_NAME, machinesData)
        self.populate_table(READINGS_TBL_NAME, readingsData)

    # Populates a given table with data
    def populate_table(self, table, data):
        data.to_sql(table, engine, if_exists='replace')

    def recreate_database(self):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        self.populate_database()


class DataLoader():
    # Filesystem data loading methods
    def loadCSV(self, filepath):
        csvData = pd.read_csv(filepath,
                              sep=',',
                              decimal='.',
                              dtype={'Timestamp': str, 'MachineId': str, 'Reading': float})

        # Apply header and datatype corrections
        csvData.columns = ["Timestamp", "MachineId", "Reading"]
        csvData['Timestamp'] = pd.to_datetime(
            csvData.Timestamp, format='%Y-%m-%d')

        return csvData

    def loadJSON(self, filepath, dataToLoad=None):
        jsonData = pd.read_json(filepath)

        # Apply header overwrites depending on the data we are loading
        if dataToLoad == DataTypes.STATION:
            jsonData.columns = ['StationId', 'Location', 'Description']
        elif dataToLoad == DataTypes.MACHINE:
            jsonData.columns = ['MachineId',
                                'MachineName', 'StationId', 'Unit']

        return jsonData


# Enums for the datafile types
class DataTypes(Enum):
    STATION = 1
    MACHINE = 2
    READING = 3


if __name__ == "__main__":
    dbHandler = DatabaseHandler()
    dbHandler.recreate_database()
