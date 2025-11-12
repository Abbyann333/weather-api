from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Abby’s Friendly Weather API")

# Homepage route
@app.get("/")
def home():
    return "Welcome to Abby’s Weather API! Use /weather?city=CityName to get weather info."

# Weather route
@app.get("/weather")
def get_weather(city: str = Query("Canton", description="City name, defaults to Canton")):
    try:
        # Get city coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_data = requests.get(geo_url).json()

        if "results" not in geo_data or len(geo_data["results"]) == 0:
            return f"City '{city}' not found."

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Get weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_data = requests.get(weather_url).json()
        current = weather_data.get("current_weather", {})

        return f"It’s {current.get('temperature')}°C in {city.title()} with wind {current.get('windspeed')} km/h."
    except:
        return "Something went wrong. Try again."













