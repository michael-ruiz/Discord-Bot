import discord
import os
import random
from discord.ext import commands
from list import fun_facts
from corona import corona
from img_search import search

client = commands.Bot(command_prefix='!')
client.remove_command('help')
    
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

@client.command()
async def help(ctx):
    help = discord.Embed(title='Help', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ', description="Below is a list of all of this bot's commands", color=0x4287f5)
    help.set_thumbnail(url='https://www.oxigeno.fm/wp-content/uploads/2015/10/Ayudame-470X310-436x291.jpg')
    help.add_field(name='funfact', value='Displays a random fun fact' , inline=False)    
    help.add_field(name='wow', value='Wow', inline=False)
    help.add_field(name='ping', value="Shows the bot's ping", inline=False)
    help.add_field(name='covid', value="Displays today's covid numbers in Canada, Ontario and London", inline=False)
    help.add_field(name='picsearch', value='Search for a photo on Google. Type your search word after the command', inline=False)
    help.add_field(name='help', value='Shows this message', inline=False)
    help.set_footer(text='Thanks for listening to my TEDTalk')
    await ctx.send(embed = help)

client.run(os.getenv('TOKEN'))