from utils import startup
import unittest
from discord.ext import commands


client = commands.Bot(command_prefix="", help_command=None)


class TestStartup(unittest.TestCase): 
    def test_load_cogs(self):
        self.assertEqual(startup.load_cogs(client, include_folders=True), 0)
        
    def test_initial_load_with_debug_off(self):
        self.assertEqual(startup.initial_load(debug=False), 0)
        
    def test_initial_load_with_debug_on(self):
        self.assertEqual(startup.initial_load(debug=True), 0)
        
        
if __name__ == "__main__":
    unittest.main()
    