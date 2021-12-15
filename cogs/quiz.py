import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import random


class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def quiz(self, ctx):
        await ctx.send("The Quiz Command is not ready yet")



def setup(client):
    client.add_cog(Quiz(client))
