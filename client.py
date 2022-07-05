import speech_recognition as sr
import requests
import re
import os
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

URL = 'http://sr.techome.systems/predict'
TEMP_FILE = 'temp.wav'

def save_wave_file(audio):
    with open(TEMP_FILE, "wb") as f:
        f.write(audio.get_wav_data())

def recognize():
    with open(TEMP_FILE, 'rb') as file:
        files = {'file': file}
        response = requests.post(URL, files=files)

    return response.text.lower()

while True:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try :
            recognizer.pause_threshold = .8
            audio = recognizer.listen(source)
            sentence = recognize()
            print(sentence)
            if 'leo' in sentence:  
                message = re.match('(.*)leo(.*)',sentence).group(2)
                message = message.strip()
                response = requests.post(f'http://nlp.techome.systems/predict?message={message}').json()
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
        
    os.remove(TEMP_FILE)   
    
