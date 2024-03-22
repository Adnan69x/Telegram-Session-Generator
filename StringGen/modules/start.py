from pyrogram import filters
from pyrogram.types import Message

from StringGen import Adnany
from StringGen.utils import add_served_user, keyboard


@Adnany.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"Hey {message.from_user.first_name},\n\n◑ This is {Adnany.mention},\nAn Open Source String Session Generator Bot, Written In Python With The Help Of Python.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
