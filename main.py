import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Charger les variables d'environnement (.env si local)
load_dotenv()

# Récupérer le token depuis la variable d’environnement
TOKEN = os.getenv("DISCORD_TOKEN")

# Sécurité : vérifie que le token est bien présent
if TOKEN is None:
    raise ValueError("❌ Le token DISCORD_TOKEN n'est pas défini dans les variables d'environnement.")

# Définir les intentions du bot
intents = discord.Intents.default()
intents.message_content = True

# Création du bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} est connecté à Discord.")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong !")

# Lancer le bot
bot.run(TOKEN)
