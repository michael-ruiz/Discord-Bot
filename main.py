import discord
from discord.ext import commands
from list import fun_facts
import os
import random

client = commands.Bot(command_prefix='!')
    
@client.event
async def on_ready():
    print('Bot ready')

@client.command()
async def funfact(ctx):
    fact = random.randint(0, len(fun_facts)-1)
    await ctx.send('Did you know:\n' + fun_facts[fact])

@client.command()
async def wow(ctx):
    await ctx.send('https://tenor.com/view/owen-wilson-owen-wilson-amazing-wonderful-gif-6103373')

@client.command()
async def ping(ctx):
    await ctx.send('My ping is ' + str(round(client.latency * 1000)) + 'ms')   

client.run(os.getenv('TOKEN'))