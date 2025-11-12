from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Abby’s Friendly Weather API")

# Homepage
@app.get("/")
def home():
    return {
        "message": "Welcome to Abby’s Weather API! Use /weather?city=CityName to get weather info."
    }

# Weather route with friendly output
@app.get("/weather")
def get_weather(city: str = Query("Canton", description="City name, defaults to Canton, Ohio")):
    try:
        # Step 1: Geocode the city to get latitude and longitude
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if "results" not in geo_data or len(geo_data["results"]) == 0:
            return {"message": f"City '{city}' not found."}

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Step 2: Get current weather for the city
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        current = weather_data.get("current_weather", {})

        # Step 3: Return friendly message
        return {
            "message": f"It’s {current.get('temperature')}°C in {city.title()} "
                       f"with wind {current.get('windspeed')} km/h at {current.get('time')}."
        }

    except Exception as e:
        # Catch any unexpected errors
        return {"message": "Sorry, something went wrong. Please try again."}












