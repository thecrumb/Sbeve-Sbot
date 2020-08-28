import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title = 'About Sbeve',
            description = 'Sbeve! Use .help to see all the Commands'
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = 'Invite Link',
            description = 'Add Sbeve to another server!',
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
