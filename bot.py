import discord
from discord.ext import commands
import openai
from config import DISCORD_TOKEN, OPENAI_API_KEY

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
openai.api_key = OPENAI_API_KEY

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='joke')
async def tell_joke(ctx):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a funny bot. Tell a short, clean joke."},
            {"role": "user", "content": "Tell me a joke"}
        ]
    )
    joke = response.choices[0].message.content
    await ctx.send(joke)

@bot.command(name='rps')
async def rock_paper_scissors(ctx, choice: str):
    import random
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    
    if choice.lower() not in choices:
        await ctx.send("Please choose rock, paper, or scissors!")
        return

    await ctx.send(f"I choose {bot_choice}!")
    
    if choice.lower() == bot_choice:
        await ctx.send("It's a tie!")
    elif (choice.lower() == 'rock' and bot_choice == 'scissors') or \
         (choice.lower() == 'paper' and bot_choice == 'rock') or \
         (choice.lower() == 'scissors' and bot_choice == 'paper'):
        await ctx.send("You win! 🎉")
    else:
        await ctx.send("I win! 😎")
