import discord
from discord.ext import commands
import aiohttp
import random


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/memes.json") as r:
                memes = await r.json()
                embed = discord.Embed(color=discord.Color.random())
                embed.set_image(url=memes['data']['children'][random.randint(0, 25)]['data']['url'])
                embed.set_footer(text=f"Requested By  {ctx.author}")
                await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Meme(client))
