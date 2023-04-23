# API de conversor de Euro para Real
import requests 

class EurToBrlAPI:
    def get_euro(self):
        request_bpi = requests.get('https://economia.awesomeapi.com.br/json/last/EUR-BRL')
        return request_bpi.json()['EURBRL']['bid']