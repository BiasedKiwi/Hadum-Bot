from nextcord.ext import commands
from rich.console import Console


console = Console()


class Staff(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        console.log(__name__.replace("extensions.", "") + "Cog Online")

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
