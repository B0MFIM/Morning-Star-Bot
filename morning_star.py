#import os
from decouple import config
from discord.ext import commands

bot = commands.Bot("@")

def load_cogs(bot):
    bot.load_extension("manager")

    """
    for file in os.listdir("Commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"Commands.{cog}")
    
    for file in os.listdir("Tasks"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"Tasks.{cog}")
    """

load_cogs(bot)

TOKEN = config("TOKEN_SECRET")
bot.run(TOKEN)