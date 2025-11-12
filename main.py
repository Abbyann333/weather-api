from fastapi import FastAPI, Query
import requests

app = FastAPI()

# Homepage
@app.get("/")
def home():
    return "Welcome to Abby’s Weather API! Go to /weather?city=CityName for weather."

# Weather route
@app.get("/weather")
def weather(city: str = Query("Canton")):
    try:
        geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1").json()
        if "results" not in geo or len(geo["results"]) == 0:
            return f"City '{city}' not found."
        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        weather_data = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true").json()
        current = weather_data.get("current_weather", {})
        temp = current.get("temperature")
        wind = current.get("windspeed")

        return f"It’s {temp}°C in {city.title()} with wind {wind} km/h."
    except:
        return "Something went wrong."
















