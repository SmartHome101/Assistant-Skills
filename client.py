import speech_recognition as sr
import requests
import json
import time
import Weather , News , IOT , Kitchen , Enterainment , Social , Productivity 
from TTS import speak

mapping={
        'Greeting'      : Social.Social,
        'Goodbye'       : Social.Social,
        'Thanks'        : Social.Social,
        'Joke'          : Enterainment.joke,
        'PlayMusic'     : Enterainment.play_music,
        'Cooking'       : Kitchen.cooking,
        'Weather'       : Weather.weather,
        'News'          : News.news,
        'Iot'           : IOT.smartHome,
        'Datetime'      : Productivity.productivity,
        'Reminder'      : Productivity.productivity
        } 

while True:

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)

    # recognize speech using Google Speech Recognition
        message = recognizer.recognize_google(audio)
        print(message)

    response = requests.post(f'http://127.0.0.1:8000/predict?message={message}').json()
    #make a request to the server and get the response in json format then mapping the response to the function
    speak(str(mapping[response['Intent']](response)))
    time.sleep(5)

    if response['Intent'] in ["Goodbye" , "Thanks"]:
                break

    time.sleep(10)