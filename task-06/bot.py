import discord
from discord.ext import commands
import os
import logging
from dotenv import load_dotenv
from scrapper import fetch_live_score, fetch_match_history, append_to_csv

# Load environment variables
load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Set a custom help command to display the command prefix
bot.remove_command('help')

@bot.command(name='help')
async def custom_help(ctx):
    command_prefix = bot.command_prefix
    command_list = [f"{command_prefix}{command.name}" for command in bot.commands if not command.hidden]

    help_message = f"Commands:\n" + '\n'.join(command_list)
    await ctx.send(help_message)

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name}')

@bot.command(name='livescore', help='Get the live scores')
async def get_live_score(ctx):
    live_score_info = fetch_live_score()
    if live_score_info:
        await ctx.send(live_score_info)
    else:
        await ctx.send("No live scores available! Try again later.")

@bot.command(name='csv', help='Get the csv file the livescores are stored in')
async def get_match_history(ctx):
    match_history = fetch_match_history()
    if match_history:
        await ctx.send(file=discord.File('match_history.csv'))
    else:
        await ctx.send("No match history available.")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    bot.run(bot_token)
