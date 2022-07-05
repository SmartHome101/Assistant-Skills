import speech_recognition as sr
import requests
import re
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
        recognizer.adjust_for_ambient_noise(source)
        try :
            recognizer.pause_threshold = .8
            audio = recognizer.listen(source)
            sentence = recognizer.recognize_google(audio)
            sentence = sentence.lower()
            print(sentence)
            if 'leo' in sentence:  
                message = re.match('(.*)leo(.*)',sentence).group(2)
                message = message.strip()
                response = requests.post(f'http://nlp.techome.systems/predict?message={message}').json()
                print(response)
                if response['Intent'] in ['Cooking','News']:
                        speak(str(mapping[response['Intent']](response)))
                        time.sleep(10)
                else:
                    speak(str(mapping[response['Intent']](response)))
                    time.sleep(3)
                    
            else:
                continue 
        except:
            continue
    
