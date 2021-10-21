import random

import nextcord
from nextcord.ext import commands
from rich.console import Console

console = Console()


class Miscellaneous(commands.Cog):
    """Miscellanous Cog

    Args:
        commands (module): Parent Class
    """
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        console.log(__name__.strip("extensions.") + " Cog Online")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Return Latency in milliseconds

        Args:
            ctx (commands.Context): Command Context

        Returns:
            Int: Exit Code
        """
        embed = nextcord.Embed(title="Pong!", description=f"Current Ping between Discord and the bot: {round(self.bot.latency, 4)}ms")
        await ctx.channel.send(embed=embed)
        
        return 0
    
    
    @commands.command(name="coinflip")
    async def coinflip(self, ctx: commands.Context):
        """Randomly chooses between heads and tails and returns that value to the user.

        Args:
            ctx (commands.Context): Command Context

        Returns:
            Int: Exit Code
        """
        embed = nextcord.Embed(title=f"It's {random.choice(['Heads', 'Tails'])}!")
        embed.set_footer(text=f"Invoked by {ctx.author.display_name}")
        
        await ctx.channel.send(embed=embed)
        return 0


def setup(bot:commands.Bot):
    bot.add_cog(Miscellaneous(bot))
    