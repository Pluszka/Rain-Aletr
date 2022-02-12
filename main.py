import requests
from private_data import *
from twilio.rest import Client

MY_LAT = 50.0915234
MY_LON = 18.2199165
parameters = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'exclude': 'current,minutely,daily,alerts',
    'appid': my_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

rain = False
next_hours = data['hourly'][:12]

if [True for hour in next_hours if hour['weather'][0]['id'] < 700]:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Hey, it's going to rain. Don\'t forget your umbrella ☂️",
            from_='+18126339019',
            to=my_phone
        )
    print(message.status)