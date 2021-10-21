import asyncio
import json

import nextcord
import wikipedia
from nextcord.ext import commands
from rich.console import Console

console = Console()

class Listeners(commands.Cog):
    """A Collection of listeners

    Args:
        commands (module): Parent Class
    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        console.log(__name__.strip("extensions.") + " Cog Online")


def setup(bot:commands.Bot):
    bot.add_cog(Listeners(bot))
