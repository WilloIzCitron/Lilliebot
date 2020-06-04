import asyncio
import ast
import random
import discord
import webserver
from discord.ext.commands import Bot
from webserver import keep_alive
from discord.ext import commands
import json

client = discord.Client()
commands = commands.Bot(command_prefix='l$')

print('Please wait ok')


@client.event
async def on_ready():
	myAct = discord.Activity(name=str(len(client.users))+ ' People in '+str(len(client.guilds))+' Cities '' | l$ ', type=discord.ActivityType.listening)
	await client.change_presence(status=discord.Status.idle, activity=myAct,)
	print('Bot is online')
	print('Console has Launched')
	print('Lilliebot Console By WilloIzCitron')

@client.event
async def on_message(message):
    msg = message.content.lower()
    split = message.content.split()
    if message.author.bot==True:
       return
    if message.author == client.user:
        return

    if '<@!703427882726457403>' in message.content or '<@703427882726457403>' in message.content:
        embed = discord.Embed(
            title="", description="hello {0.author.mention} My Prefix is `l$` | use `l$help`".format(message), color=(random.choice([0x00ff00, 0x0ff0ff, 0xff01ff,0xfd300f,0x000000])))
        embed.set_footer(text='dont ping me again :v')

    if message.content.startswith('l$hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))

    if msg.startswith('l$avatar'):
        embed = discord.Embed(colour=discord.Colour.magenta())
        embed.set_image(url=message.guild.get_member(int(split()[1][2:][:-1])).avatar_url)

    if message.content.startswith('l$whoareyou'):
        await message.channel.send('im liliebot i can help you')

    if message.content.startswith('l$lol'):
        await message.channel.send('hahaha its funny!')

    if message.content.startswith('l$dance'):
        await message.channel.send(random.choice(['lol i cant dance im bot', 'try this a song https://www.youtube.com/watch?v=A67ZkAd1wmI']))

    if message.content.startswith('l$about'):
        embed = discord.Embed(
            title="Lilliebot Biodata", description=(random.choice(['this is fun fact?', 'also try username601', 'what is this?', 'also try Nezumi Yui', 'you know? who is Vladimir Putin', 'press Alt+F4', 'you know? who is Ash Kentchum','You eat Nugget everyday?'])), colour=0xFBFB9B)
        embed.add_field(name='Bot Biodata', value='Programing code:python(py)\nBot Created:April 25 2020\nCreated by: ||<@479642404216111124> or someball45#2588||\nDefault Prefix: l$')
        embed.add_field(name='Programer biodata', value='Favorite game=Terraria,Minecraft,From The Depths, Pc Buidling Simulator\nFavorite Language:Python,HTML,Javascript\nName:Willoizcitron\nSocial Media:\n[Github](https://github.com/WilloIzCitron)')
        embed.set_footer(text='©Willoizcitron 2020-2020')

    if message.content.startswith('l$nuke'):
         embed = discord.Embed(title="Nuke Complete", description="You completly nuke this channel", colour=0x0ff00)
         embed.set_image(url='https://i.makeagif.com/media/12-22-2015/_1JY9N.gif')


    if message.content.startswith('l$covid'):
        await message.channel.send('Dont touch me pls, {0.author.mention} is possitive coronavirus!'.format(message))

    if message.content.startswith('l$shoot'):
        await message.channel.send('Hahaha you are dead'.format(message))

    if message.content.startswith('l$god'):
        await message.channel.send(random.choice(['i dont know about that the Lillie is G O D', 'by the way the laptop had G O D specs', 'we need a G O D Terraria', 'is here a G O D Mario', 'i catch a G O D Pokemon']))

    if msg.startswith('l$ping'):
      embed = discord.Embed(
            title="", description="**Pong!** \nBot latency is "+str(round(client.latency*1000)) + "ms".format(message), color=0x00ff00)
      embed.set_thumbnail(url='https://cdn.dribbble.com/users/729829/screenshots/4272534/galshir-pingpong-slow-motion.gif')
      embed.set_footer(text='you dont know latency?')
      

    if message.content.startswith('l$pokemon'):
        await message.channel.send(random.choice(['Pikachu', 'Eevee', 'Charmander', 'Bulbasaur', 'Squirtle']))

    if msg.startswith(f'l$say'):
        await message.delete()
        await message.channel.send(message.content[int(len(split[0])+1):])


    if message.content.startswith('l$invite'):
      embed = discord.Embed(
            title="Invite Links", description="Please invite me to your server 😊", color=(random.choice([0x00ff00, 0x0ff0ff, 0xff01ff,0xfd300f,0x000000])))
      embed.add_field(name='Links', value='[Bot Invite](https://discordapp.com/api/oauth2/authorize?client_id=703427882726457403&permissions=8&scope=bot)\n[Support Server](https://discord.gg/6AkeDD9)')
      embed.set_footer(text='Please Support him')


    if message.content.startswith('l$randomnpc'):
        await message.channel.send(random.choice(['https://www.pngitem.com/pimgs/m/446-4468761_terraria-guide-npc-hd-png-download.png You Got Guide', 'https://66.media.tumblr.com/247cfd904f5fb23a6de54d3cb8a1b9b6/tumblr_phngb6yM2G1vhhmun_540.jpg You Got Dryad', 'https://vignette.wikia.nocookie.net/terraria/images/4/4d/NPC_19.png/revision/latest?cb=20200425230158 You Got Arms Dealer', ]))

    if msg.startswith('someball'):
        await message.channel.send('somegirl')

    if msg.startswith(f'l$help'):
        embed = discord.Embed(
            title="<a:animatedcheck:716553160314847242> Lilliebot Help", description="Is here a Help Pages,{0.author.mention}".format(message), color=(random.choice([0x00ff00, 0x0ff0ff, 0xff01ff,0xfd300f,0x000000])))
 
 
        embed.add_field(name='Roleplay',
                        value='`hello, lol, covid, shoot `', inline='False')
        embed.add_field(name='Games Themed Commands',
                        value='`randomnpc, pokemon `', inline='False')
        embed.add_field(name='Miscellaneous',
                        value='`ping, invite, god, about, dance, whoareyou `', inline='False')
        embed.set_footer(text='the prefix is `l$`|Made By someball45#2588')

    await message.channel.send(embed=embed)



async def on_guild_join(guild, message):
  await message.channel.send('Thanks For Invite Me') 


keep_alive()
client.run('You Token Here')
