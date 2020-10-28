import logging

import requests
from redbot.core import Config, commands
from redbot.core.bot import Red

log = logging.getLogger("red.wizworm_cogs.gaze")

class Gaze(commands.Cog):
    """
    Query each endpoint of noobshack gaze API.

    gaze.reulan.com/
    - /gameservers
    - /gameservers/:unique
    """

    gaze_base_url = "gaze.reulan.com"
    gaze_route = "/gameservers"

    def print_request_data(r):
        print("Status Code: " + r.status_code + "\n")
        print("Text: " + r.text + "\n")
        print("JSON: " + r.json() + "\n")

    # gameserver information
    @commands.command()
    async def get_index(self, ctx):
        """Returns the hostname"""
        r = requests.get(gaze_base_url)
        print_request_data(r)
        await ctx.send(r.text)

    @commands.command()
    async def get_gameserver_list(self, ctx):
        """placeholder!"""
        r = requests.get(gaze_base_url + gaze_route)
        print_request_data(r)
        await ctx.send(r.text)

    @commands.command()
    async def get_gameserver(self, ctx):
        """placeholder!"""
        game = "mordhau"
        r = requests.get(gaze_base_url + gaze_route + "/" + game)
        print_request_data(r)
        await ctx.send(r.text)
