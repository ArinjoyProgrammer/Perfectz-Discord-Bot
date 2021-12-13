import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import random


class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def luckynumber(self, ctx):
        luckynumber = random.randint(0, 100)

        embed = discord.Embed(title="What is your Lucky Number?", description=f"Your **Lucky Number** is **{luckynumber}**\nDon't forget to check your **Lucky Number** again", timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)


    @commands.command(aliases=['cr'])
    async def coolrate(self, ctx):
        coolrate = random.randint(0, 100)

        embed = discord.Embed(title="What is your Cool Rate?", description=f"Your **Cool Rate** is {coolrate}**%\nDon't forget to check your **Cool Rate** again!")


    @commands.command()
    async def hack(self, ctx, member : discord.Member):

        random_password = ['36b29c', 'kt764a', '45cvv76', 'fh90;ll', 'gda889', 'kla789', 'kkk89q', 'ff89f52', '95632lrt']

        await ctx.send(f"Hacking Satrted on {member}")
        await ctx.send(f"Hacking Username and Password of {member}")
        await asyncio.sleep(4)
        await ctx.send(f"Hacked!\nUsername - ``{member}``\nPassword - ``{random.choice(random_password)}``")
        await asyncio.sleep(4)
        await ctx.send("Hacking Completed 20%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 30%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 50%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Epic Games and Steam Account")
        await asyncio.sleep(2)
        await ctx.send("Hacking Epic Games and Steam Account Completed Successfully")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 80%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 90%")
        await asyncio.sleep(4)
        await ctx.send(f"A **Dangerous Hacking** Completed on **{member}**\nDon't mind this was a really **Fake Hack**")

        

def setup(client):
    client.add_cog(FunCommands(client))