from nextcord.ext import commands
from rich.console import Console

console = Console()


class Administrator(commands.Cog):
    def __init__(self, bot: commands.Bot):
        """A collection of Administrator commands (temporary)

        Args:
            bot (commands.Bot): Parent class
        """
        self.bot = bot
        self.warning_messages = ["Hold up!", "Wait!", "Are you sure about this?"]
        console.log(__name__.strip("extensions.") + " Cog Online")


def setup(bot: commands.Bot):
    bot.add_cog(Administrator(bot))
