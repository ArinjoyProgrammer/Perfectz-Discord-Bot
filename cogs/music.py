import asyncio
from collections import UserDict, UserList, UserString
from types import GenericAlias
from datetime import datetime
import discord
from discord import FFmpegPCMAudio
from discord import player
from discord import voice_client
from discord import guild
from discord import emoji
from discord.channel import VoiceChannel
from discord.enums import VoiceRegion
import json
import os
from discord import user
from discord import message
from discord.ext import commands
from discord import colour
import random
from discord.ext.commands import bot
import youtube_dl
import asyncio
import discord.ext.commands.bot
from discord.ext.commands.converter import MemberConverter, VoiceChannelConverter
from types import GenericAlias
import discord
from discord import colour
from discord.gateway import VoiceKeepAliveHandler
from discord.member import VoiceState



class MusicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def join(ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('schedulen.wav')
            player - voice.play(source)
        else:
            await ctx.send("you are not in a voice channel, you must be in a voice channel to run this command!")
    @commands.command(pass_context = True)
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice channel")
        else:
            await ctx.send("I am not in a voice channel")

    @commands.command(pass_context=True)
    async def play(self, ctx, url : str):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()

            # download the youtube video
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file .endswidth(".mp3"):
                    os.rename(file, "song.mp3")

                    source = FFmpegPCMAudio('song.mp3')
                    player - voice.play(source)

            else:
                await ctx.send("you are not in a voice channel, you must be in a voice channel to run this command!")

    @commands.command(pass_context=True)
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients,guild-ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("at the moment, there is no audio playing in the voice channel!")


    @commands.command(pass_context=True)
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients,guild=ctx.guild)
        if voice.is_playing():
            voice.resume()
        else:
            await ctx.send("at the moment, there is no song is paused!")



def setup(client):
    client.add_cog(MusicCommands(client))
