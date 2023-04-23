import random
from datetime import datetime

import requests


class NewsAPI:
    BASE_URL = 'https://newsapi.org/v2/'
    
    def __init__(self, api_key) -> None:
        """recebe a api_key do google news"""
        self.api_key = api_key

    def get_url_processed(self, url):
        """usado para obter o retorno da url acessada, porque a url é redirecionada para a url real. esta funcao retorna a url redirecionada"""
        return requests.get(url).url

    def build_params(self, *args, **kwargs):
        """usado para transformar os parametros recebidos em query params da url"""
        return '&'.join([f'{key}={value}' for key, value in kwargs.items()])

    def get(self, endpoint, **params):
        """monta uma requisicao get para o endpoint requerido e passando os parametros escolhidos e retorna a resposta do endpoint"""
        _params = self.build_params(**params)
        return requests.get(f'{self.BASE_URL}{endpoint}?apiKey={self.api_key}&{_params}').json()

    def get_top_headlines(self):
        """retorna as noticias em alta e retorna um dict com as informacoes necessarias para exibir no discord"""
        result = self.get('top-headlines', sources='google-news-br')
        pos = random.randint(0, result['totalResults'] - 1)
        return {
            'site': result['articles'][pos]['author'],
            'title': result['articles'][pos]['title'],
            'publishedAt': datetime.strptime(result['articles'][pos]['publishedAt'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d/%m/%Y'),
            'url': self.get_url_processed(result['articles'][pos]['url'])
        }
