# ๐๐จ๐๐ฎ๐ฅ๐๐ฌ ๐๐ง๐ ๐๐ง๐ฏ๐ข๐ซ๐จ๐ง๐ฆ๐๐ง๐ญ๐ฌ
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# ๐๐ง๐ญ๐๐ซ๐ง๐๐ฅ ๐๐๐ซ๐ข๐๐๐ฅ๐๐ฌ (@๐ช๐๐๐_๐ฒ๐๐๐09)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# ๐๐๐ช๐ฎ๐ข๐ซ๐๐ ๐๐๐ซ๐ข๐๐๐ฅ๐๐ฌ //๐๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ @๐ช๐๐๐_๐ฒ๐๐๐09
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/c6e1041c6c9a12913f57a.png")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "โณโฃโแดตแดฌแดน โกUโธE ฦลโฆG ๐ฉ๐๐ช")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Cute_King09")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/CuteKing09/DishaMusic")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5399406295").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/DevilHaveliMF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/DevilServerMF")

# ๐๐จ ๐๐จ๐ญ ๐๐ก๐๐ง๐ ๐ ๐๐ก๐ข๐ฌ ๐๐ข๐ง๐๐ฌ // ๐๐ ๐ง๐จ๐ซ๐ ๐๐ก๐ข๐ฌ (๐ช๐๐๐ ๐ฒ๐๐๐) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/Team_STD_Network")
