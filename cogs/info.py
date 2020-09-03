import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title = 'About Sbeve',
            description = 'Sbeve! Use $help to see all the Commands'
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        """Sends the invite link for this bot"""
        embed = discord.Embed(
            title = 'Invite Link',
            url = 'https://www.google.com/',
            description = 'Add Sbeve to another server!',
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Help',
            description = 'Send a message containing "creeper" and Sbeve will respond!',
            color = discord.Color.red()
        )
        embed.add_field(
            name = 'ℹ️ Info',
            value =
'''
`about`: Gives details about the bot
`invite`: Sends the invite link for this bot
`help`: Returns this menu
`ping`: Checks the bot's response time to Discord
''',
            inline = False
        )
        embed.add_field(
            name = '🎵 Music',
            value =
'''
`join`: Joins a voice channel
`play` or `p`: Joins a voice channel and plays a song given a search result or url (e.g. YouTube)
`pause`: Pauses the current song
`resume`: Resumes the current song
`stop`: Stops playing music
`leave`: Disconnects the bot from voice
`lyrics`: Shows the lyrics to Revenge by CaptainSparklez
''',
            inline = False
        )
        embed.add_field(
            name = '⚙️ Config',
            value =
'''
`changeprefix`: Sets a custom command prefix for this server
''',
            inline = False
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """Checks the bot's response time to Discord"""
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Info(bot))
