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
        embed = discord.Embed(description=f"Pong! ```{self.client.latency * 1000}``` ms!")

        await ctx.send(embed=embed)

    @commands.command()
    async def pong(self, ctx):
        embed = discord.Embed(description=f"Ping! ```{self.client.latency * 1000}``` ms")

        await ctx.send(embed=embed)

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

        embed = discord.Embed(title="Invite The Bot", description="These are the two invite links of the bot!", timestamp=datetime.utcnow(), color=discord.Color.purple())

        embed.add_field(name="Invite Link", value="[Click To Invite](https://discord.com/oauth2/authorize?client_id=898073261982769185&scope=bot&permissions=1099511627775)", inline=False)

        embed.add_field(name="Invite Link (With Slash Commands (Beta))", value="[Click To Invite (With Slash Commands (Beta))](https://discord.com/api/oauth2/authorize?client_id=898073261982769185&permissions=1644972474359&scope=bot%20applications.commands)", inline=False)

        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)

    @commands.command()
    async def botversion(self, ctx):
        botversions = ['Beta Version (Development Version)', 'v0.1', 'v0.2', 'v0.3', 'v0.4', 'v0.5', 'v0.6', 'v0.7', 'v0.8', 'v0.9', 'v0.10', 'v0.11']

        embed = discord.Embed(title="Bot Version!", description=f"The Version of the bot is **{botversions[4]}**", timestamp=datetime.utcnow(), color=discord.Color.random())

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


    @commands.command()
    async def github(self, ctx):
        embed = discord.Embed(title="Github  ||  **Perfectz Discord Bot**", description="This is the Github Page of Perfectz Discord Bot", timestamp=datetime.utcnow(), color=discord.Color.purple())
        embed.add_field(name="Github Page Link", value="Github Page - https://github.com/ArinjoyProgrammer/Perfectz-Discord-Bot", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)


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


    @commands.command()
    async def updates(self, ctx):
        embed = discord.Embed(title="The Latest Update!!", description="See the Lates Updates of the bot below", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Brad New Slash Commands (Under Development)", value="Hello there! The new Slash Commands are releasing soon! There will be the same commands that the bot have but the commands will be included with the slash commands!\nBut for now you can use the normal commands (With Prefix)", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author}")

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Commands(client))
