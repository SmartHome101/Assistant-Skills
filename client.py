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
    # obtain audio from the microphone
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try :
            # recognize speech 
            recognizer.pause_threshold = .8
            audio = recognizer.listen(source)
            message = recognizer.recognize_google(audio)
            print(message)
            # wake up the assistant
            if 'leon' in message.lower():  
                speak("Hi, How can I help you?")
                recognizer = sr.Recognizer()
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    try:
                        recognizer.pause_threshold = .8
                        audio = recognizer.listen(source)
                        message = recognizer.recognize_google(audio)
                        print(message)
                        #send a request to the server
                        response = requests.post(f'http://nlp.techome.systems/predict?message={message}').json()
                        if response['Intent'] in ['Cooking','News']:
                            speak(str(mapping[response['Intent']](response)))
                            time.sleep(10)
                        else:
                            speak(str(mapping[response['Intent']](response)))
                            time.sleep(3)
                    except:
                        pass
            else:
                continue 
        except:
            continue
    
