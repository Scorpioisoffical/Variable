import os
import nextcord
from nextcord.ext import commands

TESTING_GUILD_ID = [981871464556945419,982118415525376050]  
# Array of Guild IDs
# goodbye commands 
intents = nextcord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=".",messages=True, guilds=True, intents=intents)

@bot.event
async def on_ready():
    print(f"Signed in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author != bot.user:
        print(f'(#{message.channel}) {message.author}: {message.content}')
        
@bot.event
async def on_message_delete(message):
    print(f'User {message.author} has deleted "{message.content}"')

@bot.event
async def on_message_edit(before, after):
    print(f'User {before.author} has edited "{before.content}" to "{after.content}"')

for cog_name in os.listdir("./cogs/"):
    try:
        if cog_name.endswith(".py"):
            bot.load_extension(f"cogs.{cog_name[:-3]}")
            print(f"{cog_name} was loaded")
    except:
        print(f"{cog_name} was not loaded")


with open("token.txt","r") as f:
    token = f.read()

bot.run(token)