import discord
from discord.ext import commands
from datetime import time
import time


class Datetime(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def nowtime(self, ctx):

        nowtimeis = time.strftime("Date: %d/%m/%y\nTime: %H:%M:%S")

        embed = discord.Embed(title="The Time is: ", description=f"**{nowtimeis}**", color=ctx.author.color)
        embed.set_footer(text=f"Requested by   {ctx.author}")

        await ctx.send(embed=embed)


    @commands.command()
    async def time(self, ctx):
        nowtimeis = time.strftime("Time: %H:%M:%S")

        embed = discord.Embed(title="The Time is: ", description=f"**{nowtimeis}**", color=ctx.author.color)
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)


    @commands.command()
    async def date(self, ctx):
        nowtimeis = time.strftime("Date: %d/%m/%y")

        embed = discord.Embed(title="The Day is: ", description=f"**{nowtimeis}**", color=ctx.author.color)
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)

            

def setup(client):
    client.add_cog(Datetime(client))
