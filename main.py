import discord
import os

bot = discord.Client()
action_symbol = '*'

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith(action_symbol + 'hello'):
        await message.channel.send('Hello!')

bot.run(os.getenv('TOKEN'))