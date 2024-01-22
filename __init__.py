import os

from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
if os.path.exists("local.env"):
    load_dotenv("local.env")

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

app = Client(
    "my_app",
    api_id = API_ID,
    api_hash = API_HASH, 
    bot_token = BOT_TOKEN,
    plugins = {"root": "Replyraid.modules"}
)
