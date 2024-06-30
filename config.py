"""
Configuration module for the bot status checker.

This module loads environment variables required for the bot to function,
such as bot token, API ID and API HASH.
It also sets up the necessary configuration settings.
"""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(getenv("26021206", "0"))
    API_HASH = getenv("cd9a575457394f081ac8ca5a82673a16")
    BOT_TOKEN = getenv("6511014299:AAEIdpFOs818gKhuLYMVeFnd5zSWTGkZmM8")
    
