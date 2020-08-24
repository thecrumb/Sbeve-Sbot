import discord
import config
from config import token

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if 'creeper' in message.content.lower():
        await message.channel.send('AW MAN')

client.run(token)
