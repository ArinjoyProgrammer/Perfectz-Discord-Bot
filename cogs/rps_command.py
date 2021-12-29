import discord
from discord.ext import commands
import random

class Rps(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def rps(self, ctx):
        rpsGame = ['rock', 'paper', 'scissors']
        await ctx.send(f"Rock, paper, or scissors? Choose wisely...")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

        # user_choice = await self.client.wait_for('message', check=check)
        user_choice = (await self.client.wait_for('message', check=check)).content


        comp_choice = random.choice(rpsGame)
        if user_choice == 'rock':
            if comp_choice == 'rock':
                await ctx.send(f'Well, that was weird. We tied.nYour choice: {user_choice}nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'Nice try, but I won that time!!nYour choice: {user_choice}nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Aw, you beat me. It won't happen again!nYour choice: {user_choice}nMy choice: {comp_choice}")

        elif user_choice == 'paper':
            if comp_choice == 'rock':
                await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!nYour choice: {user_choice}nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!nYour choice: {user_choice}nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Aw man, you actually managed to beat me.nYour choice: {user_choice}nMy choice: {comp_choice}")

        elif user_choice == 'scissors':
            if comp_choice == 'rock':
                await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!nYour choice: {user_choice}nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'Bruh. >: |nYour choice: {user_choice}nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Oh well, we tied.nYour choice: {user_choice}nMy choice: {comp_choice}")




def setup(client):
    client.add_cog(Rps(client))
