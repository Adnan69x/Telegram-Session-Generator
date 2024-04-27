import aiohttp
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bs4 import BeautifulSoup
import os
import re

TOKEN = "6090428616:AAGEDpuZXDWk0EyoGEz7G1DKdOFxmBP5yIA"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def download_mp4(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                filename = url.split('/')[-1]
                with open(filename, 'wb') as f:
                    f.write(await response.read())
                return filename
            else:
                raise Exception("Couldn't download the MP4 file.")

async def get_content_id_from_url(url: str) -> str:
    # Assuming the content ID is the last part of the URL after the last '/'
    parts = url.split('/')
    content_id = parts[-1]
    return content_id

async def get_bongobd_response(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                raise Exception("Couldn't fetch the BongoBD webpage.")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hello! Send me the BongoBD URL or content ID you want to download.")

@dp.message_handler()
async def process_url(message: types.Message):
    url = message.text
    try:
        if 'https;//bongobd.com/watch/' in url:
            # Extract content ID from the URL
            content_id = re.search(r'watch/(\w+)', url).group(1)
            # Construct request URL using content ID
            request_url = f"https://vod.bongobd.com/vod/vod/{content_id}/3/8/{content_id}_x264_1080p_5500k.m3u8"
        else:
            # Assuming the user directly provides the request URL
            request_url = url

        # Download MP4 file from the constructed/request URL
        mp4_filename = await download_mp4(request_url)

        with open(mp4_filename, 'rb') as mp4_file:
            await bot.send_document(message.chat.id, mp4_file)

        os.remove(mp4_filename)  # Remove the downloaded file after sending
        await message.reply("MP4 file sent successfully!")
    except Exception as e:
        await message.reply(f"Error: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
