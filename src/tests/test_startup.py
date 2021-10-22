import os
import unittest

from discord.ext import commands
from utils import startup

client = commands.Bot(command_prefix="", help_command=None)


class TestStartup(unittest.TestCase):
    def test_load_cogs_recursively(self):
        self.assertEqual(startup.load_cogs(client, include_folders=True), 0)
        
    def test_initial_load_with_debug_off(self):
        self.assertEqual(startup.initial_load(debug=False), 0)
        
    def test_initial_load_with_debug_on(self):
        self.assertEqual(startup.initial_load(debug=True), 0)
        
    def test_get_token(self):
        try:
            with open("./.env", "x") as outfile:
                print("sample .env file created")
                outfile.seek(0)
                outfile.write("TOKEN=12345")
        except FileExistsError:
            pass
        self.assertNotEqual(startup.get_token(file="./.env",ask_for_token=False), -1)
        if os.path.exists("./.env"):
            os.remove("./.env")


if __name__ == "__main__":
    unittest.main()
    