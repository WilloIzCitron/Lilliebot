import asyncio
import discord
import random
from discord.ext.commands import Bot
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content.lower()
    embed = discord.Embed()
    if message.author == client.user:
        return

    if message.content.startswith('l$hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))

    if message.content.startswith('l$whoareyou'):
        await message.channel.send('im liliebot i can help you')

    if message.content.startswith('l$lol'):
        await message.channel.send('hahaha its funny!')

    if message.content.startswith('l$ping'):
        await message.channel.send('**Pong!**\n'+str(round(client.latency*1000))+' ms.')

    if message.content.startswith('l$dance'):
        await message.channel.send('lol i cant dance im bot')

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
        await message.channel.send('Is here a Invite For add in your server. link=https://discordapp.com/api/oauth2/authorize?client_id=703427882726457403&permissions=8&scope=bot and server invite =https://discord.gg/6AkeDD9')


async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)

client.run('NzAzNDI3ODgyNzI2NDU3NDAz.Xqt8hA.QoQIt7HlHYFLao59P5S4g8p7qsU')
