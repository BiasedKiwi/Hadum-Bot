import nextcord
from nextcord.ext import commands
from nextcord.ext.tasks import loop
from rich.console import Console
import datetime

console = Console()
uptime = 0

class About(commands.Cog):
    def __init__(self, bot: commands.Bot):
        """The About Command."""
        self.bot = bot
        console.log(__name__.strip("extensions.") + " Cog Online")
        self.get_uptime.start()

    @commands.command(name="about")
    async def about(self, ctx: commands.Context):
        embed = nextcord.Embed(title="About this bot.")
        embed.add_field(name="Version", value="v0.1.0 (c3b315e/master)")
        embed.add_field(name="Uptime", value=f"The bot has been up for: {datetime.timedelta(seconds=uptime)}")
        await ctx.channel.send(embed=embed)
        
    @loop(seconds=1)
    async def get_uptime(self):
        global uptime
        uptime += 1


def setup(bot:commands.Bot):
    bot.add_cog(About(bot))
