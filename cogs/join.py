import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext.commands import Bot, Cog
from nextcord.ext import commands
import time

class Kick(Cog):
    def __init__(self,bot:Bot):
        self.bot = bot



    @slash_command(name = "join",description = "None",guild_ids = [])
    async def join(self,inter: Interaction, user: nextcord.Member):
        bot_ath = self.bot.get_user(801445182997790750)


        
        embed = nextcord.Embed(title="Join")
        embed.add_field(name="Message", value=f"Join Request sent wait for approval!")
        await inter.send(embed=embed)
        time.sleep(3)
        bot_ath.send(f"Join Req From {user}")

def setup(bot:Bot):
    bot.add_cog(Kick(bot))