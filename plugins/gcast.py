# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 (C) 2022 𝑩𝒚 @Cute_King09

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as aditya
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["gcast", "broadcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**`🥀 ꜱᴛᴀʀᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀꜱᴛ ...`**")
        if not message.reply_to_message:
            await wtf.edit("**🎸 𝗣𝗹𝗲𝗮𝘀𝗲 𝗥𝗲𝗽𝗹𝘆 𝗧𝗼 𝗔 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 ...**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**🥀 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗶𝗻𝗴 ...** \n\n**✔️ 𝐒𝐞𝐧𝐭 𝐓𝐨:** `{sent}` **𝐂𝐡𝐚𝐭𝐬** \n**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐈𝐧:** `{failed}` **𝐂𝐡𝐚𝐭𝐬**")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await wtf.delete()
        await message.reply_text(f"**🥀 𝐆𝐜𝐚𝐬𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ...**\n\n**✔️ 𝐒𝐞𝐧𝐭 𝐓𝐨:** `{sent}` **𝐂𝐡𝐚𝐭𝐬**\n**❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐈𝐧:** `{failed}` **𝐂𝐡𝐚𝐭𝐬**")
