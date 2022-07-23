$entrypoint = "main:app"

# Clear previous statements from the shell
clear

# Activate the virtual environment with the required packages
.\.venv\Scripts\Activate.ps1

# [Optional] Launch browser and open interactive docs
Start-Process "http://127.0.0.1:8000/docs"

# Launch the FastAPI server
echo "> Launching FastAPI Server <"
uvicorn $entrypoint --reload
