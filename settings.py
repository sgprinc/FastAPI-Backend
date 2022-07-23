import pathlib

# Commonly accessed directories
ROOT_DIR = pathlib.Path(__file__).parent
DATA_DIRECTORY = ROOT_DIR.joinpath("data")

# Datafiles mapping
__STATIONS_DATAFILE = "Stations.json"
__READINGS_DATAFILE = "Readings.csv"
__MACHINES_DATAFILE = "Machines.json"

# Data loading functions
STATIONS_DATA = DATA_DIRECTORY / __STATIONS_DATAFILE
READINGS_DATA = DATA_DIRECTORY / __READINGS_DATAFILE
MACHINES_DATA = DATA_DIRECTORY / __MACHINES_DATAFILE

# Database connection
DB_NAME = "DB.db"
DB_DIR = ROOT_DIR / DB_NAME
DB_URL = f"sqlite:///{DB_DIR.as_posix()}"
DB_ARGS = {"check_same_thread": False}

# Tables' name mappings
STATIONS_TBL_NAME = "Stations"
READINGS_TBL_NAME = "Readings"
MACHINES_TBL_NAME = "Machines"
