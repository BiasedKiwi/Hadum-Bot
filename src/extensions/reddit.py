import configparser
import os
import random
import configparser
import random
from nextcord.ext.tasks import loop

import asyncpraw
import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands
from nextcord.ext.tasks import loop
from rich.console import Console

console = Console()
config = configparser.ConfigParser()
config.read("config.ini")
load_dotenv()
all_subs = []


class Reddit(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=f"dankmemes scraper v0.4 by u/{os.getenv('REDDIT_USER_AGENT')}",
        )
        self.get_memes.start()
        console.log(__name__.strip("extensions.") + " Cog Online")
        
    @loop(seconds=1800)
    async def get_memes(self):
        subreddit = await self.reddit.subreddit(config.get("reddit", "meme_sub"))
        top = subreddit.hot(limit=200)
        async for submission in top:
            all_subs.append(submission)

    @commands.command(name="meme")
    async def meme(self, ctx: commands.Context):
        meme = random.choice(all_subs)
        
        embed = nextcord.Embed(title=meme.title, url="https://www.reddit.com" + meme.permalink)
        embed.set_image(url=meme.url)
        embed.set_footer(text="Posted in r/dankmemes")
        await ctx.channel.send(embed=embed)

    @commands.command(name="reddit")
    async def reddit_(self, ctx: commands.Context, sub: str):
        subreddit = await self.reddit.subreddit(sub.strip("r/"))
        
        post = await subreddit.random()
        if post.over_18 and not ctx.channel.is_nsfw():
            await ctx.channel.send("Post is NSFW! Call this command in a NSFW Channel.")
            return 0
        
        if post.selftext == "":  # If the post contains no text, then post the image associated with it.
            embed = nextcord.Embed(title=post.title, url=post.url)
            embed.set_image(url=post.url)
        else:
            embed = nextcord.Embed(title=post.title, description=post.selftext, url=post.url)
            
        embed.set_footer(text=f"Posted in r/{subreddit}")
        await ctx.channel.send(embed=embed)
        
        
def setup(bot:commands.Bot):
    bot.add_cog(Reddit(bot))
