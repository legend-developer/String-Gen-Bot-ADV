from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN" , "7403775017:AAGeSpSdZG7vq044xma9X5fRowbycmDBrqs")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 5337517666))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+cOFKKAr4_DVjMjE9")
