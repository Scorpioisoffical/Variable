import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext.commands import Bot, Cog

class Warn(Cog):
    def __init__(self,bot:Bot):
        self.bot = bot

    @slash_command(name = "warn",description = "Warns A User",guild_ids = [])
    async def warn(self,inter: Interaction, member: nextcord.Member, reason):
        embed = nextcord.Embed(title="Warn")
        embed.add_field(name="Message", value=f"User **{member}** Has been warned for **{reason}**")
        await inter.send(embed=embed)

def setup(bot:Bot):
    bot.add_cog(Warn(bot))