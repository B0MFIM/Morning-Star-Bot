from discord.ext import commands
from console_logging.console import Console
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

console = Console()

class Manager(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        console.info("Connect")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos. Digite '!help' para ver os parâmetros de cada comando.")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite '!help' para ver os comandos existêntes.")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))