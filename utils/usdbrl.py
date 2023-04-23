# API de conversor de Dólar para Real
import requests

class UsdToBrlAPI:
    def get_dolar(self):
        request_dolar = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
        return request_dolar.json()['USDBRL']['bid']    