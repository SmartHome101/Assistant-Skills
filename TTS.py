from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pygame as pg
import os


# Authentication
url = "https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/75b750d8-7b6b-4640-a00a-eda97dd26afe"
apikey = "WsmWrStJU1Y2zBgs3LFn-YIjG73RdvHDVtQCwELTsHa5"

#setup service
authenticator = IAMAuthenticator(apikey)
#new TTS service
tts = TextToSpeechV1(authenticator=authenticator)
#set service URL
tts.set_service_url(url)

num = 0
def speak(output):
    global num
    # num to rename every audio file with different name to remove ambiguity
    num += 1
    
    file = str(num)+'.mp3'
    with open(file, 'wb') as audio_file:
        res = tts.synthesize(output, accept='audio/mp3', voice='en-US_MichaelV3Voice').get_result()
        audio_file.write(res.content)    
        
    # for playing note.mp3 file
    pg.mixer.init()
    sound = pg.mixer.Sound(file)
    sound.play()
    os.remove(file)          
   
