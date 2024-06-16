from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("27913018"))
API_HASH = getenv("04e2f4e414cdabe52ad985adaa6cfe09")

BOT_TOKEN = getenv("7198675016:AAEhGG7AedNnEHXY9J9kceXjtmkMsjBWwdU")
MONGO_DB_URI = getenv("mongodb+srv://Farhan:FARHAN@cluster0.uqsweah.mongodb.net/?retryWrites=true&w=majority", None)
OWNER_ID = int(getenv("ONWER_ID", 5041639607))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ADNANiTUNE")
