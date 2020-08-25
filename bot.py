import discord
import config
from discord.ext import commands
from config import token

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if 'creeper' in message.content.lower():
        await message.channel.send('AW MAN')
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

client.run(token)
