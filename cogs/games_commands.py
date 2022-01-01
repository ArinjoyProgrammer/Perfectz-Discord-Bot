import discord
from discord.ext import commands
import random
from datetime import datetime

class Rps(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(description="This Command is on maitainance")
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



    @commands.group(invoke_without_command=True, aliases=['gtn', 'guess_the_num', 'guessthenum', 'guessthenumber'])
    async def guess_the_number(self, ctx, user_choice):
        # def check(msg):
        #     return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in embed

        # user_choice = (await self.client.wait_for('message', check=check)).content
        computer_choice = random.randint(1, 10)
        colors = discord.Color.random(), discord.Color.gold()
        colors_random = random.choice(colors)

        if (user_choice == computer_choice):
            embed = discord.Embed(title="Guess the Number (Game)", description=f"Wow You choosed the **correct option** like the **Bot choose**!\nBot choosed {computer_choice}", timestamp=datetime.utcnow(), color=colors_random)
            await ctx.send(embed=embed)

        elif (user_choice is not computer_choice):
            embed = discord.Embed(title="Guess the Number (Game)", description=f"Your choice is **not matching** with the **Bot's choice**\nBot choosed **{computer_choice}**\nBetter luck next time {ctx.author.mention}", timestamp=datetime.utcnow(), color=colors_random)
            await ctx.send(embed=embed)

        elif (user_choice > 10):
            embed = discord.Embed(title="Guess the Number (Game)", description="Umm, you are doing some wrong things!\nPlease choose numbers which are **lesser that 10 and it should be between 1 and 10**!", timestamp=datetime.utcnow(), color=colors_random)
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title="Guess the Number (Game)", description=f"I can't recognize your message please run the command again!", timestamp=datetime.utcnow(), color=colors_random)


    # Commands help
    @guess_the_number.group()
    async def help(self, ctx):
        embed = discord.Embed(title="Guess the Number (Game)", description="Guess your number between 1 and 10", timestamp=datetime.utcnow(), color=ctx.author.color)
        
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Rps(client))
