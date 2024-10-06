# details specific to open weather map's data structure

def set_location():
    # Minneapolis
    lat = 44.97
    lon = -93.26

    location = [lat, lon]
    return location


def set_units():
    # temperature - standard for Kelvin, metric for Celsius, imperial for Fahrenheit
    # wind speed - standard or metric for meter per second, imperial for miles per hour
    measurement = 'imperial'
    return measurement


def weather_list(data):
    try:
        forecast_list = data['list']
        return forecast_list
    except KeyError:
        print(unexpected_format())
        return 'Unknown'


def get_timestamp(data):
    try:
        timestamp = data['dt']
        return timestamp
    except KeyError:
        print(unexpected_format())
        return 'Unknown'


def get_temp(data):
    try:
        temp = data['main']['temp']
        return temp
    except KeyError:
        print(unexpected_format())
        return 'Unknown'


def get_description(data):
    try:
        description = data['weather'][0]['description']
        return description
    except KeyError:
        print(unexpected_format())
        return 'Unknown'


def get_speed(data):
    try:
        speed = data['wind']['speed']
        return speed
    except KeyError:
        print(unexpected_format())
        return 'Unknown'


def unexpected_format():
    return 'This data is not in the expected format'
