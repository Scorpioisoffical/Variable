import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext.commands import Bot, Cog
from nextcord.ext import commands

class Kick(Cog):
    def __init__(self,bot:Bot):
        self.bot = bot

    @slash_command(name = "kick",description = "Kicks An User",guild_ids = [])
    @commands.has_permissions(kick_members=True)
    async def kick(self,inter: Interaction, member: nextcord.Member, reason):
        if member == None:
         await inter.send("Please enter a user!")
         return



        await member.kick(reason=reason)
        embed = nextcord.Embed(title="Kick")
        embed.add_field(name="Message", value=f"User **{member}** Has been kicked for **{reason}**")
        await inter.send(embed=embed)

def setup(bot:Bot):
    bot.add_cog(Kick(bot))