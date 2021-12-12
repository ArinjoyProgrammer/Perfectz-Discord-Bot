import discord
from discord.ext import commands
from datetime import datetime


class ChannelCommands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send('Channel locked.')


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.mention + " ***has been unlocked.***")





    # Channel Errors
    # @lock.error
    # async def lock_error(ctx, error):
    #     if isinstance(error,commands.CheckFailure):
    #         await ctx.send('You do not have permission to use this command!')

def setup(client):
    client.add_cog(ChannelCommands(client))
