import discord
from discord.ext import commands
from discord_components.dpy_overrides import send_message


class MessageContentCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_message(self, message):

        msg = message.content

        if msg.startswith("perfectz"):
            await message.channel.send("Hello my name is ``Perfectz Bot`` and my prefix in this server is ``p. and P.``")
    

    
def setup(client):
    client.add_cog(MessageContentCommands(client))
