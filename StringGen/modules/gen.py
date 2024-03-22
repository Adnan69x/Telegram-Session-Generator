import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from StringGen import Adnany
from StringGen.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ᴛᴇʟᴇᴛʜᴏɴ"
    elif old_pyro:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v1"
    else:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v2"

    await message.reply_text(f"» TRYING TO START {ty} SESSION GENERATOR...")

    try:
        api_id = await Adnany.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴀᴘɪ ɪᴅ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Adnany.send_message(
            user_id,
            "» TIMED LIMIT REACHED OF 5 MINUTES.\n\nPLEASE START GENERATING SESSION AGAIN.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Adnany.send_message(
            user_id,
            "» THIS API ID YOU'VE SENT IS INVALID.\n\nPLEASE START GENERATING SESSION AGAIN .",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Adnany.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴀᴘɪ ʜᴀsʜ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Adnany.send_message(
            user_id,
            "» TIMED LIMIT REACHED OF 5 MINUTES.\n\nPLEASE START GENERATING SESSION AGAIN .",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Adnany.send_message(
            user_id,
            "» THIS API HASH YOU'VE SENT IS INVALID.\n\nPLEASE START GENERATING SESSION AGAIN .",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Adnany.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Adnany.send_message(
            user_id,
            "» TIMED LIMIT REACHED OF 5 MINUTES.\n\nPLEASE START GENERATING SESSION AGAIN .",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Adnany.send_message(user_id, "» TRYING TO SEND OTP AT THE GIVEN NUMBER...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Adnany", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Adnany.send_message(
            user_id,
            f"» FAILED TO SEND CODE FOR LOGIN.\n\nPLEASE WAIT FOR {f.value or f.x} SECOUNDS AND TRY AGAIN.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Adnany.send_message(
            user_id,
            "» ɪɴᴠᴀʟɪᴅ API ID OR API HASH IS INVALID.\n\nPLEASE START GENERATING YOUR SESSION AGAIN.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Adnany.send_message(
            user_id,
            "» PHONE NUMBER INVALID.\n\nPLEASE START GENERATING YOUR SESSION AGAIN.",
            reply_markup=retry_key,
        )

    try:
        otp = await Adnany.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"PLEASE ENTER THE OTP SENT TO {phone_number}.\n\nIF OTP IS <code>12345</code>, PLEASE SEND IT AS <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Adnany.send_message(
            user_id,
            "» TIMED LIMIT REACHED OF 10 MINUTES.\n\nPLEASE START GENERATING YOUR SESSION AGAIN.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Adnany.send_message(
            user_id,
            "» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs <b>ᴡʀᴏɴɢ.</b>\n\nPLEASE START GENERATING YOUR SESSION AGAIN.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Adnany.send_message(
            user_id,
            "» THE OTP YOU'VE SENT IS <b>ᴇxᴩɪʀᴇᴅ.</b>\n\nPLEASE START GENERATING YOUR SESSION AGAIN.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Adnany.ask(
                identifier=(message.chat.id, user_id, None),
                text="» PLEASE ENTER YOUR TWO STEP VERIFICATION PASSWORD TO CONTINUE :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Adnany.send_message(
                user_id,
                "» TIMED LIMIT REACHED OF 5 MINUTES.\n\nPLEASE START GENERATING SESSION AGAIN .",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Adnany.send_message(
                user_id,
                "» THE PASSWORD YOU'VE SENT IS WRONG.\n\nPLEASE START GENERATING YOUR SESSION AGAIN.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Adnany.send_message(user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code>")

    try:
        txt = "HERE IS YOUR {0} STRING SESSION\n\n<code>{1}</code>\n\nA STRING GENERATOR BOT BY <a href={2}>ADNANiTUNE</a>\n☠ <b>NOTE :</b> DON'T SHARE IT WITH YOUR GIRLFRIEND."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@ADNANiTUNE"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("ADNANiTUNE")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Adnany.send_message(
            chat_id=user_id,
            text=f"SUCCESSFULLY GENERATED YOUR {ty} STRING SESSION.\n\nPLEASE CHECK YOUR SAVED MESSAGES FOR GETTING IT.\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={SUPPORT_CHAT}>ADNANiTUNE</a>.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» CANCELLED THE ONGOING STRING GENERATION PROCESS.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» SUCCESSFULLY RESTATED THIS BOT.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» CANCELLED THE ONGOING STRING GENERATION PROCESS.", reply_markup=retry_key
        )
        return True
    else:
        return False
