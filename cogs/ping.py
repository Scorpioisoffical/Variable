import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext.commands import Bot, Cog

class Ping(Cog):
    def __init__(self,bot:Bot):
        self.bot = bot

    @slash_command(name = "ping",description = "shows the Lattency/ping of the bot",guild_ids = [])
    async def ping(self,inter: Interaction):
        await inter.send(f"Pong! {round(self.bot.latency * 1000)}ms :ping_pong: ")

def setup(bot:Bot):
    bot.add_cog(Ping(bot))
