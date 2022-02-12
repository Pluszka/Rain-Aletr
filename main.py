import requests
from private_data import *

parameters = {
    'lat': 50.0915234,
    'lon': 18.2199165,
    'exclude': 'current,minutely,daily,alerts',
    'appid': my_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

next_hours = data['hourly'][:12]

weather = next_hours[0]['weather'][0]['id']

print(weather)