# Backend stage
FROM python:3.9
WORKDIR /usr/src/backend
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Initialize & populate the SQLite DB
CMD [ "python", "./database.py"]
# Run the FastAPI app
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]