from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'b07db316c823917567b216280f7a6dea'

def get_weather(city_name):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    city_name = ""

    if request.method == "POST":
        city_name = request.form["city"]
        weather_data = get_weather(city_name)

    return render_template("index.html", weather=weather_data, city=city_name)

if __name__ == "__main__":
    app.run(debug=True)
