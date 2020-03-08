from redbot.core import commands

class NoobshackAdmin(commands.Cog):
    """Noobshack administrative tooling."""

    # gameserver information
    @commands.command()
    async def get_gameserver_gce(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")

    @commands.command()
    async def get_gameserver_battlemetrics(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")

    @commands.command()
    async def gameserver_information_list(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")

    # community feedback
    @commands.command()
    async def feedback(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")

    # noobshack points
    @commands.command()
    async def get_points(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")

    @commands.command()
    async def set_points(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")

    @commands.command()
    async def list_points(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")

    @commands.command()
    async def daily_quest(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")

    @commands.command()
    async def leaderboards(self, ctx):
        """placeholder!"""
        await ctx.send("placeholder")
