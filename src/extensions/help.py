import nextcord
from nextcord.ext import commands
from rich.console import Console


console = Console()


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        """Help command

        Args:
            bot (commands.Bot): Bot instance
        """
        self.bot = bot
        console.log(__name__.strip("extensions.") + " Cog Online")

    @commands.group(name="help", aliases=["cmds", "commands"])
    async def help_(self, ctx: commands.Context):
        """Help command

        Args:
            ctx (commands.Context): Command context
        """

        def gen_field(name, value):
            return embed.add_field(name=name, value=value, inline=True)

        if ctx.invoked_subcommand is None:
            embed = nextcord.Embed(title="Hadum Commands")
            gen_field("Moderation", "Run `h.help moderation` to see commands.")
            gen_field("Miscellaneous", "Run `h.help misc` to see commands.")
            gen_field("Reddit", "Run `h.help reddit` to see commands.")
            await ctx.channel.send(embed=embed)

            return 0

    @help_.command(name="moderation")
    async def moderation(self, ctx: commands.Context):
        """Moderation section of the help commands

        Args:
            ctx (commands.Context): Command context

        Returns:
            Int: Exit code
        """
        embed = nextcord.Embed(title="Moderation Commands")
        embed.add_field(
            name="ban",
            value="Permanently Ban a user.\n Usage: `h.ban [USER] [REASON]`",
            inline=False,
        )
        embed.add_field(
            name="kick",
            value="Kick a user.\n Usage: `h.kick [USER] [REASON]`",
            inline=False,
        )
        embed.add_field(
            name="masskick",
            value="Kick multiple users simultaneously.\n Usage: `h.masskick [USERS] [REASON]`",
            inline=False,
        )
        await ctx.channel.send(embed=embed)

        return 0

    @help_.command(name="misc")
    async def misc(self, ctx: commands.Context):
        """Misc section of the help command

        Args:
            ctx (commands.Context): Command context

        Returns:
            Int: Exit code
        """
        embed = nextcord.Embed(title="Miscellaneous Commands")
        embed.add_field(
            name="ping",
            value="Get the latency between the bot and Discord Servers.\n Usage: `h.ping`",
            inline=False,
        )
        embed.add_field(
            name="coinflip", value="Flip a coin!\n Usage: `h.coinflip`", inline=False
        )
        await ctx.channel.send(embed=embed)

        return 0

    @help_.command(name="reddit")
    async def reddit_(self, ctx: commands.Context):
        """Reddit section of the help command

        Args:
            ctx (commands.Context): Command context

        Returns:
            Int: Exit code
        """
        embed = nextcord.Embed(title="Miscellaneous Commands")
        embed.add_field(
            name="meme", value="Get a random meme!\n Usage: `h.meme`", inline=False
        )
        embed.add_field(
            name="reddit",
            value="Get a random post from the subreddit entered!\n Usage: `h.reddit [SUBREDDIT]`",
            inline=False,
        )
        embed.add_field(
            name="automeme",
            value="Get memes without even asking for them!\n Usage: `h.autopostmeme [N_OF_MEMES]`",
            inline=False,
        )
        await ctx.channel.send(embed=embed)

        return 0


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
