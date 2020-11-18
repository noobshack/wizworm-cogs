import logging

from redbot.core import Config, commands
from redbot.core.bot import Red

import aiohttp
import requests

log = logging.getLogger("red.wizworm_cogs.gaze")

class Gaze(commands.Cog):
    """
    Query each endpoint of noobshack gaze API.

    gaze.reulan.com/
    - /gameservers
    - /gameservers/:unique
    - /gameservers/minecraft
    """

    # Setup vars then initialize bot
    gaze_base_url = "gaze.reulan.com"
    gaze_route = "/gameservers"

    def __init__(self, bot):
        self.bot = bot

    # gameserver information
    @commands.command()
    async def get_index(self, ctx):
        """Returns the hostname"""
        async with aiohttp.ClientSession() as session:
            async with session.get(gaze_base_url) as response:
                gsinfo = await response.text
                await ctx.send(gsinfo)

    @commands.command()
    async def get_gameserver_list(self, ctx):
        """Print list of active gameservers"""
        async with aiohttp.ClientSession() as session:
            async with session.get(gaze_base_url + gaze_route) as response:
                gsinfo = await response.text
                await ctx.send(gsinfo)

    @commands.command()
    async def get_gameserver(self, ctx, game):
        """For a given gameserver, return game-specific formatting"""
        async with aiohttp.ClientSession() as session:
            async with session.get(gaze_base_url + gaze_route + game) as response:
                gsinfo = await response.json()
                await ctx.send(gsinfo)

        if gsinfo['Response'] == "False" or gsinfo['Response'] == "Not Found":
            await ctx.send("Unable to retrieve valid response from gaze.")
            return

if __name__ == "__main__":
    gaze_base_url = "https://gaze.reulan.com"
    gaze_route = "/gameservers"
    mc_route = "/minecraft"
    mc_url = gaze_base_url + gaze_route + mc_route

    gaze = Gaze("minecraft")
    # Parse minecraft stats
    #r = requests.get(mc_url)
    #print(r.json())
