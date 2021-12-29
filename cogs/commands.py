import discord
from discord import embeds
from discord.ext import commands
from datetime import datetime
import random
import time


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")

    @commands.command()
    async def pong(self, ctx):
        await ctx.reply("Ping!")

    @commands.command()
    async def slap(self, ctx, member: discord.Member, *, reason="No reason was given for Slapping!"):

        embed = discord.Embed(title="Slapped!!!", description=f"You slapped {member.mention}  |  Reason: **{reason}**", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.set_image(url="https://cdn.discordapp.com/attachments/911200129611071490/919598098941091890/slap.jpg")
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
    async def info(self, ctx):

        embed = discord.Embed(title="", description="Hello! I am **Perfectz** a **Multi-purpose** bot!", color=discord.Color.random())
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        embed.add_field(name="Prefix", value="**p.** and **P.**", inline=True)
        embed.add_field(name="discord Library", value="discord.py", inline=True)
        embed.add_field(name="Developer", value="< Arinjoy.py />#0994", inline=True)
        embed.add_field(name="In Servers", value=f"{len(self.client.guilds)}", inline=True)
        embed.add_field(name="Created on", value="December 8 2021", inline=True)
        embed.add_field(name="Discriminator", value="0", inline=True)
        embed.add_field(name="Invite", value="[Invite](https://discord.com/oauth2/authorize?client_id=898073261982769185&scope=bot&permissions=1099511627775)", inline=True)
        embed.add_field(name="Vote", value="[discord Bots List](https://discordbotlist.com/bots/perfectz)", inline=True)
        embed.set_footer(text=f"Requested by   {ctx.author}")

        await ctx.send(embed=embed)


    @commands.command()
    async def tos(self, ctx):
        await ctx.send("discord TOS: https://discord.com/terms/")

    @commands.command(aliases=['8ball', '8b'])
    async def eightball(self, ctx, *, question):
        responses = [
        'Hell no.',
        'Prolly not.',
        'Idk bro.',
        'Prolly.',
        'Hell yeah my dude.',
        'It is certain.',
        'It is decidedly so.',
        'Without a Doubt.',
        'Yes - Definitaly.',
        'You may rely on it.',
        'As i see it, Yes.',
        'Most Likely.',
        'Outlook Good.',
        'Yes!',
        'No!',
        'Signs a point to Yes!',
        'Reply Hazy, Try again.',
        'IDK but u should Invite the bot with is [INVITE](https://discord.com/oauth2/authorize?client_id=898073261982769185&scope=bot&permissions=1099511627775)!!!',
        'Better not tell you know.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't Count on it.",
        'My reply is No.',
        'My sources say No.',
        'Outlook not so good.',
        'Very Doubtful']
        await ctx.send(f":8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}")


    @commands.command()
    async def spoiler(self, ctx, *, spoiler="||No **Spoiler Message** was given||"):
        await ctx.send(f"||{spoiler}||")



def setup(client):
    client.add_cog(Commands(client))
