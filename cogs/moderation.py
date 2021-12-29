import discord
from discord.ext import commands
from datetime import datetime


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client



    # Mute Command
    @commands.command(pass_context = True)
    async def mute(self, ctx, member: discord.Member):
        if ctx.message.author.server_permissions.administrator:
            role = discord.utils.get(member.server.roles, name='Muted')
            await ctx.add_roles(member, role)
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
            await ctx.send(embed=embed)


    # Unmute Command
    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        try:
            await member.send(f" you have unmutedd from: - {ctx.guild.name}")
        except:
            await ctx.send("The member's dms were closed!")
        
        embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)


    # Kick Command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        if reason==None:
            reason=" no reason provided"
        
        await ctx.guild.kick(member)
        await ctx.send(f'User {member.mention} has been kicked for {reason}')


    # Ban Command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason):
        await ctx.guild.ban(user, reason=reason) # Bans the user.
        await user.send(f"You have been banned in {ctx.guild} for {reason}")
        await ctx.send(f"{user} has been successfully banned.")


    # Unban Command
    @commands.command()
    async def unban(self, ctx, *,member):
        banned_user = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_user:
            user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send("THE MESSAGES ARE DELETED", delete_after=2)
        


def setup(client):
    client.add_cog(Moderation(client))
