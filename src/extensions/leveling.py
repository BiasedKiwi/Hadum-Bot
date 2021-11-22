import asyncio

import nextcord
import aiosqlite
from aiosqlite.core import Connection, Cursor
from nextcord.ext import commands
from nextcord.ext.tasks import loop
from rich.console import Console


console = Console()
connection: Connection
cursor: Cursor


class Leveling(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        console.log(__name__.strip("extensions.") + " Cog Online")
        self.commit_db.start()
        
    @loop(seconds=10)
    async def commit_db(self):
        global connection
        global cursor
        first_run = True
        if first_run:
            connection = await aiosqlite.connect("./databases/levels.db")
            cursor = await connection.cursor()
            first_run = False
            
        await connection.commit()
        
    @commands.command(name="level", aliases=["rank"])
    async def level(self, ctx: commands.Context):
        i = await cursor.execute("SELECT * FROM user")
        rows = await i.fetchall()
        for _i in rows:
            await ctx.channel.send(_i)
        
        
def setup(bot:commands.Bot):
    bot.add_cog(Leveling(bot))
