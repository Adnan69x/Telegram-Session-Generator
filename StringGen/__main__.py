import asyncio
import importlib

from pyrogram import idle

from StringGen import LOGGER, Adnany
from StringGen.modules import ALL_MODULES


async def adnany_boot():
    try:
        await Adnany.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("StringGen.modules." + all_module)

    LOGGER.info(f"@{Adnany.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(adnany_boot())
    LOGGER.info("Stopping String Gen Bot...")
