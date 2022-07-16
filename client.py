import speech_recognition as sr
import requests
import re
import os
import json
import pygame
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
<<<<<<< Updated upstream
        print('will sent a request to sr')
=======
>>>>>>> Stashed changes
        response = requests.post(SR_URL, files=files)

    return response.text.lower()

pygame.init()
sound = pygame.mixer.Sound('indicator.mp3')
sound.play()
while True:
   # sound.play()
    recognizer = sr.Recognizer()
<<<<<<< Updated upstream
    
=======
     
>>>>>>> Stashed changes
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try :
           # print('Say Something!')
            recognizer.pause_threshold = .8
            print("Hey, How can I help you!")
            audio = recognizer.listen(source)
            save_wave_file(audio)
<<<<<<< Updated upstream
            print('Got the audio and will process')
            sentence = recognize()
            print(sentence)
            if 'leo' in sentence:
                message = re.match('(.*)leo(.*)',sentence).group(2)
=======
            sentence = recognize()
            print(sentence)
            if 'alex' in sentence:
                message = re.match('(.*)alex(.*)',sentence).group(2)
>>>>>>> Stashed changes
                message = message.strip()
                print(f'will sent request "{message}" to nlb')
                response = requests.post(f'http://nlp.techome.systems/predict?message={message}').json()
                print(response)
                mapping[response['Intent']](response)
                    
            else:
                continue 
        except:
            continue
<<<<<<< Updated upstream
            
    os.remove(TEMP_FILE)   
    
=======
    os.remove(TEMP_FILE)   
>>>>>>> Stashed changes
