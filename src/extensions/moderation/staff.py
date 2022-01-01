import nextcord
from nextcord.ext import commands
from rich.console import Console


console = Console()


class Staff(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        console.log(__name__.strip("extensions.") + " Cog online")

    @commands.group(name="staff")
    async def staff(self, ctx: commands.Context):
        """Placeholder for staff command

        Args:
            ctx (command.Context): Command Context

        Raises:
            NotImplementedError: Error Raised
        """
        raise NotImplementedError


def setup(bot: commands.Bot):
    bot.add_cog(Staff(bot))
