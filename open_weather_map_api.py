import os
import requests


url = f'https://api.openweathermap.org/data/2.5/forecast?'
api_key = os.environ['WEATHER_KEY'] # Set this environment variable on your computer


def get_current_weather(location, units):
    try:
        query = {'q': location, 'units': units, 'appid': api_key}
        response = requests.get(url, params=query)
        response.raise_for_status()
        weather_forecast = response.json()
        return weather_forecast, None
    except Exception as e:
        print(e)
        print(response.text)
        return None, e

