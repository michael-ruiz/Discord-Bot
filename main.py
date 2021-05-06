import discord
import os
import random
from discord.ext import commands
from list import fun_facts
from corona import corona
from img_search import search

client = commands.Bot(command_prefix='!')
    
@client.event
async def on_ready():
    print('Bot ready')

@client.command(aliases=['ff', 'didyouknow', 'dyk'])
async def funfact(ctx):
    fact = random.randint(0, len(fun_facts)-1)
    await ctx.send('Did you know:\n' + fun_facts[fact])

@client.command()
async def wow(ctx):
    await ctx.send('https://tenor.com/view/owen-wilson-owen-wilson-amazing-wonderful-gif-6103373')

@client.command()
async def ping(ctx):
    await ctx.send('My ping is ' + str(round(client.latency * 1000)) + 'ms')

@client.command(aliases=['corona', 'COVID'])
async def covid(ctx):
    await ctx.send('```' + corona() + '```')

@client.command(aliases=['ps'])
async def picsearch(ctx, arg):
    search(arg)
    await ctx.send('Here is the first image that comes up:', file=discord.File('SEARCH_IMG.png'))

client.run(os.getenv('TOKEN'))