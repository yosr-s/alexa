import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from datetime import date
import pyjokes
import wikipedia
import requests

 
 
listener=sr.Recognizer()
engine=pyttsx3.init()
rate=engine.getProperty("rate")
engine.setProperty("rate",150)
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        print('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        talk('current time is'+time)
        print(time)
    elif 'joke' in command:
        ch=pyjokes.get_joke()
        print(ch)
        talk(ch+"      hahahahahahahahhahaha")
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        talk(info)
    elif 'weather' in command:
        user_api = "7d34b41b3756881d9d48c0b124cb91a9"
        location = "tunisia,sousse"
        base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api + "&units=metric"
        weather_data = requests.get(base_url).json()
        temp = weather_data['main']['temp']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        print("temprature : {} degree celcius".format(temp))
        print("wind speed : {} m/s".format(wind_speed))
        print("description : {}".format(description))
        day=date.today()
        print(str(day))
        talk("today's date is" + str(day))
        talk("temprature : {} degree celcius".format(temp))
        talk("wind speed : {} meters per second".format(wind_speed))
        talk("description : {}".format(description))
        if temp<15:
            talk("so,take your jacket with you.")
        elif temp>15:
            talk("enjoy your day its cool outside")
        elif 'rain' in weather_data:
            talk("don't forget your umbrella it might rain")
    elif 'thank' in command:
        talk("you're welcome")

while True:
    run_alexa()
