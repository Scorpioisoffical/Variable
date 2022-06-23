import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext.commands import Bot, Cog

class Say(Cog):
    def __init__(self,bot:Bot):
        self.bot = bot

    @slash_command(name = "say",description = "Says A message",guild_ids = [])
    async def say(self,inter: Interaction, question):
        await inter.send(f"{question}")

def setup(bot:Bot):
    bot.add_cog(Say(bot))