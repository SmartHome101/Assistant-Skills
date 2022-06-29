import requests
from TTS import speak

api_key = "661d81f3b17f7764fba64a3b2e0118db"

def weather(result):
    # Check if the user has provided a city name or not
    city_name = '' 
    
    if 'location' in result['Entities']:
        city_name += result['Entities']['location']
    else:
        city_name = 'cairo'
    
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,api_key)
    response = requests.get(url)

    # get information from the response object and convert it to json format to be able to access the data
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        # get the temperature in kelvin and convert it to celsius and weather description    
        min_temp = round(y["temp_min"] - 273.15,2)
        max_temp = round(y["temp_max"] - 273.15,2)
        weather_describe = z[0]["description"]
        
        if 'weather_descriptor' in result['Entities']:
            description = result['Entities']['weather_descriptor']
            if description == weather_describe :
                speak("Yes, weather is {}".format(weather_describe))
            else :
                speak("No, weather is {}".format(weather_describe))
        else :
            res = "The weather forecast in {} is {} with a minimum of {} Celsius and a maximum of {} Celsius".format(city_name,weather_describe,min_temp,max_temp)
            speak(res)
        
    else:
        speak("There are error")