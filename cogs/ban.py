import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext.commands import Bot, Cog
from nextcord.ext import commands

class Ban(Cog):
    def __init__(self,bot:Bot):
        self.bot = bot

    @slash_command(name = "ban",description = "bans An User",guild_ids = [])
    @commands.has_permissions(ban_members=True)
    async def ban(self,inter: Interaction, member: nextcord.Member, reason):
        if member == None:
         await inter.send("Please enter a user!")
         return



        await member.ban(reason=reason)
        embed = nextcord.Embed(title="Ban")
        embed.add_field(name="Message", value=f"User **{member}** Has been banned for **{reason}**")
        await inter.send(embed=embed)

def setup(bot:Bot):
    bot.add_cog(Ban(bot))