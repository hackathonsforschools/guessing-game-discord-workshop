import random
import discord
from discord.ext import commands

TOKEN = "paste_your_token_here"
PREFIX = "!"
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 10

bot = commands.Bot(command_prefix=PREFIX)
numbers = {}

# This is triggered when the bot has started up.
@bot.event
async def on_ready():
    print("Bot ready!")

# This is run every time a message is sent on the Discord server
@bot.event
async def on_message(message):
    await bot.process_commands(message)

# This is triggered when a user says !start in the Discord server
@bot.command()
async def start(ctx):
    user_id = str(ctx.message.author.id)

    if user_id in numbers:
        await ctx.send("Already in a game!")
        return

    random_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER + 1)

    numbers[user_id] = random_number

    await ctx.send(f"I'm thinking of a number between {LOWEST_NUMBER} and {HIGHEST_NUMBER}\nType `!guess (number)` to make guesses!")
    print(numbers)

# This is triggered when a user says !guess in the Discord server
@bot.command()
async def guess(ctx):
    user_id = str(ctx.message.author.id)

    if user_id not in numbers:
        await ctx.send("You are not in a game yet! Use `!start` to begin one.")
        return

    guessed_number = int(ctx.message.content.split(' ')[1])

    actual_number = numbers[user_id]

    if guessed_number > actual_number:
        await ctx.send("Too high!")
    elif guessed_number < actual_number:
        await ctx.send("Too low!")
    else:
        await ctx.send(f"Correctly guessed, the number is {actual_number}!")
        del numbers[user_id]

# This prints out that the bot is starting up.
print('\x1b[2J\nBot starting...')
bot.run(TOKEN)