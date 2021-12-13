import discord
from discord.ext import commands
from datetime import datetime


class ModerationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    # Unmute Command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        embed = discord.Embed(
            title="Unmute",
            description=f" unmuted-{member.mention}",
            colour=discord.Colour.green()
        )
        await ctx.send(embed=embed)
        await member.send(f"You have unmuted from: - {ctx.guild.name}")


    # Kick Command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(
            title="Kicked!",
            description=f"{member} has been Kicked from {ctx.guild.name}  |  Reason: {reason}",
            timestamp=datetime.now(),
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        await member.kick(f"You have been Kicked from {ctx.guild.name}  |  Reason: {reason}")


    # Ban Command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(
            title="Ban!",
            description=f"{member} You have been banned from {ctx.guild.name}  |  Reason: {reason}",
            timestamp=datetime.now(),
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        await member.ban("You have been Banned from {ctx.guild.name}  |  Reason: {reason}")


    # Unban Command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


    # Warning Command
    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(
            title="Warning!",
            description=f"{member.mention} has been warned from {ctx.guild.name}  |  Reason: {reason}",
            timestamp=datetime.now(),
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        await member.send(f"You have been Warned from {ctx.guild.name}  |  Reason: {reason}")


    @commands.command()
    async def report(self, ctx, member: discord.Member, *, report="No **Report Message** was given!"):
        embed = discord.Embed(
            title = "Report!",
            description = f"{member.mention} You have been **Reported** from {ctx.guild.name}  |  Reason: {report}",
            timestamp = datetime.now(),
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)

        embed = discord.Embed(
            title = "Report!",
            description = f"{member.mention} You have been **Reported** from {ctx.guild.name}  |  Reason: {report}",
            timestamp = datetime.now(),
            color = discord.Color.red()
        )
        await member.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send("THE MESSAGES ARE DELETED", delete_after=2)

    @clear.error
    async def clear_error(self, error, ctx):
        if isinstance(error, error.MissingPermissions):
            await ctx.send(":redTick: You don't have permission to Clear/Delete messages!.")



def setup(client):
    client.add_cog(ModerationCommands(client))
