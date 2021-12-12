import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import random


class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def luckynumber(self, ctx):
        luckynumber = random.randint(0, 100)

        embed = discord.Embed(title="What is your Lucky Number?", description=f"Your **Lucky Number** is **{luckynumber}**\nDon't forget to check your **Lucky Number** again", timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)


    @commands.command(aliases=['cr'])
    async def coolrate(self, ctx):
        coolrate = random.randint(0, 100)

        embed = discord.Embed(title="What is your Cool Rate?", description=f"Your **Cool Rate** is {coolrate}**%\nDon't forget to check your **Cool Rate** again!")

        

def setup(client):
    client.add_cog(FunCommands(client))