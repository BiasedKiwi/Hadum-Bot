import configparser

import psutil
from nextcord.ext import commands
from nextcord.ext.tasks import loop
from rich.console import Console

console = Console()
config = configparser.ConfigParser()
config.read("config.ini")
on = config.getboolean("config", "background_tasks")

class BackgroundTasks(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        console.log(__name__.strip("extensions.") + " Cog Online")
        
        if on:
            self.get_info.start()

    @loop(seconds=15)
    async def get_info(self):
        latency = round(self.bot.latency, 4)
        cpu_usage = psutil.cpu_percent(4)
        ram_percent = psutil.virtual_memory()[2]
        
        console.rule("Status Report")
        console.print(f"Latency: {latency}ms")
        console.print(f"CPU Usage %: {cpu_usage}")
        console.print(f"RAM Usage %: {ram_percent}")
        
    @get_info.before_loop
    async def _get_info(self):
        await self.bot.wait_until_ready()
        

def setup(bot:commands.Bot):
    bot.add_cog(BackgroundTasks(bot))
