import discord
from discord.ext import commands
import asyncio
from datetime import datetime
import time


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def event(self, ctx):

        events = ['There are no Upcoming Events!']
        reactions = ['👍', '👎']

        embed = discord.Embed(title="Event", description=f"Event - **{events[0]}**", timestamp=datetime.utcnow(), color=ctx.author.color)

        reaction = await ctx.send(embed=embed)

        await reaction.add_reaction(reactions[0])
        await reaction.add_reaction(reactions[1])



def setup(client):
    client.add_cog(Events(client))
