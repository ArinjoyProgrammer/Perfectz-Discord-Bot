import discord
from discord.ext import commands


class MessageContentCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if self.client.mentioned(message):
    #         await message.send("Hello my name is ``Perfectz Bot`` and my prefix in this server is ``p. and P.``")
    

    
def setup(client):
    client.add_cog(MessageContentCommands(client))
