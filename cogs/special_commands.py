import discord
from discord import emoji
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import random
from PIL import Image
from io import BytesIO


class SpecialCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def announcement(self, ctx, *, announcement):
        await ctx.send(f"{announcement}")


    @commands.command(aliases=['mc'])
    async def membercount(self, ctx):
        embed = discord.Embed(title="Members", description=f"{ctx.guild.member_count}", timestamp=datetime.utcnow(), color=discord.Color.blue())
        await ctx.send(embed=embed)


    @commands.command()
    async def rip(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open('rip.jpg')
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((179, 125))

        wanted.paste(pfp, (228, 206))

        wanted.save("profile.jpg")

        await ctx.send(file = discord.File("profile.jpg"))


    @commands.command()
    async def say(self, ctx, *, say="No **say** command was told!"):
        await ctx.send(f"{say}")
        await ctx.message.delete()


    @commands.command()
    async def poll(self, ctx):
        thumbsup = "👍"
        thumbsdown = "👎"

        embed = discord.Embed(title="Poll Time!", description="👍 You like it - 👎 You don't like it", timestamp=datetime.utcnow(), color=ctx.author.color)

        reaction = await ctx.send(embed=embed)

        await reaction.add_reaction(emoji=thumbsup)
        await reaction.add_reaction(emoji=thumbsdown)


    @commands.command()
    async def pollwrite(self, ctx, *, poll="No **poll** was given!"):
        thumbsup = "👍"
        thumbsdown = "👎"

        embed = discord.Embed(title="Poll Time!", description=f"{poll}", timestamp=datetime.utcnow(), color=ctx.author.color)

        reaction = await ctx.send(embed=embed)

        await reaction.add_reaction(emoji=thumbsup)
        await reaction.add_reaction(emoji=thumbsdown)


    # view futures maintenance
    @commands.command()
    async def earlymaintenance(self, ctx):
        await ctx.send("The maintenance is now going on!")


def setup(client):
    client.add_cog(SpecialCommands(client))
