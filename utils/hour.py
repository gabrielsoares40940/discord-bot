# API de horário
import requests

class HourAPI:
    def get_hour(self):
        request_hour = requests.get('https://timeapi.io/api/Time/current/zone?timeZone=America/Fortaleza')
        return request_hour.json()['time']