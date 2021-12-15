import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import random


class Afk(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def afk(self, ctx, *, afk_arg="No **AFK** message was given!"):
        
        embed = discord.Embed(title="", description=f"{ctx.author.mention} has gone **AFK**\nAFK Message: **{afk_arg}**", color=ctx.author.color)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Afk(client))
