import discord
from discord.ext import commands
from datetime import datetime
import time


class AddRoles(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)

        embed = discord.Embed(title=f"{member} You have been Given a **Role**!", description=f"hey {member.mention}, You have given a role called: **{role.name}**", timestamp=datetime.now(), color=ctx.author.color)

        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)

        embed = discord.Embed(title=f"{member} You have been Given a **Role**!", description=f"hey {member.mention}, Your role has been removed called: **{role.name}**", timestamp=datetime.now(), color=ctx.author.color)

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(AddRoles(client))
