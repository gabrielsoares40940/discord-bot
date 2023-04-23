# API de conversor de Bitcoin para Real
import requests 

class BtcToBrlAPI:
    def get_bitcoin(self):
        request_bpi = requests.get('https://economia.awesomeapi.com.br/json/last/BTC-BRL')
        return request_bpi.json()['BTCBRL']['bid']