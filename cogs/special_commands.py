import discord
from discord import emoji
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import random
from PIL import Image
from io import BytesIO
from discord_components import *


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
        await ctx.send("The maintenance will be planned later\nNow you can use the bot freely")


    @commands.command()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)

        server_name = str(ctx.guild.name)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description="",
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Server Name", value=server_name, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Channels: ", value=len(
            ctx.message.guild.channels), inline=True)
        embed.add_field(name="Country", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.add_field(name="Requested By: ", value=str(
            ctx.message.author.mention), inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def whois(self, ctx, user: discord.Member = None):

        created_at = user.created_at
        joined_at = user.joined_at

        created = created_at.strftime("Date: %d/%m/%y  |  Time: %H:%M:%S")
        joined = joined_at.strftime("Date: %d/%m/%y  |  Time: %H:%M:%S")

        if user == None:
            user = ctx.author

        rlist = []
        for role in user.roles:
            if role.name != "@everyone":
                rlist.append(role.mention)

        b = ", ".join(rlist)

        embed = discord.Embed(colour=user.color, timestamp=datetime.now())

        embed.set_author(name=f"User Info - {user}"),
        embed.set_thumbnail(url=user.avatar_url),

        embed.add_field(name='ID:', value=user.id, inline=False)
        embed.add_field(name='Name:', value=user.display_name, inline=False)

        embed.add_field(name='Created at:', value=created, inline=False)
        embed.add_field(name='Joined at:', value=joined, inline=False)

        embed.add_field(name='Bot?', value=user.bot, inline=False)

        embed.add_field(name=f'Roles:({len(rlist)})',
                        value=''.join([b]), inline=False)
        embed.add_field(name='Top Role:',
                        value=user.top_role.mention, inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def joined(self, ctx, *, member: discord.Member):
        joined_at = member.joined_at
        time_joined = joined_at.strftime("Date: %d/%m/%y  |  Time: %H:%M:%S")

        await ctx.send(f"**{member}** joined on **{time_joined}**")


    @commands.command(aliases=['cngnick'])
    async def change_nick(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')



def setup(client):
    client.add_cog(SpecialCommands(client))
