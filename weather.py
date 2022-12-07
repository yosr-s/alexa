import requests
from pprint import pprint
from twilio.rest import Client

def send():
    account_sid="AC0e5bcf4fafd8593d2cc24faa941a25dc"
    auth_token="0ec54481f204ccfb541f7bbe88b22c03"
    twilio_number="+19088276738"
    my_number="+21656899869"
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body="hey,its raining today!",
        from_=twilio_number,
        to=my_number)

user_api="7d34b41b3756881d9d48c0b124cb91a9"
location="tunisia,sousse"
base_url="http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api+"&units=metric"



weather_data=requests.get(base_url).json()
pprint(weather_data)

temp=weather_data['main']['temp']
wind_speed=weather_data['wind']['speed']
description=weather_data['weather'][0]['description']
print("temprature : {} degree celcius".format(temp))
print("wind speed : {} m/s".format(wind_speed))
print("description : {}".format(description))

if 'rain' in weather_data:
    send()