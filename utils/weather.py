# API de clima
import requests
import os    
    
class WeatherAPI:    
    def get_weather(self, cidade):
        request_temp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={os.getenv("API_KEY_WEATHER")}&lang=pt_br&units=metric')
        request_desc = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={os.getenv("API_KEY_WEATHER")}&lang=pt_br')
        return request_temp.json()['main']['temp'], request_desc.json()['weather'][0]['description']