import requests

from redbot.core import commands

class Gaze(commands.Cog):
    """Query each endpoint of noobshack gaze API."""

    gaze_base_url = "gaze.reulan.com"
    gaze_route = "/gameservers"

    # gameserver information
    @commands.command()
    async def get_index(self, ctx):
        """Returns the hostname"""
        r = requests.get(gaze_base_url)
        print("Status Code: " + r.status_code + "\n")
        print("Text: " + r.text + "\n")
        print("JSON: " + r.json() + "\n")
        await ctx.send(r.text)

    @commands.command()
    async def get_gameserver_list(self, ctx):
        """placeholder!"""
        r = requests.get(gaze_base_url + gaze_route)
        print("Status Code: " + r.status_code + "\n")
        print("Text: " + r.text + "\n")
        print("JSON: " + r.json() + "\n")
        await ctx.send(r.text)

    """
    @commands.command()
    async def get_gameserver(self, ctx, game):
        r = requests.get(gaze_base_url + gaze_route + "/" + game)
        print("Status Code: " + r.status_code + "\n")
        print("Text: " + r.text + "\n")
        print("JSON: " + r.json() + "\n")
        await ctx.send("")
    """
