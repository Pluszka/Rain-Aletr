import requests
from private_data import *

MY_LAT = 50.0915234
MY_LON = 18.2199165
parameters = {
    'lat': -14.235004,
    'lon': -51.925282,
    'exclude': 'current,minutely,daily,alerts',
    'appid': my_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

rain = False
next_hours = data['hourly'][:12]

if [True for hour in next_hours if hour['weather'][0]['id'] < 700]:
    print('Bring an umbrella')
