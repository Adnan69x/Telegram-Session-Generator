from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv(""))
API_HASH = getenv("")

BOT_TOKEN = getenv("")
MONGO_DB_URI = getenv("", None)
OWNER_ID = int(getenv("ONWER_ID", 5041639607))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ADNANiTUNE")
