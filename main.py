import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} est connecté à Discord.")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong !")

bot.run(TOKEN)
