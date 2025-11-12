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
from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Abby’s Free Weather API")

# Homepage route
@app.get("/")
def home():
    return {
        "message": "Welcome to Abby’s Weather API! Use /weather?city=CityName to get weather info."
    }

# Weather route
@app.get("/weather")
def get_weather(city: str = Query(None, description="City name")):
    if not city:
        return {"error": "Please provide a city using ?city=CityName"}

    # Geocoding API to get latitude/longitude for the city
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    if "results" not in geo_data or len(geo_data["results"]) == 0:
        return {"error": f"City '{city}' not found."}

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    # Weather API using Open-Meteo
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    current = weather_data.get("current_weather", {})

    return {
        "city": city.title(),
        "latitude": lat,
        "longitude": lon,
        "temperature": current.get("temperature"),
        "windspeed": current.get("windspeed"),
        "time": current.get("time"),
    }





