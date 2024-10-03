from datetime import datetime
import open_weather_map_api as owm_api
import weather_details as details


def main():
    location = details.set_location()
    units = details.set_units()
    weather_data, error = owm_api.get_current_weather(location, units)
    if error:
        print('Sorry could not get weather.')
    else:
        list_of_forecasts = details.weather_list(weather_data)
        forecasts(list_of_forecasts)


def forecasts(forecast_data):
    # should show the timestamp, temp and unit, weather description, and wind speed for every three hour interval
    for day in forecast_data:
        timestamp = details.get_timestamp(day)
        forecast_date = datetime.fromtimestamp(timestamp)
        temp = details.get_temp(day)
        weather_description = details.get_description(day)
        wind_speed = details.get_speed(day)
        print(f'{forecast_date} - {temp}F\n'
              f'Weather: {weather_description} with wind speeds of {wind_speed} mph.\n')


if __name__ == '__main__':
    main()