from . import app
from pyrogram import idle

async def main():
	print("Staring...")
	await app.start()
	print("Started")
	await app.send_message(6277256830, "started master")
	await idle()
	print("Stopping...")
	await app.stop()
	print("Stopped")

app.run(main())