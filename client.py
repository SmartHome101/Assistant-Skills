import speech_recognition as sr
import requests
import re
import os
import json
import pygame
import time
import Weather , News , IOT , Kitchen , Entertainment , Social , Productivity 
from TTS import speak


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

pygame.init()
sound = pygame.mixer.Sound('indicator.mp3')

while True:
    sound.play()
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try :
           # print('Say Something!')
            recognizer.pause_threshold = .8
            audio = recognizer.listen(source)
            save_wave_file(audio)
            sentence = recognize()
            print(sentence)
            if 'alex' in sentence:
                message = re.match('(.*)alex(.*)',sentence).group(2)
                message = message.strip()
                response = requests.post(f'http://nlp.techome.systems/predict?message={message}').json()
                print(response)
                mapping[response['Intent']](response)
                    
            else:
                continue 
        except:
            continue
            
    os.remove(TEMP_FILE)   
