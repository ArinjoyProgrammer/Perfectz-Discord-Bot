from types import prepare_class
from asyncio.locks import Event
import discord
from discord.ext import commands
import os
import asyncio
import random
import json
from dotenv import load_dotenv

load_dotenv()

prefixes = 'p.', 'P.', '.', '>'

client = commands.Bot(command_prefix = prefixes)

client.remove_command("help")


@client.event
async def on_ready():
    print("The Bot is Ready")



async def ch_pr():
    await client.wait_until_ready()

    statuses = ['p.help', f'On {len(client.guilds)} servers']

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=status))
        # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(5)

client.loop.create_task(ch_pr())



@client.event
async def on_ready():
    print(f"{client.user} is Online on Discord")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")



client.run(os.getenv('token'))
