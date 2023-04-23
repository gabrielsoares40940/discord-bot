import discord
import os
import random
import asyncio
import requests
from dotenv import load_dotenv
from datetime import datetime

from utils.news import NewsAPI

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

owner = 'by BlazeOfDark#9607'

''' JOGO DA COBRINHA'''

game = {
    "high_score": 0,
    "current_score": 0,
    "games_played": 0,
    "game": False,
    "head": [1, 1],
    "length": 0,
    "direction": 6,
    "body": [],
    "grid": [
        [4, 4, 4, 4, 4, 4, 4, 4],
        [4, 3, 3, 3, 3, 3, 3, 4],
        [4, 3, 3, 3, 3, 3, 3, 4],
        [4, 3, 3, 3, 3, 3, 3, 4],
        [4, 3, 3, 3, 3, 3, 3, 4],
        [4, 3, 3, 3, 3, 3, 3, 4],
        [4, 3, 3, 3, 3, 3, 3, 4],
        [4, 4, 4, 4, 4, 4, 4, 4]
    ],# Just for reference
    "elements": {
        0: ":green_circle:", # Snake Head
        1: ":green_square: ", # Snake Body
        2: ":white_large_square:", # Background
        3: ":brown_square:", # Walls
        4: ":red_square:" # Food
    },
    "spawn_food": True,
    "food": []
}


