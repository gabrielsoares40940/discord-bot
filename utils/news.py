# API de notícias
import random
from datetime import datetime
import requests

class NewsAPI:
    BASE_URL = 'https://newsapi.org/v2/'
    
    def __init__(self, api_key) -> None:
        """Recebe a api_key do Google News"""
        self.api_key = api_key

    def get_url_processed(self, url):
        """Usado para obter o retorno da URL acessada, porque a URL é redirecionada para a URL real. Esta função retorna a URL redirecionada"""
        return requests.get(url).url

    def build_params(self, *args, **kwargs):
        """Usado para transformar os parâmetros recebidos em query parâmetros da URL"""
        return '&'.join([f'{key}={value}' for key, value in kwargs.items()])

    def get(self, endpoint, **params):
        """Monta uma requisição do tipo 'get' para o endpoint requerido e passando os parâmetros escolhidos e retorna a resposta do endpoint"""
        _params = self.build_params(**params)
        return requests.get(f'{self.BASE_URL}{endpoint}?apiKey={self.api_key}&{_params}').json()

    def get_top_headlines(self):
        """Retorna as notícias em alta e retorna um dicionário com as informações necessárias para exibir no Discord"""
        result = self.get('top-headlines', sources='google-news-br')
        pos = random.randint(0, result['totalResults'] - 1)
        return {
            'site': result['articles'][pos]['author'],
            'title': result['articles'][pos]['title'],
            'publishedAt': datetime.strptime(result['articles'][pos]['publishedAt'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d/%m/%Y'),
            'url': self.get_url_processed(result['articles'][pos]['url'])
        }
