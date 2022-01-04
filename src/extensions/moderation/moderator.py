import asyncio
import random

import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import errors
from nextcord.ext.commands.errors import BadArgument, MissingPermissions
from rich.console import Console

console = Console()


class ConfirmButton(nextcord.ui.View):
    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.red)
    async def confirm(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.green)
    async def cancel(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        self.value = False
        self.stop()


class Moderator(commands.Cog):
    """Set of Moderator commands.

    Args:
        commands (module): Parent Class
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.warning_messages = ["Hold up!", "Wait!", "Are you sure about this?"]
        console.log(__name__.strip("extensions.") + " Cog Online")

    @commands.command(name="kick", aliases=["yank"])
    @commands.has_permissions(kick_members=True)
    async def kick(
        self, ctx: commands.Context, user: nextcord.Member = None, reason: str = None
    ):
        """Kicks a user from current guild

        Args:
            ctx (commands.Context): Command Context
            user (nextcord.member): User(s) to kick
            reason (str, optional): Reason for kick. Defaults to None.

        Returns:
            Int: Exit Code
        """
        if reason is None:
            reason = "Being dumb"
        if user is None:
            await ctx.channel.send("You need to mention someone to kick!")
            return 0

        try:
            await user.kick(
                reason=f"You were kicked from **{ctx.guild}** for reason {reason}"
            )
        except nextcord.Forbidden:
            await ctx.channel.send(
                f"Oops! I couldn't kick **{user}**. Please make sure he isn't a moderator."
            )
            return -1

        await ctx.channel.send(
            f"**{user}** was successfully kicked from **{ctx.guild.name}**"
        )
        return 0

    @commands.command(name="masskick", aliases=["massyank"])
    @commands.has_permissions(kick_members=True)
    async def masskick(self, ctx: commands.Context, *args: nextcord.Member):
        """Kicks multiple users from a guild at the same time

        Args:
            ctx (commands.Context): Command Context
            reason (str, optional): Ban reason. Defaults to None.

        Returns:
            int: exit code
        """
        if not args:  # Check if no users were mentionned.
            await ctx.channel.send("You need to specify someone to kick!")
            return

        for item in args:  # Kick users
            try:
                await item.kick(reason=f"You were kicked from **{ctx.guild}**")
            except nextcord.Forbidden:
                await ctx.channel.send(
                    f"Oops! I couldn't kick **{item}** from **{ctx.guild}**"
                )

        await ctx.channel.send(
            f"**{len(args)}** Users where successfully kicked from **{ctx.guild}**."
        )
        return 0

    @masskick.error
    async def masskick_error(self, ctx: commands.Context, error):
        """Handles all errors related to the masskick command

            Args:
            ctx (commands.Context): Command Context
            error (traceback): Error

        Returns:
            Int: Exit Code
        """
        if isinstance(error, BadArgument):
            embed = nextcord.Embed(
                title="Oops!", description="Something went wrong! (BadArgument)"
            )
            await ctx.channel.send(embed=embed)
        elif isinstance(error, MissingPermissions):
            embed = nextcord.Embed(
                title="Oops!",
                description="You don't have the required permissions to run this command!",
            )
            await ctx.channel.send(embed=embed)

        return 0

    @commands.command(name="masskick", aliases=["massyank"])
    @commands.has_permissions(kick_members=True)
    async def masskick(self, ctx: commands.Context, *args: nextcord.Member):
        """Kicks multiple users from a guild at the same time.add()

        Args:
            ctx (commands.Context): Command Context
            reason (str, optional): Ban reason. Defaults to None.

        Returns:
            [type]: [description]
        """
        if not args:  # Check if no users were mentionned.
            await ctx.channel.send("You need to specify someone to kick!")
            return

        for item in args:  # Ban users
            try:
                await item.kick(reason=f"You were kicked from **{ctx.guild}**")
            except nextcord.Forbidden:
                await ctx.channel.send(
                    f"Oops! I couldn't kick **{item}** from **{ctx.guild}**"
                )

        await ctx.channel.send(
            f"**{len(args)}** Users where successfully kicked from **{ctx.guild}**."
        )
        return 0

    @masskick.error
    async def masskick_error(self, ctx: commands.Context, error):
        """Handles all errors related to the masskick command

            Args:
            ctx (commands.Context): Command Context
            error (traceback): Error

        Returns:
            Int: Exit Code
        """
        if isinstance(error, BadArgument):
            embed = nextcord.Embed(
                title="Oops!",
                description=f"Something went wrong when trying to execute {ctx.command}! (BadArgument)",
            )
            await ctx.channel.send(embed=embed)
        elif isinstance(error, MissingPermissions):
            embed = nextcord.Embed(
                title="Oops!",
                description="You don't have the required permissions to run this command!",
            )
            await ctx.channel.send(embed=embed)

        return 0

    @kick.error
    async def kick_error(self, ctx: commands.Context, error):
        """Handles all errors related to the kick command

            Args:
            ctx (commands.Context): Command Context
            error (traceback): Error

        Returns:
            Int: Exit Code
        """
        if isinstance(error, BadArgument):
            embed = nextcord.Embed(
                title="Oops!",
                description=f"Something went wrong when trying to execute {ctx.command}! (BadArgument)",
            )
            await ctx.channel.send(embed=embed)
        elif isinstance(error, MissingPermissions):
            embed = nextcord.Embed(
                title="Oops!",
                description="You don't have the required permissions to run this command!",
            )
            await ctx.channel.send(embed=embed)

        return 0

    @commands.command(name="ban", aliases=["permban"])
    @commands.has_permissions(ban_members=True)
    async def ban(
        self, ctx: commands.Context, user: nextcord.Member = None, reason: str = None
    ):
        """Permanently Ban a given user from a guild

        Args:
            ctx (commands.Context): Command Context
            user (nextcord.User, optional): User to Ban. Defaults to None.

        Returns:
            Int: Exit Code
        """
        if user is None:  # Check if no users were specified.
            await ctx.channel.send("You need to mention someone to ban!")
            return 0

        if reason is None:
            reason = "No reason specified"

        view = ConfirmButton()  # Initialize views (buttons)
        confirm_embed = nextcord.Embed(
            title=random.choice(self.warning_messages),
            description=f"You're about to ban {user} **Permanently** Are you sure?",
        )
        await ctx.channel.send(embed=confirm_embed, view=view)

        await view.wait()
        if view is None:
            await ctx.channel.send("Timed Out! Cancelling Operation...")
        elif view.value:
            try:
                await user.ban(reason=reason)
                await ctx.channel.send(f"Alright! I permanently banned {user}!")
            except nextcord.Forbidden:
                await ctx.channel.send(
                    f"Oops! I couldn't ban **{user}** Please make sure he isn't a moderator."
                )
        else:
            await ctx.channel.send("Alright! Operation Cancelled...")

        return 0

    @commands.command(name="massban")
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx: commands.Context, *args: nextcord.Member):
        view = ConfirmButton()

        if not args:
            await ctx.channel.send("You need to mention people to ban!")
            return 0
        confirm_embed = nextcord.Embed(
            title=random.choice(self.warning_messages),
            description=f"You're about to **permanently ban {len(args)}** users, are you sure?",
        )
        await ctx.channel.send(embed=confirm_embed, view=view)

        await view.wait()
        if view is None:
            await ctx.channel.send("Timed out! Cancelling Operation...")
        elif view.value:
            try:
                for item in args:
                    await item.ban()

                await ctx.channel.send(
                    f"Alright! I successfully banned **{len(args)}** Users!"
                )
            except nextcord.Forbidden:
                await ctx.channel.send(f"Oops! I couldn't ban **{item}**!")
        else:
            await ctx.channel.send("Alright! Operation Cancelled...")

    @commands.command(name="massban")
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx: commands.Context, *args: nextcord.Member):
        """Ban multiple users at the same time

        Args:
            ctx (commands.Context): Command context

        Returns:
            Int: Exit code
        """
        if len(args) == 0:  # Check if no users were specified
            await ctx.channel.send("You need to mention people to ban!")
            return 0
        confirm_embed = nextcord.Embed(
            title=random.choice(self.warning_messages),
            description=f"You're about to **permanently ban {len(args)}** users, are you sure? (Y/n)",
        )
        await ctx.channel.send(embed=confirm_embed)

        def check(m):  # Function to check if the message was the message expected
            return m.author == ctx.author and m.channel == ctx.channel

        try:  # Wait for confirmation message
            confirm_msg = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:  # Handle timeout
            termination_embed = nextcord.Embed(
                title="You took too long to respond!", description="Operation Cancelled"
            )
            await ctx.channel.send(embed=termination_embed)
            return 0

        if confirm_msg.content.lower() == "y" or confirm_msg.content.lower() == "yes":
            try:
                for item in args:  # Ban users
                    item.ban()
            except nextcord.Forbidden:
                await ctx.channel.send(f"Oops! I couldn't ban **{item}**!")
        else:
            await ctx.channel.send(f"Alright! Operation Cancelled.")
            return

    @ban.error
    async def ban_error(self, ctx: commands.Context, error):
        """Handle errors related to the ban command.

        Args:
            ctx (commands.Context): Command Context
            error (Exception): error

        Returns:
            Int: Exit code
        """
        if isinstance(error, MissingPermissions):
            embed = nextcord.Embed(
                title="Hold up!",
                description="You don't have the permissions to do that!",
            )
            await ctx.channel.send(embed=embed)

            return 0

    @commands.command(name="purge", aliases=["delete", "clear"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx: commands.Context, num: int = None):
        """Bulk delete messages

        Args:
            ctx (commands.Context): Command context
            num (int, optional): Number of messages to delete. Defaults to None.

        Returns:
            Int: Exit code
        """
        if num is None:
            await ctx.channel.send(
                "You need to specify a number of messages to delete!"
            )
            return 0
        try:
            await ctx.message.channel.purge(limit=num)
            await ctx.channel.send(
                f"Successfully Deleted **{num}** Messages!", delete_after=5
            )

            return 0
        except nextcord.Forbidden:
            await ctx.channel.send(
                "Sorry! I don't have enough permissions to delete messages!"
            )
            return -1

    @purge.error
    async def purge_error(self, ctx: commands.Context, error):
        """Handle errors related to the purge error

        Args:
            ctx (commands.Context): Command Context
            error (Exception): Error
        """
        if isinstance(error, MissingPermissions):
            embed = nextcord.Embed(
                title="Hold Up!",
                description="You don't have enough permissions to delete messages!",
            )
            await ctx.channel.send(embed=embed)
        if isinstance(error, TypeError):
            await ctx.channel.send("Please specify a **number** of messages to delete.")


def setup(bot: commands.Bot):
    bot.add_cog(Moderator(bot))
