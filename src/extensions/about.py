import configparser
import datetime
import time

import nextcord
from nextcord.ext import commands
from rich.console import Console

console = Console()
uptime = 0
config = configparser.ConfigParser()
config.read("config.ini")


class About(commands.Cog):
    def __init__(self, bot: commands.Bot):
        """The About Command."""
        self.bot = bot
        self.start_time = time.time()

    @commands.Cog.listener()
    async def on_ready(self):
        console.log(__name__.replace("extensions.", "") + "Cog Online")

    @commands.command(name="about")
    async def about(self, ctx: commands.Context):
        """Send info about the bot

        Args:
            ctx (commands.Context): Command context
        """
        embed = nextcord.Embed(title="About this bot.")
        embed.add_field(name="Version", value=config.get("config", "bot_version"))
        embed.add_field(
            name="Uptime",
            value=f"The bot has been up for: {datetime.timedelta(seconds=self.start_time - time.time())}",
        )
        await ctx.channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(About(bot))
