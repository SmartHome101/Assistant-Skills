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
        speak("Hi, I am Lemma personal assistant. How can I help you?")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            message = recognizer.recognize_google(audio)
            print(message)
            # make a request to the server and get the response in json format then mapping the response to the function
            response = requests.post(f'http://nlp.techome.systems/predict?message={message}').json()
            if response['Intent'] in ['Cooking','News']:
                speak(str(mapping[response['Intent']](response)))
                time.sleep(10)
            else:
                speak(str(mapping[response['Intent']](response)))
                time.sleep(3)
        except:
            print("sorry, could not recognise try again")
            # try "continue"
    if response['Intent'] in ["Goodbye" , "Thanks"]:
                break
