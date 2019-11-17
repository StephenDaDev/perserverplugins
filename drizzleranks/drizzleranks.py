import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class drizzleRanks(commands.Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["groupranks"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def ranks(self, ctx):
        """Send the ranks of Drizzle Hotels"""
        embed = discord.Embed(
            title="Drizzle Hotel Ranks"
        )
        embed.description = """
                > Chairperson
                
                > Vice-Chairperson
                
                > Executive
                
                > Public Relations Officer
                
                > Board of Directors
                
                > Shift Manager
                
                > Supervisor
                
                > Security
                
                > Receptionist
                
                > Trainee
            """
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(drizzleRanks(bot))
