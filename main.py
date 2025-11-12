from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/weather")
def get_weather(city: str = Query(..., description="City name")):
    # Simple example: this uses Open-Meteo (no API key needed)
    url = f"https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city, canton
        "temperature": data["current_weather"]["temperature"],
        "windspeed": data["current_weather"]["windspeed"],
        "time": data["current_weather"]["time"]
    }
from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome! Use /weather?city=CityName to get weather info."}

@app.get("/weather")
def get_weather(city: str = Query(..., description="City name")):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city,
        "temperature": data["current_weather"]["temperature"],
        "windspeed": data["current_weather"]["windspeed"],
        "time": data["current_weather"]["time"]
    }
from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Abby’s Free Weather API")

# Homepage
@app.get("/")
def home():
    return {
        "message": "Welcome to Abby’s Weather API! Use /weather?city=CityName to get weather info."
    }

# Weather endpoint
@app.get("/weather")
def get_weather(city: str = Query(..., description="City name")):
    # Simple example: Open-Meteo API
    url = f"https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city,
        "temperature": data["current_weather"]["temperature"],
        "windspeed": data["current_weather"]["windspeed"],
        "time": data["current_weather"]["time"]
    }
https://your-app-name.onrender.com/weather?city=Alliance
https://your-app-name.onrender.com/docs




