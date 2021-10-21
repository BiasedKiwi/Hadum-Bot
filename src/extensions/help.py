import nextcord
from nextcord.ext import commands
from rich.console import Console


console = Console()


class Help(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        console.log(__name__.strip("extensions.") + " Cog Online")
        
        
    @commands.group(name="help", aliases=["cmds", "commands"])
    async def help_(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            embed = nextcord.Embed(title="Hadum Commands")
            embed.add_field(name="Moderation", value="Run `h.help moderation` to see commands.", inline=True)
            embed.add_field(name="Miscellaneous", value="Run `h.help misc` to see commands.", inline=True)
            await ctx.channel.send(embed=embed)
            
            return 0
        
    
    @help_.command(name="moderation")
    async def moderation(self, ctx: commands.Context):
        embed = nextcord.Embed(title="Moderation Commands")
        embed.add_field(name="ban", value="Permanently Ban a user. Usage: `h.ban [USER] [REASON]`", inline=False)
        embed.add_field(name="kick", value="Kick a user. Usage: `h.kick [USER] [REASON]`", inline=False)
        embed.add_field(name="masskick", value="Kick multiple users simultaneously. Usage: `h.masskick [USERS] [REASON]`", inline=False)
        await ctx.channel.send(embed=embed)
        
        return 0
    
    
    @help_.command(name="misc")
    async def misc(self, ctx: commands.Context):
        embed = nextcord.Embed(title="Miscellaneous Commands")
        embed.add_field(name="ping", value="Get the latency between the bot and Discord Servers. Usage: `h.ping`")
        embed.add_field(name="coinflip", value="Flip a coin! Usage: `h.coinflip`")
        await ctx.channel.send(embed=embed)
        
        return 0


def setup(bot:commands.Bot):
    bot.add_cog(Help(bot))