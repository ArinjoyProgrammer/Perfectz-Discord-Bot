import discord
from discord.ext import commands
import aiohttp
import random


class ImageCommands(commands.Cog):
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


    @commands.command(aliases=['img'])
    async def image(self, ctx, arg):
        embed = discord.Embed(
            title = 'Random Image 🐈',
            description = 'Random',
            colour = discord.Colour.purple()
            )
        embed.set_image(url='https://source.unsplash.com/1600x900/?{}'.format(arg))            
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(ImageCommands(client))
