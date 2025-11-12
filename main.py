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
        "city": city,
        "temperature": data["current_weather"]["temperature"],
        "windspeed": data["current_weather"]["windspeed"],
        "time": data["current_weather"]["time"]
    }
