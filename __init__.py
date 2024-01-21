from pyrogram import Client

BOT_TOKEN = "6819897576:AAGa59y6l_vuqndIxXhHPMuEDcfEIMy-GUA"
API_ID = 27169529
API_HASH = "5d67602a4e0bbfabe669c0febeaf63b6"

app = Client(
    "my_app",
    api_id = API_ID,
    api_hash = API_HASH, 
    bot_token = BOT_TOKEN,
    plugins = {"root": "raidbot.modules"}
)