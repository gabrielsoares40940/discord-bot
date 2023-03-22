import discord
import os
import random
import asyncio
import requests
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

owner = 'by BlazeOfDark#9607'

class MyClient(discord.Client):
    NOT_PREFIX_ALLOWED = (
        'prefix',
        'teste'
    )

    def get_bitcoin(self):
        request_bpi = requests.get('https://economia.awesomeapi.com.br/json/last/BTC-BRL')
        return request_bpi.json()['BTCBRL']['bid']

    def get_dolar(self):
        request_dolar = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
        return request_dolar.json()['USDBRL']['bid']

    async def on_ready(self):
        print('The bot {0}is working!'.format(self.user))

    async def on_message(self, message):
        if not message.content.startswith('?') and message.content not in self.NOT_PREFIX_ALLOWED:
            print('Mensagem de {0.author}: {0.content}'.format(message))
            return

        # Regras
        if message.content == '?regras': # Se o conteúdo da mensagem foi igual a "?regras", ele irá imprimir o nome do usuário e ditará as regras
            if message.guild.id in [SERVER-DISCORD-ID]:
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

        elif message.content == 'teste':
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
            if message.author.id in [USER-DISCORD-ID]: # Se o usuário for o Ryan (seu ID), irá rolar um dado de forma aleatória do número 15 ao 20
                 dado = random.randint(15, 20)
            elif message.author.id in [USER-DISCORD-ID]:# Se o usuário for o Biel (seu ID), irá rolar um dado de número único (1)
                 dado = 1
            else:
                dado = random.randint(1, 20) # Se for um usuário comum, ele irá rolar um dado de forma aleatória do número 1 ao 20
            await message.reply(f'🎲🔁🎲 → **{dado}**', mention_author=False)

        # Comandos
        elif message.content == '?commands':
            if message.guild.id in [SERVER-DISCORD-ID]:
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
                embedVar.add_field(name="`?ti   ringa`", value='Irei postar um gif do Tiringa.', inline=False)
                embedVar.set_footer(text=owner, icon_url='https://i.imgur.com/OurwHrV.png')
                await message.reply(embed=embedVar, mention_author=False)

        # Hello
        elif message.content == '?hello': # 
            await message.reply(f'Olá, **{message.author.name}**!', mention_author=False)
        
        # Ryan
        elif message.content == '?ryan':
            if message.guild.id in [SERVER-DISCORD-ID]:
                await message.reply('https://i.imgur.com/cu81SU9.png', mention_author=False)
                await message.channel.send(f'*"oi gays{os.linesep}sou viado{os.linesep}v 👍"{os.linesep}**- Ryan Pedro, 2021** *')
            else:
                return

        # Fuleco
        elif message.content == '?fuleco':
            if message.guild.id in [SERVER-DISCORD-ID]:
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
        
        # Tiringa
        elif message.content == '?tiringa':
            await message.reply('https://media.tenor.com/nkdIOj6q7SIAAAAd/tiringa-mad.gif', mention_author=False)

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))