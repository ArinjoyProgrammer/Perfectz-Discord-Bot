import discord
from discord.ext import commands
from datetime import datetime


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

        
    emojis = ['✨', '', '', '', '']

    ## Main Help Command
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Help Command ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        # embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        embed.add_field(name="✨ Normal Commands", value="``p.help commands``", inline=True)
        embed.add_field(name="💡 Moderation Commands", value="``p.help moderation``", inline=True)
        embed.add_field(name="😃 User Commands", value="``p.help usercommands``", inline=True)
        embed.add_field(name="⏲️ Datetime Commands", value="``p.help datetime``", inline=True)
        embed.add_field(name="🎌 Roles Commands", value="``p.help roles``", inline=True)
        embed.add_field(name="📰 Images Command", value="``p.help images``", inline=True)
        embed.add_field(name="🕹️ Games Commands", value="``p.help games``", inline=True)
        embed.add_field(name="💡 Calculator Commands", value="``p.help calculator``", inline=True)
        embed.add_field(name="😃 Normal Messages Commands", value="``p.help normiemsg``", inline=True)
        embed.add_field(name="🌇 Other More Commands", value="``p.help othermorecmds``", inline=True)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)



    ## Other Help Commands
    @help.command()
    async def commands(self, ctx):

        embed = discord.Embed(title="Chat Commands Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Normal Commands (Without Special Arguments) (With Prefix)", value="```ping, pong, hello, hi, fine, bad, invite, botversion, info, tos```", inline=False)
        embed.add_field(name="Slap (With Prefix)", value="``p.slap <mention the member> <write the reason>``", inline=False)
        embed.add_field(name="Wish (With Prefix)", value="``p.wish <mention the member> <write the wish>``", inline=False)
        embed.add_field(name="Greet (With Prefix)", value="``p.greet <mention the member> <greet message>``", inline=False)
        embed.add_field(name="Eightball (With Prefix)", value="``p.eightball <question>``", inline=False)
        embed.add_field(name="Spoiler (With Prefix)", value="``p.spoiler <spoiler message>``", inline=False)
        embed.add_field(name="Github (With Prefix)", value="``p.github``", inline=False)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)


    @help.command()
    async def roles(self, ctx):

        embed = discord.Embed(title="Add Roles Commands Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Add Role (With Prefix)", value="``p.addrole <mention the member> <mention the role>``", inline=False)
        embed.add_field(name="Remove Role (With Prefix)", value="``p.removerole <mention the member> <mention the role>``", inline=False)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)


    @help.command()
    async def calculator(self, ctx):

        embed = discord.Embed(title="Calculator Commands Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Calculation (Addition)", value="``p.add <give first number> <give second number>``\nExample - ``p.add 10 10``", inline=False)
        embed.add_field(name="Calculation (Substraction)", value="``p.sub <give first number> <give second number>``\nExample - ``p.sub 10 5``", inline=False)
        embed.add_field(name="Calculation (Multiplication)", value="``p.mul <give first number> <give second number>``\nExample - ``p.mul 10 10``", inline=False)
        embed.add_field(name="Calculation (Division)", value="``p.div <give first number> <give second number>``\nExample - ``p.div 10 5``", inline=False)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)


    @help.command()
    async def datetime(self, ctx):

        embed = discord.Embed(title="Datetime Command Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Datetime (Without Special Arguments) (With Prefix)", value="```p.nowtime, p.date, p.time```", inline=False)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)


    @help.command()
    async def images(self, ctx):

        embed = discord.Embed(title="Meme Command Help  ||  Perfectz Bot", decsription="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Meme (Without Special Arguments) (With Prefix)", value="``p.meme``", inline=False)
        embed.add_field(name="Random Image (With Prefix)", value="``p.img <image name>``", inline=False)
        embed.set_footer(text=f"Command Requested bt {ctx.author}")

        await ctx.send(embed=embed)


    @help.command()
    async def games(self, ctx):
        embed = discord.Embed(title="Games Command Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Games (With Prefix)", value="``p.rps, p.gtn <number between 1 and 10>``", inline=False)
        embed.set_footer(text=f'Command Requested by {ctx.author}')

        await ctx.send(embed=embed)


    @help.command()
    async def normiemsg(self, ctx):

        embed = discord.Embed(title="Normal Messages Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Normal Messages (Without Special Arguments) (Prefix Isn't Required)", value="```perfectz```", inline=False)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)


    @help.command()
    async def moderation(self, ctx):
        
        embed = discord.Embed(title="Moderation Commands Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Mute Command (With Prefix)", value="``p.mute <mention the member> <reason for muting>``", inline=False)
        embed.add_field(name="Unmute Command (With Prefix)", value="``p.unmute <mention the member>``", inline=False)
        embed.add_field(name="Kick Command (With Prefix)", value="``p.kick <mention the member> <reason for kicking>``", inline=False)
        embed.add_field(name="Ban Command (With Prefix)", value="``p.ban <mention the member> <reason for banning>``", inline=False)
        embed.add_field(name="Unban Command (With Prefix)", value="``p.unban <mention the member>``", inline=False)
        embed.add_field(name="Report Command (With Prefix)", value="``p.report <mention the member> <reason for reporting>``", inline=False)
        embed.add_field(name="Warn Command (With Prefix)", value="``p.warn <mention the member> <reaon for warning>``", inline=False)
        embed.add_field(name="Clear Command (With Prefix)", value="``p.clear <amount of messages>``", inline=False)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)


    @help.command()
    async def usercommands(self, ctx):
        embed = discord.Embed(title="User Commands Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Announcement Command (With Prefix)", value="``p.announce <announcement message here>``", inline=False)
        embed.add_field(name="Say Command (With Prefix)", value="``p.say <your message here>``", inline=False)
        embed.add_field(name="Dm Command (With Prefix)", value="``p.dm <mention the member> <message for dm>``", inline=False)
        embed.add_field(name="Alert Command (With Prefix)", value="``p.alert <alert message here>``", inline=False)
        embed.add_field(name="Alert Command (With Embed) (With Prefix)", value="``p.alert_em <your message here>``", inline=False)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)


    @help.command()
    async def othermorecmds(self, ctx):
        embed = discord.Embed(title="Other More Commands Help  ||  Perfectz Bot", description="", timestamp=datetime.utcnow(), color=ctx.author.color)
        embed.add_field(name="Other More Commands (Without Special Arguments) (With Prefix)", value="```p.membercount, p.serverinfo, p.whois, p.rip, p.poll, p.joined```", inline=False)
        embed.add_field(name="Pollwrite (With Prefix)", value="``p.pollwrite <your message here>``", inline=False)
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(HelpCommand(client))
