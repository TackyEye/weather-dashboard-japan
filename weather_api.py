import requests
import json

def get_weather_forecast():
    """Fetch weather forecast data from Open-Meteo API"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 35.6897,
        "longitude": 139.6922,
        "hourly": "temperature_2m"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        
        data = response.json()
        print("Weather Forecast Data:")
        print(json.dumps(data, indent=2))
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    forecast_data = get_weather_forecast()
