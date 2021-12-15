import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import random


class UserCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def alert(self, ctx, *, alert_msg="No **Alert** Message was given!"):
       await ctx.send(f"{alert_msg}\n\nMessage Created by **{ctx.author}**")


    @commands.command()
    async def alert_em(self, ctx, member: discord.Member, *, alert_em_msg="No **Alert** Message was given!"):
        
        embed = discord.Embed(title="Alert Message!", description=f"{alert_em_msg}", timestamp=datetime.now(), color=ctx.author.color)
        embed.set_footer(text=f"Message Created by   {ctx.author}")

        await member.send(embed=embed)

    @commands.command()
    async def dm(self, ctx, member: discord.Member, *, dm_msg="No **DM** Message was given!"):
        await member.send(f"{dm_msg}\n\nMessage sent by **{ctx.author}**")



def setup(client):
    client.add_cog(UserCommands(client))
