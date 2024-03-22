from pyrogram import filters
from pyrogram.types import Message

from StringGen import Adnany
from StringGen.utils import add_served_user, keyboard


@Adnany.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"𝐇𝐞𝐲 {message.from_user.first_name},\n\n◑ 𝐓𝐡𝐢𝐬 𝐢𝐬 {Adnany.mention},\n𝐀𝐧 𝐎𝐩𝐞𝐧 𝐒𝐨𝐮𝐫𝐜𝐞 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐁𝐨𝐭, 𝐖𝐫𝐢𝐭𝐭𝐞𝐧 𝐈𝐧 𝐏𝐲𝐭𝐡𝐨𝐧 𝐖𝐢𝐭𝐡 𝐓𝐡𝐞 𝐇𝐞𝐥𝐩 𝐎𝐟 𝐏𝐲𝐭𝐡𝐨𝐧.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
