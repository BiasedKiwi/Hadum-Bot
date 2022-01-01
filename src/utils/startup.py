import configparser
import os
import time

import requests
from dotenv import load_dotenv
from nextcord.ext import commands
from nextcord.ext.commands import AutoShardedBot
from rich.console import Console

from utils.exceptions import StartupError


config = configparser.ConfigParser()
config.read("config.ini")
console = Console()


def initial_load(*, debug: bool = False, test_mode: bool = False) -> int:
    """
    Starts the animation bar and loads the big 'Hadum' ASCII Art text.
    """
    if debug:
        return 0
    to_anim = [
        "'##::::'##::::'###::::'########::'##::::'##:'##::::'##:",
        " ##:::: ##:::'## ##::: ##.... ##: ##:::: ##: ###::'###:",
        " ##:::: ##::'##:. ##:: ##:::: ##: ##:::: ##: ####'####:",
        " #########:'##:::. ##: ##:::: ##: ##:::: ##: ## ### ##:",
        " ##.... ##: #########: ##:::: ##: ##:::: ##: ##. #: ##:",
        " ##:::: ##: ##.... ##: ##:::: ##: ##:::: ##: ##:.:: ##:",
        " ##:::: ##: ##:::: ##: ########::. #######:: ##:::: ##:",
        "..:::::..::..:::::..::........::::.......:::..:::::..::\n\n",
    ]

    for item in to_anim:
        console.print(f"[green]{item}", justify="center")
        time.sleep(0.08)

    if not test_mode:
        with console.status("Checking for updates..."):
            check_for_updates()

    with console.status("Loading Extensions..."):
        time.sleep(5)

    return 0


def load_cogs(
    client_var: AutoShardedBot,
    *,
    file_extension: str = ".py",
    cog_path: str = "extensions",
    recursive: bool = False,
    debug: bool = False,
) -> int:
    """Loads all the cogs in the specified directory.

    Args:
        file_extension (str, optional): Extensions of the files to be loaded. Defaults to ".py".
        cog_path (str, optional): Directory in which the cogs are located. Defaults to "extensions".
        recursive(bool, optional): Whether to search through folders when looking for cogs. Defaults to False.
    """
    console.log("Starting to load extensions...")

    try:
        for filename in os.listdir(
            "./" + cog_path + "/"
        ):  # I know this is really messy but I'll try to clean it up later
            if filename.endswith(file_extension):
                if debug and filename == "reddit.py":  # TODO: Fix this
                    break
                else:
                    client_var.load_extension(
                        f"{cog_path}.{filename[:-len(file_extension)]}"
                    )  # this loop is stolen from youtube
            elif recursive and os.path.isdir("./" + cog_path + "/" + filename):
                cwd = os.getcwd()
                f = filename
                os.chdir("./" + cog_path + "/" + filename)
                for filename in os.listdir(os.getcwd()):
                    if filename.endswith(".py"):
                        if debug and "reddit" in filename:
                            break
                        client_var.load_extension(
                            f"{cog_path}.{f}.{filename[:-len(file_extension)]}"
                        )  # for some reason context managers don't work on os.chdir() might fix.
                os.chdir(cwd)

    except OSError as e:
        raise StartupError(e)

    return 0


def get_token(file: str = ".env", *, ask_for_token: bool = False) -> str:
    """Gets the token from an environment variable

    Args:
        file (str, optional): .env File path. Defaults to ".env".

    Returns:
        str: Token.
    """
    try:
        load_dotenv(file)
    except IOError:
        console.log(
            "[red]Could locate the .env file! Please make sure the file is named '.env' and is present in the project root folder."
        )
        return -1

    TOKEN_VAR = os.getenv("TOKEN")
    if TOKEN_VAR is None:
        console.log(
            "[red]Could not find 'TOKEN' environment variable. Please make sure the environment variable name is in ALL CAPS."
        )
        if not ask_for_token:
            return -1

        token_prompt: str = console.input("Please paste your token here: ")
        try:
            with open("../" + file, "w") as f:
                f.write("TOKEN=" + token_prompt)
                f.flush()
                TOKEN_VAR = os.getenv("TOKEN")
        except FileExistsError as e:
            console.print(f"[red]File {file} already exists")
            raise IOError(e)
        except IOError as e:
            console.print(f"[red]Could not write to '{file}'.")
            raise IOError(e)

    return TOKEN_VAR


def check_for_updates():
    if not config.getboolean("auto_update", "auto_update"):
        return
    response = requests.get(
        f"https://api.github.com/repos/{config.get('auto_update', 'owner')}/{config.get('auto_update', 'target_repo')}/releases/latest"
    )
    latest_ver = response.json()["tag_name"]
    chopped_latest = int(response.json()["tag_name"].replace("v", "").replace(".", ""))
    current_ver = config.get("config", "bot_version")
    chopped_current = int(
        config.get("config", "bot_version").replace("v", "").replace(".", "")
    )

    if latest_ver > current_ver:
        console.log(
            f"You are running an outdated bot version ({current_ver}). The latest version is {latest_ver}."
        )
        console.log(f"You can download it at {response.json()['url']}")
    elif latest_ver < current_ver:
        console.log(
            "You are running a newer bot version than the latest stable release!"
        )
    else:
        console.log("You are running the latest version of the bot!")


def main() -> None:
    console.print("###")


if __name__ == "__main__":
    main()
