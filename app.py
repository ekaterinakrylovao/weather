from flask import Flask, jsonify
import requests

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = "5151e161a3bb6ea866d7688c8fab79a9"  # <-- Put your OpenWeatherMap API key here!
OPENWEATHERMAP_API_URL = "https://api.openweathermap.org/data/2.5/"

def get_weather_data(endpoint, city):
    params = {'q': city, 'appid': OPENWEATHERMAP_API_KEY}
    response = requests.get(OPENWEATHERMAP_API_URL + endpoint, params=params)
    return response.json()

@app.route('/current_info/<cityname>')
def current_info(cityname):
    data = get_weather_data('weather', cityname)
    return jsonify(data)

@app.route('/current_weather/<cityname>')
def current_weather(cityname):
    data = get_weather_data('weather', cityname)['main']
    return jsonify({'weather': data})

@app.route('/weather_forecast/<cityname>')
def weather_forecast(cityname):
    data = get_weather_data('forecast', cityname)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
