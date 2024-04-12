from os import getenv
from dotenv import load_dotenv
import asyncio

from telegram_bot import TelegramBot

load_dotenv('.env')
BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = getenv('TELEGRAM_CHAT_ID')

if __name__ == '__main__':
    bot = TelegramBot(BOT_TOKEN, CHAT_ID)
    asyncio.run(bot.start())
