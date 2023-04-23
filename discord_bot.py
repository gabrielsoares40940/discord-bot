import discord
import os
import random
import asyncio
from dotenv import load_dotenv

from utils.news import NewsAPI
from utils.btcbrl import BtcToBrlAPI
from utils.usdbrl import UsdToBrlAPI
from utils.eurbrl import EurToBrlAPI
from utils.weather import WeatherAPI
from utils.hour import HourAPI

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

owner = MY-DISCORD-USER-ID

class MyClient(discord.Client):

    NOT_PREFIX_ALLOWED = (
        'prefix',
        'PREFIX',
        'teste',
        'Teste',
        'TESTE'
    )
    
    async def on_ready(self):
        print('The bot {0} is working!'.format(self.user))

    async def on_message(self, message):
        if not message.content.startswith('?') and message.content not in self.NOT_PREFIX_ALLOWED:
            print('Mensagem de {0.author}: {0.content}'.format(message))
            return

        # Regras
        if message.content.lower() in ('?regras', '?rules'): # Se o conteúdo da mensagem foi igual a "?regras", ele irá imprimir o nome do usuário e ditará as regras
            if message.guild.id in [DISCORD-GUILD-ID]:
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

        elif message.content.lower() in ('teste', 'Teste'): # Se o conteúdo da mensagem for igual a "teste" ou "Teste", ele irá imprimir um texto e gif de testes.
            await message.reply('Testando...', mention_author=False)
            await message.channel.send('https://media.tenor.com/LacNG2e3b3AAAAAd/spongebob-mr-crab.gif')

        # Tudo bom?
        elif message.content.lower() == '?tudo bom?': # Se o conteúdo da mensagem foi igual a "?tudo bom?", ele irá imprimir um emoji de polegar para cima
            await message.reply('👍', mention_author=False)

        # Rolar D20
        elif message.content.lower() in ('?rolard20', '?d20'): # Se o conteúdo da mensagem foi igual a "?rolard20", ele irá fazer algumas ações:
            if message.author.id in [DISCORD-USER-ID]: # Se o usuário for o utiliário do ID, irá rolar um dado de forma aleatória do número 15 ao 20
                 dado = random.randint(15, 20)
            elif message.author.id in [DISCORD-USER-ID]:# Se o usuário for o utiliário do ID, irá rolar um dado de número único (1)
                 dado = 1
            else:
                dado = random.randint(1, 20) # Se for um usuário comum, ele irá rolar um dado de forma aleatória do número 1 ao 20
            await message.reply(f'🎲🔁🎲 → **{dado}**', mention_author=False)

        # Comandos
        elif message.content.lower() == '?help':
            if message.guild.id in [DISCORD-GUILD-ID]:
                embedVar = discord.Embed(title="Comandos", color=0xBF9676)
                embedVar.set_author(name=message.guild.name, icon_url=message.guild.icon)
                embedVar.add_field(name="`?regras / ?rules`", value='Irei lhe mostrar as regras do servidor.', inline=False)
                embedVar.add_field(name="`?tudo bom?`", value='👍', inline=False)
                embedVar.add_field(name="`?rolard20 / ?d20`", value='Irei rolar um dado de 20 lados para você.', inline=False)
                embedVar.add_field(name="`?hello`", value='Irei oi para você.', inline=False)
                embedVar.add_field(name="`prefix`", value='Irei lhe mostrar o prefixo.', inline=False)
                embedVar.add_field(name="`?dolar`", value='Irei lhe informar o valor do dólar em tempo real.', inline=False)
                embedVar.add_field(name="`?bitcoin`", value='Irei lhe informar o valor do bitcoin em tempo real.', inline=False)
                embedVar.add_field(name="`?euro`", value='Irei lhe informar o valor do euro em tempo real.', inline=False)
                embedVar.add_field(name="`?clima / ?weather`", value='Irei lhe mostrar a temperatura e o tempo de uma cidade de sua escolha.', inline=False)
                embedVar.add_field(name="`?hora / ?hour`", value='Irei lhe mostrar as horas.', inline=False)
                embedVar.add_field(name="`?news`", value='Irei lhe mostrar as últimas notícias.', inline=False)
                embedVar.set_footer(text=owner, icon_url='https://i.imgur.com/OurwHrV.png')
                await message.reply(embed=embedVar, mention_author=False)
            else:
                embedVar = discord.Embed(title="Comandos", color=0x5263ED)
                embedVar.set_author(name=message.guild.name, icon_url=message.guild.icon)
                embedVar.add_field(name="`?regras / ?rules`", value='Irei lhe mostrar as regras do servidor.', inline=False)
                embedVar.add_field(name="`?tudo bom?`", value='👍', inline=False)
                embedVar.add_field(name="`?rolard20 / ?d20`", value='Irei rolar um dado de 20 lados para você.', inline=False)
                embedVar.add_field(name="`?hello`", value='Irei oi para você.', inline=False)
                embedVar.add_field(name="`prefix`", value='Irei lhe mostrar o prefixo.', inline=False)
                embedVar.add_field(name="`?dolar`", value='Irei lhe informar o valor do dólar em tempo real.', inline=False)
                embedVar.add_field(name="`?bitcoin`", value='Irei lhe informar o valor do bitcoin em tempo real.', inline=False)
                embedVar.add_field(name="`?euro`", value='Irei lhe informar o valor do euro em tempo real.', inline=False)
                embedVar.add_field(name="`?tiringa`", value='Irei postar um gif do Tiringa.', inline=False)
                embedVar.add_field(name="`?clima / ?weather`", value='Irei lhe mostrar a temperatura e o tempo de uma cidade de sua escolha.', inline=False)
                embedVar.add_field(name="`?hora / ?hour`", value='Irei lhe mostrar as horas.', inline=False)
                embedVar.add_field(name="`?news`", value='Irei lhe mostrar as últimas notícias.', inline=False)
                embedVar.set_footer(text=owner, icon_url='https://i.imgur.com/OurwHrV.png')
                await message.reply(embed=embedVar, mention_author=False)

        # Hello
        elif message.content.lower() == '?hello': # 
            await message.reply(f'Olá, **{message.author.name}**!', mention_author=False)

        # Prefixo
        elif message.content.lower() == 'prefix':
            msg = await message.reply('Meu prefixo é: `?`', mention_author=False)
            await asyncio.sleep(5)
            await msg.delete()

        # Informa o valor do Dólar em Real com atualização recorrente de 30 segundos
        elif message.content.lower() == '?dolar':
            price_dolar = UsdToBrlAPI()
            await message.reply(f'💸 O valor **atual** do Dólar é de `R$ {price_dolar.get_dolar()}`.', mention_author=False)
      
        # Informa o valor do Bitcoin em Real com atualização recorrente de 30 segundos
        elif message.content.lower() == '?bitcoin':
            price_bpi = BtcToBrlAPI()
            await message.reply(f'💸 O valor **atual** do Bitcoin é de `R$ {price_bpi.get_bitcoin()}`.', mention_author=False)  
            
        # Informa o valor do Euro em Real com atualização recorrente de 30 segundos
        elif message.content.lower() == '?euro':
            price_euro = EurToBrlAPI()
            await message.reply(f'💸 O valor **atual** do Euro é de `R$ {price_euro.get_euro()}`.', mention_author=False)  
            
        # Informa notícias
        elif message.content.lower() == '?news':
            news_client = NewsAPI(api_key=os.getenv('API_KEY_NEWS'))
            top_headlines = news_client.get_top_headlines()
            await message.reply(f'Temos uma notícia do site 🌐 `{top_headlines["site"]}`!{os.linesep}**{top_headlines["title"]}**{os.linesep}**Data de publicação: **{top_headlines["publishedAt"]}{os.linesep}{top_headlines["url"]}', mention_author=False)

        # Informa a hora para o usuário
        elif message.content.lower() in ('?hora', '?hour'):
            current_hour = HourAPI()
            await message.reply(f'⏰ `{current_hour.get_hour()}`', mention_author=False)
        
        # Tiringa
        elif message.content.lower() == '?tiringa':
            await message.reply('https://media.tenor.com/nkdIOj6q7SIAAAAd/tiringa-mad.gif', mention_author=False)

        # O bot irá mandar uma mensagem em sua DM
        elif message.content.lower() == '?dmme':
            await message.add_reaction('📬')
            user = await client.fetch_user(message.author.id)
            await user.send(f'Olá **{message.author.name}**, o que seria?')

        # O bot irá mostrar o clima
        elif message.content.lower() in ('?clima', '?weather'):
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
                api_weather = WeatherAPI()
                temp, desc = api_weather.get_weather(cidade.content)
                      
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
                        
        # Teste do bot editando a própria mensagem
        elif message.content.lower() == "?teste":
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
        elif message.content.lower() == '?entrar':            
            voice_client = await message.author.voice.channel.connect()
            voice_client[voice_client.guild.id] = voice_client
        
client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))
