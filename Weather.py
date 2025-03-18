def Weather():
    while True:
        print("Welcome To The Python Weather App!")
        city = input("Please Enter your city: ").title()
        if city.lower() == 'exit':
            break
        displayWeather(city)

    print("Thank you for using the Weather App!")


def displayWeather(city):
    try:
        city = city.title()
        if city in weather_data:
            data = weather_data[city]
            print(f"Current Temperature in {city}: {data['temperature']}")
            print(f"Weather Condition: {data['conditions']}")
            print(f"Wind Speed: {data['wind_speed']}")
            print(f"Humidity: {data['humidity']}")
        else:
            print("No data found for this city")
    except Exception as e:
        print(f"please insert an actual city {e}")

weather_data = {"London": {"temperature": "15°C", "conditions": "Cloudy", 
"wind_speed": "5 km/h", "humidity": "80%"}, "New York": {"temperature": 
"20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": 
"50%"}, "Tokyo": {"temperature": "18°C", "conditions": "Rainy", 
"wind_speed": "7 km/h", "humidity": "90%"}, "Sydney": {"temperature": 
"22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": 
"60%"}, "Paris": {"temperature": "17°C", "conditions": "Foggy", 
"wind_speed": "3 km/h", "humidity": "85%"}}


Weather()