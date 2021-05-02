import discord
import os
import random

bot = discord.Client()
action_symbol = '*'

def funFact():
    fact = random.randint(0 , 1)
    if fact == 0:
        return 'AHHHHH!'
    elif fact == 1:
        return ':flushed:'

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(action_symbol + 'hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith(action_symbol + 'wow'):
        await message.channel.send('https://tenor.com/view/owen-wilson-owen-wilson-amazing-wonderful-gif-6103373')

    if message.content.startswith(action_symbol + 'funFact'):
        await message.channel.send(funFact())

bot.run(os.getenv('TOKEN'))