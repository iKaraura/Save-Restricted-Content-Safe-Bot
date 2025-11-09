# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25271265"))
API_HASH = getenv("API_HASH", "2b444dd24960df5a274aea08bf62cf8e")
BOT_TOKEN = getenv("BOT_TOKEN", "7863778055:AAGWlwPKwSut_fcUjzsYkrBxhL0c_6As7rU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5765708156").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://iamrohityadavx:hDtdzzDL5Eu0f0PS@cluster0.zn0g3jr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003151011036")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002996562355"))
