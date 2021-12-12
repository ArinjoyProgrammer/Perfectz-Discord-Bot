import discord
from discord import embeds
from discord.ext import commands
from datetime import datetime
import time


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")

    @commands.command()
    async def slap(self, ctx, member: discord.Member, *, reason="No reason was given for Slapping!"):

        embed = discord.Embed(title="Slapped!!!", description=f"You slapped {member.mention}  |  Reason: **{reason}**", timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    async def wish(self, ctx, member: discord.Member, *, wish="No wish was give for the user!"):
        
        embed = discord.Embed(title="Wish!", description=f"You wished **{wish}** for {member.mention}", timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    async def greet(self, ctx, member: discord.Member, *, greet="No Greetings were given for the user!"):

        embed = discord.Embed(title="Greetings!", description=f"You Greeted **{greet}** for {member.mention} !", timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    async def hello(self, ctx):
        await ctx.reply(f"Hi! {ctx.author.mention} How are you?")

    @commands.command()
    async def hi(self, ctx):
        await ctx.reply(f"Hello! {ctx.author.mention} How are you doing?")

    @commands.command()
    async def fine(self, ctx):
        await ctx.reply("Wow! Excellent!")

    @commands.command()
    async def bad(self,  ctx):
        await ctx.reply("Oh! So bad!")

    @commands.command(aliases=['inv'])
    async def invite(self, ctx):

        embed = discord.Embed(title="Invite The Bot", description="Invite by clicking here  -->  [Click Invite](https://discord.com/oauth2/authorize?client_id=898073261982769185&scope=bot&permissions=1099511627775)", timestamp=datetime.utcnow(), color=discord.Color.purple())
        await ctx.send(embed=embed)

    @commands.command()
    async def botversion(self, ctx):
        botversions = ['Beta Version (Development Version)', '0.1.0', '0.2.0', '0.3.0', '0.4.0', '0.5.0']

        embed = discord.Embed(title="Bot Version!", description=f"The Version of the bot is **{botversions[0]}**", timestamp=datetime.utcnow(), color=discord.Color.random())

        await ctx.send(embed=embed)

    @commands.command()
    async def botinfo(self, ctx):

        embed = discord.Embed(title="Bot Info", description="**Description** - This is a Bot that can save your time and Chat with you when you are totally free!", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Developer", value="< Arinjoy.py />#0994", inline=False)
        embed.add_field(name="Support Us", value="[invite](https://discord.com/oauth2/authorize?client_id=898073261982769185&scope=bot&permissions=1099511627775)")
        embed.set_footer(text=f"Command Requested By    {ctx.author}")

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Commands(client))
