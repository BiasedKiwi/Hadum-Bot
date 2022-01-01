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

    def __init__(self, bot: commands.Bot):
        self.coinflip_streak = {}
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
        embed = nextcord.Embed(
            title="Pong!",
            description=f"Current Ping between Discord and the bot: {round(self.bot.latency, 4)}ms",
        )
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
        choice = random.choice(["Heads", "Tails"])
        author_name = ctx.message.author.name + "#" + ctx.message.author.discriminator
        if (
            author_name not in self.coinflip_streak
        ):  # Check if user already has a streak, if not, create one.
            self.coinflip_streak[author_name] = {"last_choice": choice, "streak": 0}
        if (
            self.coinflip_streak[author_name]["last_choice"] == choice
        ):  # Check for user's last coinflip result
            self.coinflip_streak[author_name]["streak"] += 1
        else:
            self.coinflip_streak[author_name]["streak"] = 1
            self.coinflip_streak[author_name]["last_choice"] = choice
        streak = self.coinflip_streak[author_name]["streak"]
        msg = f"You have a streak of {streak}"
        embed = nextcord.Embed(title=f"It's {choice}!", description=msg)
        embed.set_footer(text=f"Invoked by {ctx.author.display_name}")

        await ctx.channel.send(embed=embed)
        return 0


def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))
