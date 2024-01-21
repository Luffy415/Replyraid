from pyrogram import  filters
from .. import app

@app.on_message(filters.command("alive"))
async def alive(bot, m):
    await m.reply("i am alive")