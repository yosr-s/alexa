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

user_api="33baeb991596e85a52b4f9b2860dad30"
lat="34"
lon="9"

base_url="api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+user_api
weather_data=requests.get(base_url).json()
pprint(weather_data)

if 'rain' in weather_data:
    send()