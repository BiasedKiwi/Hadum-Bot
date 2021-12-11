import argparse
import configparser
import logging
import threading
from datetime import datetime
from importlib.metadata import version
from sys import version as py_ver

from nextcord.ext import commands
from nextcord.ext.commands.errors import CommandNotFound
from rich.console import Console

import utils

now = datetime.now()
logger = logging.getLogger("nextcord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=f"../logs/{now.strftime('%Y-%m-%d_%H-%M-%S')}.log/", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)
config = configparser.ConfigParser()
config.read("config.ini")
on_ready_mes = config.get("success_messages", "on_ready")
on_connect_mes = config.get("success_messages", "on_connect")
on_disconnect_mes = config.get("success_messages", "on_disconnect")
max_shards= config.getint("config", "max_shards")
strip_prefix = config.getboolean("config", "strip_after_prefix")
load_exts = config.getboolean("extensions", "load_extensions")
prefix_items = dict(config.items("prefix"))
prefix = list(prefix_items.values())

client  = commands.AutoShardedBot(command_prefix=prefix,
                       case_insensitive=True,
                       strip_after_prefix=strip_prefix,
                       help_command=None)
parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", dest="quiet", action="store_true", help="suppress output")
parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Show maximum output")
parser.add_argument("-V", "--version", dest="version", action="store_true", help="Output version info")
args = parser.parse_args()

console = Console()


def main():
    @client.event
    async def on_ready():
        console.log(on_ready_mes)
        if args.verbose:
            console.print("""[bright_black]\nERRORS WILL BE LOGGED HERE\n""", justify="center")
        
        
    @client.event
    async def on_connect():
        console.log(on_connect_mes)
        

    @client.event
    async def on_disconnect():
        console.log(on_disconnect_mes)
        
    @client.event
    async def on_command_error(ctx: commands.Context, error: commands.CommandError):
        """Handles all errors unhandled by cog

        Args:
            ctx (commands.Context): Command Context
            error (commands.CommandError): Error raised
        """
        cog = ctx.cog

        if hasattr(ctx.command, 'on_error'):
                return
        if cog and cog._get_overridden_method(cog.cog_command_error) is not None:
            return
        elif isinstance(error, NotImplementedError):
            await ctx.channel.send("Command not yet implemented.")
        elif isinstance(error, CommandNotFound):
            pass
        elif args.verbose:
            console.log(f"Unhandled Exception: {error}")
            


    t1 = threading.Thread(target=utils.initial_load(debug=args.quiet))
    t1.start()
    if load_exts:
        utils.load_cogs(client, file_extension=".py", cog_path="extensions", include_folders=True)

    try:
        client.run(utils.get_token("../../.env", ask_for_token=True))
    except TypeError:
        raise KeyError ("Ouch! It seems as if you passed an invalid token! Remember to store it in the 'TOKEN' variable of your .env file")
    t1.join()
    

if __name__ == "__main__":
    if args.version:  # Check for flags
        to_print = ["nextcord", "rich", "psutil"]
        console.print("bot: " + config.get("config", "bot_version"))
        for i in to_print:
            console.print(i + ": " + version(i))
        console.print("python: " + py_ver)
    else:
        main()
