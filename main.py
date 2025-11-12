from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Abby’s Free Weather API")

# Homepage route
@app.get("/")
def home():https://your-app-name.onrender.com/
    return {
        "message": "Welcome to Abby’s Weather API! Use /weather?city=CityName to get weather info."
    }

# Weather route
@app.get("/weather")
def get_weather(city: str = Query(None, description="City name")):
    if not city:https://your-app-name.onrender.com/weather?city=Canton
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








