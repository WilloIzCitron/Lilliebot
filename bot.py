
import asyncio
import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json

client = discord.Client()

print('Please wait ok')


@client.event
async def on_ready():
    await asyncio.sleep(6)
    myAct = discord.Activity(
        name='With you', type=discord.ActivityType.playing)
    await client.change_presence(activity=myAct)
    print('Bot is online')
    print('Console has Launched')
    print('Lilliebot Console By WilloIzCitron')


@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith('l$hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))

    if message.content.startswith('l$whoareyou'):
        await message.channel.send('im liliebot i can help you')

    if message.content.startswith('l$lol'):
        await message.channel.send('hahaha its funny!')

    if message.content.startswith('l$dance'):
        await message.channel.send(random.choice(['lol i cant dance im bot', 'try this a song https://www.youtube.com/watch?v=A67ZkAd1wmI']))

    if message.content.startswith('l$biodata'):
        await message.channel.send("Name:Lilliebot Owner: Willo Code: Python")

    if message.content.startswith('l$lmao'):
        await message.channel.send('hahaha its funny!')

    if message.content.startswith('l$covid'):
        await message.channel.send('Dont touch me pls, {0.author.mention} is possitive coronavirus!'.format(message))

    if message.content.startswith('l$shoot {1.mention}'):
        await message.channel.send('Hahaha {0.mention} are dead'.format(message))

    if message.content.startswith('l$god'):
        await message.channel.send(random.choice(['i dont know about that the Lillie is G O D', 'by the way the laptop had G O D specs', 'we need a G O D Terraria', 'is here a G O D Mario', 'i catch a G O D Pokemon']))

    if message.content.startswith('l$pokemon'):
        await message.channel.send(random.choice(['Pikachu', 'Eevee', 'Charmander', 'Bulbasaur', 'Squirtle']))

    if msg.startswith(f'l$say'):
        await message.channel.send(msg[int(len(msg.split()[0]) + 1):])

    if message.content.startswith('l$invite'):
        await message.channel.send('Is here a Invite For add in your server. link=https://discordapp.com/api/oauth2/authorize?client_id=703427882726457403&permissions=8&scope=bot and support server invite =https://discord.gg/6AkeDD9')

    if message.content.startswith('l$randomnpc'):
        await message.channel.send(random.choice(['https://www.pngitem.com/pimgs/m/446-4468761_terraria-guide-npc-hd-png-download.png You Got Guide', 'https://66.media.tumblr.com/247cfd904f5fb23a6de54d3cb8a1b9b6/tumblr_phngb6yM2G1vhhmun_540.jpg You Got Dryad', 'https://vignette.wikia.nocookie.net/terraria/images/4/4d/NPC_19.png/revision/latest?cb=20200425230158 You Got Arms Dealer']))

    if msg.startswith('someball'):
        await message.channel.send('somegirl')

    if msg.startswith(f'l$ping'):
        await message.channel.send('**Pong!** Your latency is '+str(round(client.latency*100)) + 'ms')

    if msg.startswith(f'l$help'):
        embed = discord.Embed(
            title="Help", description="Is here a Help Pages", color=(random.choice([0x00ff00, 0x0ff0ff, 0xff01ff])))

        embed.add_field(name='l$hello',
                        value='The bot say hi', inline='True')
        embed.add_field(name='l$lol or l$lmao',
                        value='make bot stay happy', inline='True')
        embed.add_field(name='l$invite',
                        value='show invite bot and server', inline='True')
        embed.add_field(name='l$god',
                        value='god things ok', inline='True')
        embed.add_field(name='l$randomnpc',
                        value='randon Terraria NPC', inline='True')
        embed.add_field(name='l$shoot',
                        value='Shoot anyone', inline='True')
        embed.add_field(name='l$pokemon',
                        value='Trandom starter', inline='True')
        embed.add_field(name='l$biodata',
                        value='show biodata', inline='True')
        embed.add_field(name='l$whoareyou',
                        value='show a names', inline='True')
        embed.add_field(name='l$say',
                        value='say everything to bot', inline='True')
        embed.add_field(name='l$dance',
                        value='make bot dance', inline='True')
        embed.add_field(name='l$ping',
                        value='check bot latency', inline='True')
        embed.add_field(name='l$help',
                        value='you are here', inline='True')
    await message.channel.send(embed=embed)


async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)
        
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
