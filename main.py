import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os
import asyncio
import random
from datetime import datetime
import json
from dotenv import load_dotenv

load_dotenv()

prefixes = 'p.', 'P.', '.', '>'

intents = discord.Intents.all()

client = commands.Bot(command_prefix = prefixes, intents=intents)

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
async def on_member_join(member):
    embed = discord.Embed(title="Welcome to the server", description=f"Welcome! {member.mention} to the server, Enjoy your stay here!", timestamp=datetime.utcnow(), color=discord.Color.random())

    await member.send(embed=embed)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(title="Goodbye from the server", description=f"Goodbye! {member.mention} from the server!", timestamp=datetime.utcnow(), color=discord.Color.random())

    await member.send(embed=embed)



@client.event
async def on_ready():
    print(f"{client.user} is Online on discord")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("You can't do that! ;-;\nReason: Missing Permissions in the server")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You are missing required arguments!\nFor help type ``p.help``")
    # elif isinstance(error, commands.errors.CommandNotFound):
    #     await ctx.reply("No such command was found!\nYou can type **p.help** for more info")
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.reply(f"Data Type passed id invalid\n`{str(error)}`")
        
    else:
        raise error



client.run(os.getenv('token'))
