import os
import random
import configparser

import nextcord
import asyncpraw
from dotenv import load_dotenv
from nextcord.ext import commands
from rich.console import Console

console = Console()
config = configparser.ConfigParser()
config.read("config.ini")
load_dotenv()


class Reddit(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=f"dankmemes scraper v0.4 by u/{os.getenv('REDDIT_USER_AGENT')}",
        )
        console.log(__name__.strip("extensions.") + " Cog Online")

    @commands.command(name="meme")
    async def meme(self, ctx: commands.Context):
        subreddit = await self.reddit.subreddit(config.get("reddit", "meme_sub"))
        meme = await subreddit.random()
        
        embed = nextcord.Embed(title=meme.title)
        embed.set_image(url=meme.url)
        await ctx.channel.send(embed=embed)


    @commands.command(name="reddit")
    async def reddit(self, ctx: commands.Context, sub: str):
        subreddit = await self.reddit.subreddit(sub.strip("r/"))
        
        post = await subreddit.random()
        if post.selftext == "":  # If the post contains no text, then post the image associated with it.
            embed = nextcord.Embed(title=post.title, url=post.url)
            embed.set_image(url=post.url)
        else:
            embed = nextcord.Embed(title=post.title, description=post.selftext, url=post.url)
            
        embed.set_footer(text=f"Posted in r/{subreddit}")
        await ctx.channel.send(embed=embed)
        
        
def setup(bot:commands.Bot):
    bot.add_cog(Reddit(bot))
