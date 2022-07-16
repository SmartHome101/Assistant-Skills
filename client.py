import speech_recognition as sr
import requests
import re
import os
import json
import time
import Weather , News , IOT , Kitchen , Entertainment , Social , Productivity 
from TTS import speak
import pygame as pg


mapping={
        'Greeting'      : Social.Social,
        'Goodbye'       : Social.Social,
        'Thanks'        : Social.Social,
        'Joke'          : Entertainment.joke,
        'PlayMusic'     : Entertainment.play_music,
        'Cooking'       : Kitchen.cooking,
        'Weather'       : Weather.weather,
        'News'          : News.news,
        'Iot'           : IOT.smartHome,
        'Datetime'      : Productivity.productivity,
        'Reminder'      : Productivity.productivity
        } 

SR_URL = 'http://sr.techome.systems/predict'
TEMP_FILE = 'temp.wav'

def save_wave_file(audio):
    with open(TEMP_FILE, "wb") as f:
        f.write(audio.get_wav_data())

def recognize():
    with open(TEMP_FILE, 'rb') as file:
        files = {'file': file}
        print('will sent a request to sr')
        response = requests.post(SR_URL, files=files)

    return response.text.lower()

while True:
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try :
            recognizer.pause_threshold = .8
            print("Hey, How can I help you!")
            audio = recognizer.listen(source)
            save_wave_file(audio)
            print('Got the audio and will process')
            sentence = recognize()
            print(sentence)
            if 'leo' in sentence:
                message = re.match('(.*)leo(.*)',sentence).group(2)
                message = message.strip()
                print(f'will sent request "{message}" to nlb')
                response = requests.post(f'http://nlp.techome.systems/predict?message={message}').json()
                print(response)
                mapping[response['Intent']](response)
                    
            else:
                continue 
        except:
            continue
            
    os.remove(TEMP_FILE)   
    
