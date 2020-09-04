import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'creeper' in message.content.lower():
            await message.channel.send('AW MAN')


def setup(bot):
    bot.add_cog(Fun(bot))
