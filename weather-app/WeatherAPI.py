from flask import Flask, render_template, request
import requests

def get_weather_by_city(api_key, city_name):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit, 'metric' for Celsius
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: Status Code {response.status_code}")
        return None

# Usage example
api_key = 'b07db316c823917567b216280f7a6dea'  
city_name = 'birmingham'
weather_data = get_weather_by_city(api_key, city_name)

if weather_data:
    print(f"Current Temperature in {city_name}: {weather_data['main']['temp']} °C")
    print(f"Weather Conditions: {weather_data['weather'][0]['description']}")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    print(f"Humidity: {weather_data['main']['humidity']}%")
else:
    print("Failed to retrieve weather data.")

