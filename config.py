# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25265"))
API_HASH = getenv("API_HASH", "2b444aea08bf62cf8e")
BOT_TOKEN = getenv("BOT_TOKEN", "7wPKwSut_fcUjzsL0c_6As7rU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "08156").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+avx:hDtdzzD0PS@cluster0.zn0g3jr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003111036")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002996355"))