class MyClient(discord.Client):

    NOT_PREFIX_ALLOWED = (
        'prefix',
        'teste',
        'Teste'
    )
    
    # def openFile(java):
    #     os.startfile('JMusicBot-0.3.9.jar')
        
    # API de conversor de Bitcoin para Real
    def get_bitcoin(self):
        request_bpi = requests.get('https://economia.awesomeapi.com.br/json/last/BTC-BRL')
        return request_bpi.json()['BTCBRL']['bid']

    # API de conversor de Dólar para Real
    def get_dolar(self):
        request_dolar = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
        return request_dolar.json()['USDBRL']['bid']    
    
    # API de clima
    def get_weather(self, cidade):
        request_temp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={os.getenv("API_KEY")}&lang=pt_br&units=metric')
        request_desc = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={os.getenv("API_KEY")}&lang=pt_br')
        return request_temp.json()['main']['temp'], request_desc.json()['weather'][0]['description']
    
    # API de horário
    def get_hour(self):
        request_hour = requests.get('https://timeapi.io/api/Time/current/zone?timeZone=America/Fortaleza')
        return request_hour.json()['time']
    
    # API de notícias
    # def get_news(self):
    #     request_news = requests.get(f'https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey={os.getenv("API_KEY_NEWS")}')
    #     site = request_news.json()['articles'][0]['source']['name']
    #     titulo = request_news.json()['articles'][0]['title']
    #     data_publicacao = request_news.json()['articles'][0]['publishedAt']
    #     url = request_news.json()['articles'][0]['url']
        
    #     lista = [titulo, data_publicacao, url, site]
    #     return lista

    
    async def on_ready(self):
        print('The bot {0}is working!'.format(self.user))

    async def on_message(self, message):
        if not message.content.startswith('?') and message.content not in self.NOT_PREFIX_ALLOWED:
            print('Mensagem de {0.author}: {0.content}'.format(message))
            return

        # Regras
        if message.content == '?regras': # Se o conteúdo da mensagem foi igual a "?regras", ele irá imprimir o nome do usuário e ditará as regras
            if message.guild.id in [610200027876556820]:
                embedVar = discord.Embed(title="Regras", color=0xBF9676)
                embedVar.set_author(name=message.guild.name, icon_url=message.guild.icon)
                embedVar.add_field(name="Regra única", value='Não usar **FDS** para "Fim de Semana"', inline=False)
                embedVar.set_footer(text=owner, icon_url='https://i.imgur.com/OurwHrV.png')
                await message.reply(embed=embedVar, mention_author=False)
            else:
                embedVar = discord.Embed(title="Regras", color=0x5263ED)
                embedVar.set_author(name=message.guild.name)
                embedVar.add_field(name="Regra nº 1", value='Não há regras', inline=False)
                embedVar.set_footer(text=owner, icon_url='https://i.imgur.com/OurwHrV.png')
                await message.reply(embed=embedVar, mention_author=False)

        elif message.content in ('teste', 'Teste'):
            await message.reply('Testando...', mention_author=False)
            await message.channel.send('https://media.tenor.com/LacNG2e3b3AAAAAd/spongebob-mr-crab.gif')

        # Saudações
        elif message.content == '?saudacoes': # Se o conteúdo da mensagem foi igual a "?saudacoes", ele irá imprimir o nome do usuário e perguntará se está tudo bem
            await message.reply(f'Olá **{message.author.name}**, tudo bom?', mention_author=False)

        # Tudo bom?
        elif message.content == '?tudo bom?': # Se o conteúdo da mensagem foi igual a "?tudo bom?", ele irá imprimir um emoji de polegar para cima
            await message.reply('👍', mention_author=False)

        # Rolar D20
        elif message.content in ('?rolard20', '?d20'): # Se o conteúdo da mensagem foi igual a "?rolard20", ele irá fazer algumas ações:
            if message.author.id in [267059555182182401]: # Se o usuário for o Ryan (seu ID), irá rolar um dado de forma aleatória do número 15 ao 20
                 dado = random.randint(15, 20)
            elif message.author.id in [355289415607910400]:# Se o usuário for o Biel (seu ID), irá rolar um dado de número único (1)
                 dado = 1
            else:
                dado = random.randint(1, 20) # Se for um usuário comum, ele irá rolar um dado de forma aleatória do número 1 ao 20
            await message.reply(f'🎲🔁🎲 → **{dado}**', mention_author=False)

        # Comandos
        elif message.content == '?commands':
            if message.guild.id in [610200027876556820]:
                embedVar = discord.Embed(title="Comandos", color=0xBF9676)
                embedVar.set_author(name=message.guild.name, icon_url=message.guild.icon)
                embedVar.add_field(name="`?regras`", value='Irei lhe mostrar as regras do servidor.', inline=False)
                embedVar.add_field(name="`?saudacoes`", value='Irei lhe dar saudações.', inline=False)
                embedVar.add_field(name="`?tudo bom?`", value='👍', inline=False)
                embedVar.add_field(name="`?rolard20`", value='Irei rolar um dado de 20 lados para você.', inline=False)
                embedVar.add_field(name="`?hello`", value='Irei oi para você.', inline=False)
                embedVar.add_field(name="`?ryan`", value='Irei postar uma foto bem vergonhosa de **Ryan**.', inline=False)
                embedVar.add_field(name="`?fuleco`", value='Irei postar uma foto de **Fuleco**. Representa um grande momento de sua vida.', inline=False)
                embedVar.add_field(name="`prefix`", value='Irei lhe mostrar o prefixo.', inline=False)
                embedVar.add_field(name="`?dolar`", value='Irei lhe informar o valor do dólar em tempo real.', inline=False)
                embedVar.add_field(name="`?bitcoin`", value='Irei lhe informar o valor do bitcoin em tempo real.', inline=False)
                embedVar.add_field(name="`?clima`", value='Irei lhe mostrar a temperatura e o tempo na cidade de sua escolha.', inline=False)
                embedVar.add_field(name="`?hora`", value='Irei lhe mostrar as horas.', inline=False)
                embedVar.add_field(name="`?snake`", value='Você irá jogar o famoso jogo da cobrinha.', inline=False)
                embedVar.set_footer(text=owner, icon_url='https://i.imgur.com/OurwHrV.png')
                await message.reply(embed=embedVar, mention_author=False)
            else:
                embedVar = discord.Embed(title="Comandos", color=0x5263ED)
                embedVar.set_author(name=message.guild.name, icon_url=message.guild.icon)
                embedVar.add_field(name="`?regras`", value='Irei lhe mostrar as regras do servidor.', inline=False)
                embedVar.add_field(name="`?saudacoes`", value='Irei lhe dar saudações.', inline=False)
                embedVar.add_field(name="`?tudo bom?`", value='👍', inline=False)
                embedVar.add_field(name="`?rolard20`", value='Irei rolar um dado de 20 lados para você.', inline=False)
                embedVar.add_field(name="`?hello`", value='Irei oi para você.', inline=False)
                embedVar.add_field(name="`prefix`", value='Irei lhe mostrar o prefixo.', inline=False)
                embedVar.add_field(name="`?dolar`", value='Irei lhe informar o valor do dólar em tempo real.', inline=False)
                embedVar.add_field(name="`?bitcoin`", value='Irei lhe informar o valor do bitcoin em tempo real.', inline=False)
                embedVar.add_field(name="`?tiringa`", value='Irei postar um gif do Tiringa.', inline=False)
                embedVar.add_field(name="`?clima`", value='Irei lhe mostrar a temperatura e o tempo na cidade de sua escolha.', inline=False)
                embedVar.add_field(name="`?hora`", value='Irei lhe mostrar as horas.', inline=False)
                embedVar.add_field(name="`?snake`", value='Você irá jogar o famoso jogo da cobrinha.', inline=False)
                embedVar.set_footer(text=owner, icon_url='https://i.imgur.com/OurwHrV.png')
                await message.reply(embed=embedVar, mention_author=False)

        # Hello
        elif message.content == '?hello': # 
            await message.reply(f'Olá, **{message.author.name}**!', mention_author=False)
        
        # Ryan
        elif message.content == '?ryan':
            if message.guild.id in [610200027876556820]:
                await message.reply('https://i.imgur.com/cu81SU9.png', mention_author=False)
                await message.channel.send(f'*"oi gays{os.linesep}sou viado{os.linesep}v 👍"{os.linesep}**- Ryan Pedro, 2021** *')
            else:
                return

        # Fuleco
        elif message.content == '?fuleco':
            if message.guild.id in [610200027876556820]:
                await message.reply('fuleco!!', mention_author=False)
                await message.channel.send('https://thumbs.gfycat.com/LawfulInsidiousFrigatebird-size_restricted.gif')
            else:
                return

        # Prefixo
        elif message.content == 'prefix':
            msg = await message.reply('Meu prefixo é: `?`', mention_author=False)
            await asyncio.sleep(5)
            await msg.delete()

        # Informa o valor do Dólar em Real

        elif message.content == '?dolar':
            price_dolar = self.get_dolar()
            await message.reply(f'O valor **atual** do Dólar é de `R$ {price_dolar}`.', mention_author=False)
      
        # Informa o valor do Bitcoin em Real
        elif message.content == '?bitcoin':
            price_bpi = self.get_bitcoin()
            await message.reply(f'O valor **atual** do Bitcoin é de `R$ {price_bpi}`.', mention_author=False)
            
        # Informa a hora para o usuário
        elif message.content == '?hora':
            current_hour = self.get_hour()
            await message.reply(f'⏰ `{current_hour}`', mention_author=False)
        
        # Tiringa
        elif message.content == '?tiringa':
            await message.reply('https://media.tenor.com/nkdIOj6q7SIAAAAd/tiringa-mad.gif', mention_author=False)

        # O bot irá mandar uma mensagem em sua DM
        elif message.content == '?dmme':
            await message.add_reaction('📬')
            user = await client.fetch_user(message.author.id)
            await user.send(f'Olá **{message.author.name}**, o que seria?')

        # O bot irá mostrar o clima
        elif message.content == '?clima':
            ctx = await message.reply(f' **{message.author.name}**, qual o nome da cidade?', mention_author=False)
            def nome_cidade(m):
                return m.author == message.author
            
            # Se a pessoa não respondê-lo dentro de 10 segundos, ele irá dizer "Você demorou demais."
            try:
                cidade = await self.wait_for('message', check=nome_cidade, timeout=5)
            except asyncio.TimeoutError:
                await asyncio.sleep(5)
                await message.add_reaction('❎')
                return await ctx.edit(content="Você demorou demais.")
            
            if cidade.content:
                temp, desc = self.get_weather(cidade.content)
                
                if desc == 'nublado':
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está `{desc}` ☁', mention_author=False)
                    
                elif desc == 'algumas nuvens':
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está com `{desc}` 🌥', mention_author=False)
                    
                elif desc == 'céu limpo':
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está com o `{desc}` ☀', mention_author=False)
                
                elif desc == 'nuvens dispersas':
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está com `{desc}` ☁ ☁', mention_author=False)
                    
                elif desc in ['chuva moderada', 'chuva leve', 'chuva']:
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está com `{desc}` 🌧', mention_author=False)
                    
                elif desc == 'pouca neve':
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está com `{desc}` 🌨', mention_author=False)
                    
                elif desc == 'tempestade':
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está com `{desc}` 🌩', mention_author=False)

                elif desc == 'névoa':
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está com `{desc}` 🌫', mention_author=False)
                        
                elif desc == 'neve':
                    await message.add_reaction('✅')
                    await message.reply(f'🌡 A temperatura é de `{temp} °C`{os.linesep}🔆 E o tempo está com `{desc}` ❄', mention_author=False)
            
        elif message.content == '?bitcoin':
            price_bpi = self.get_bitcoin()
            await message.reply(f'O valor **atual** do Bitcoin é de `R$ {price_bpi}`.', mention_author=False)   
            
        elif message.content == '?news':
            news_client = NewsAPI(api_key=os.getenv('API_KEY_NEWS'))
            top_headlines = news_client.get_top_headlines()
            await message.reply(f'Temos uma notícia do site 🌐 `{top_headlines["site"]}`!{os.linesep}**{top_headlines["title"]}**{os.linesep}**Data de publicação: **{top_headlines["publishedAt"]}{os.linesep}{top_headlines["url"]}', mention_author=False)
            
        # Teste do bot editando a própria mensagem
        elif message.content == "?teste":
            ctx = await message.reply("Processando.")
            await asyncio.sleep(1)
            
            await ctx.edit(content="Processando..")
            await asyncio.sleep(1)
            
            await ctx.edit(content="Processando...")
            await asyncio.sleep(1)
            
            await ctx.edit(content="Processando.")
            await asyncio.sleep(1)
            
            await ctx.edit(content="Processando..")
            await asyncio.sleep(1)
            
            await ctx.edit(content="Processando...")
            await asyncio.sleep(3)
            
            await ctx.edit(content="Teste completo!")

        # O bot entra na call em que o usuário estiver
        elif message.content == '?entrar':            
            voice_client = await message.author.voice.channel.connect()
            voice_client[voice_client.guild.id] = voice_client
        
        # Jogar o joguinho da cobrinha
        elif message.content == '?snake':
            if game['game']:
                return await message.channel.send('A game is already going on.')
            await message.channel.send(f'Starting a new game.{os.linesep}**Created by Purge-1.{os.linesep}GitHub: https://github.com/Purge-1**')
            await self.start_game(message)

    async def start_game(self, message):
        game['game'] = True
        game['games_played'] += 1
        await message.channel.send(f'This will be game number {game["games_played"]}')
        await self.update_grid(message)

    async def update_grid(self, message):
        if game['length'] > 0:
            game['body'].insert(0, game['head'].copy())
            game['body'].pop(-1)

        if game['direction'] == 2:
            game['head'][0] += 1
        elif game['direction'] == 4:
            game['head'][1] -= 1
        elif game['direction'] == 6:
            game['head'][1] += 1
        elif game['direction'] == 8:
            game['head'][0] -= 1

        if game['head'] == game['food'] and not game['spawn_food']:
            game['current_score'] += 1
            game['spawn_food'] = True
            game['length'] += 1
            body_add = game['head'].copy()
            if game['length'] > 1:
                body_add = game['body'][-1].copy()
            if game['direction'] == 2:
                body_add[0] -= 1
            elif game['direction'] == 4:
                body_add[1] += 1
            elif game['direction'] == 6:
                body_add[1] -= 1
            elif game['direction'] == 8:
                body_add[0] -= 1
            game['body'].insert(0, body_add)

        while game['spawn_food']:
            game['food'] = [random.randint(1, 6), random.randint(1, 6)]
            if game['food'] not in game['body'] and game['food'] != game['head']:
                game['spawn_food'] = False

        plot = await self.plot_grid()
        message = await message.channel.send(plot)
        clockwise = '\U0001F503'
        counter_clockwise = '\U0001F504'
        await message.add_reaction(counter_clockwise)
        await message.add_reaction(clockwise)

        await asyncio.sleep(2.5)
        message = await message.channel.fetch_message(message.id)
        clockwise_reactions = discord.utils.get(message.reactions, emoji='🔃')
        counter_clockwise_reactions = discord.utils.get(message.reactions, emoji='🔄')
        
        if clockwise_reactions and counter_clockwise_reactions:
            if clockwise_reactions.count > counter_clockwise_reactions.count:
                if game['direction'] == 2:
                    game['direction'] = 4
                elif game['direction'] == 4:
                    game['direction'] = 8
                elif game['direction'] == 6:
                    game['direction'] = 2
                elif game['direction'] == 8:
                    game['direction'] = 6
            elif clockwise_reactions.count < counter_clockwise_reactions.count:
                if game['direction'] == 2:
                    game['direction'] = 6
                elif game['direction'] == 4:
                    game['direction'] = 8
                elif game['direction'] == 6:
                    game['direction'] = 8
                elif game['direction'] == 8:
                    game['direction'] = 4

        if not (await self.game_over_check(message)):
            await self.update_grid(message)
        
    async def plot_grid(self):
        plot = ""
        for x in range(0, 8):
            for y in range(0, 8):
                if [x, y] == game['head']:
                    plot += game['elements'][0]
                elif [x, y] in game['body']:
                    plot += game['elements'][1]
                elif [x, y] == game['food']:
                    plot += game['elements'][4]
                elif x == 0 or y == 0 or x == 7 or y == 7:
                    plot += game['elements'][3]
                else:
                    plot += game['elements'][2]
            plot += '\n'
        return plot

    async def game_over_check(self, message):
        if game['head'][0] == 0 or game['head'][0] == 7 or game['head'][1] == 0 or game['head'][1] == 7:
            await message.channel.send(f'Game Over!\nCurrent Score: {game["current_score"]}\nHigh Score: {game["high_score"]}')
            if game["current_score"] > game["high_score"]:
                game["high_score"] = game["current_score"]
                await message.channel.send("New High Score!!")
            game['game'] = False
            game['head'] = [1, 1]
            game['length'] = 0
            game['direction'] = 6
            game['body'] = []
            game['spawn_food'] = True
            game['food'] = []
            return True
        if game['head'] in game['body']:
            await message.channel.send(f'Game Over!\nCurrent Score: {game["current_score"]}\nHigh Score: {game["high_score"]}')
            if game["current_score"] > game["high_score"]:
                game["high_score"] = game["current_score"]
                await message.channel.send("New High Score!!")
            game['game'] = False
            game['head'] = [1, 1]
            game['length'] = 0
            game['direction'] = 6
            game['body'] = []
            game['spawn_food'] = True
            game['food'] = []
            return True
        return False            
        
    # openFile(java=True)   
client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))


# os.system('start /min java -Dnogui=true -jar JMusicBot-0.3.9.jar')