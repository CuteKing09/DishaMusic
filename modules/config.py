# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝑪𝒖𝒕𝒆_𝑲𝒊𝒏𝒈09)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝑪𝒖𝒕𝒆_𝑲𝒊𝒏𝒈09
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/c6e1041c6c9a12913f57a.png")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "➳➣⃟ᴵᴬᴹ ₡U₸E ƙł₦G 𓆩😈𓆪")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Cute_King09")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/CuteKing09/DishaMusic")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5399406295").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/DevilHaveliMF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/DevilServerMF")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝑪𝒖𝒕𝒆 𝑲𝒊𝒏𝒈) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
NETWORK_CHANNEL = getenv("NETWORK_CHANNEL", "https://t.me/Team_STD_Network")
