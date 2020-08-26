import discord
import config
import json
from discord.ext import commands
from config import token

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if 'creeper' in message.content.lower():
        await message.channel.send('AW MAN')
    await client.process_commands(message)

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) # FIXME use del or remove instead

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# @client.command()
# async def play(ctx):

@client.command()
async def lyrics(ctx):
    embed1 = discord.Embed(
        title = 'Revenge',
        description = 
        '''
        [Intro: TryHardNinja]
        Creeper
        Aw man

        [Verse 1: TryHardNinja]
        So we back in the mine
        Got our pickaxe swinging from side to side
        Side-side to side
        This task, a grueling one
        Hope to find some diamonds tonight, night, night
        Diamonds tonight

        [Pre-Chorus: TryHardNinja]
        Heads up
        You hear a sound, turn around and look up
        Total shock fills your body
        Oh, no, it's you again
        I can never forget those eyes, eyes, eyes
        Eyes-eye-eyes

        [Chorus: TryHardNinja]
        'Cause, baby, tonight
        The creeper's tryna steal all our stuff again
        'Cause, baby, tonight
        You grab your pick, shovel, and bolt again (Bolt again-gain)
        And run, run until it's done, done
        Until the sun comes up in the morn'
        'Cause, baby, tonight
        The creeper's tryna steal all our stuff again (Stuff again-gain)

        [Verse 2: TryHardNinja]
        Just when you think you're safe
        Overhear some hissing from right behind
        Right-right behind
        That's a nice life you have
        Shame it's gotta end at this time, time, time
        Time-time-time-time

        [Pre-Chorus: TryHardNinja]
        Blows up
        Then your health bar drops and you could use a one-up
        Get inside, don't be tardy
        So, now you're stuck in there
        Half a heart is left, but don't die, die, die
        Die-die-die

        [Chorus: TryHardNinja]
        'Cause, baby, tonight
        The creeper's tryna steal all our stuff again
        'Cause, baby, tonight
        You grab your pick, shovel, and bolt again (Bolt again-gain)
        And run, run until it's done, done
        Until the sun comes up in the morn'
        'Cause, baby, tonight
        The creeper's tryna steal all our stuff again        
        ''',
        colour = discord.Colour.blue()
    )
    embed2 = discord.Embed(
        description =
        '''
        [Verse 3: CaptainSparklez]
        (Creepers, you're mine, haha)
        Dig up diamonds and craft those diamonds
        And make some armor, get it, baby
        Go and forge that like you so MLG pro
        The sword's made of diamonds, so come at me, bro, huh
        Training in your room under the torchlight
        Hone that form to get you ready for the big fight
        Every single day and the whole night
        Creeper's out prowlin', hoo, alright
        Look at me, look at you
        Take my revenge, that's what I'm gonna do
        I'm a warrior, baby, what else is new?
        And my blade's gonna tear through you, bring it

        [Bridge: TryHardNinja & CaptainSparklez]
        'Cause, baby, tonight
        The creeper's tryna steal all our stuff again
        (Gather your stuff, yeah, let's take back the world)
        Yeah, baby, tonight (Haha)
        Grab your sword, armor and go (It's on)
        Take your revenge (Woo), oh-oh, oh-oh
        So fight, fight, like it's the last, last night
        Of your life, life, show them your bite (Woo)

        [Chorus: TryHardNinja & CaptainSparklez]
        'Cause, baby, tonight
        The creeper's tryna steal all our stuff again
        'Cause, baby, tonight
        You grab your pick, shovel and bolt again (Bolt again-gain, woo)
        And run, run until it's done, done
        Until the sun comes up in the morn'
        'Cause, baby, tonight (Come on, swing your sword up high)
        The creeper's tryna steal all our stuff again (Come on, jab your sword down low)
        (Woo)
        ''',
        colour = discord.Colour.blue()
    )

    embed1.set_thumbnail(url='https://i.ytimg.com/vi/cPJUBQd-PNM/hqdefault.jpg')
    embed1.set_author(name='CaptainSparklez', icon_url='https://vignette.wikia.nocookie.net/youtube/images/3/34/Cs.png/revision/latest?cb=20150203013604')

    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)

client.run(token)
