from pyrogram import Client

api_id = "API_ID
api_hash = "API_HASH"
bot_token = "BOT_TOKEN"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

from pyrogram import Client

app = Client()
app.run()
