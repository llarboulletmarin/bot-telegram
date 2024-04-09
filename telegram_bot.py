from datetime import datetime
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes
import asyncio


class TelegramBot:

    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.application = ApplicationBuilder().token(bot_token).build()
        self.bot = Bot(bot_token)
        self.is_sending_messages = False

    async def start(self):
        try:
            await self.application.initialize()
            await self.application.start()
            self.application.add_handler(CommandHandler('start', self.start_command))
            self.application.add_handler(CommandHandler('stop', self.stop_command))
            self.application.add_handler(CommandHandler('help', self.help_command))
            self.application.add_handler(CommandHandler('custom', self.custom_command))
            self.application.add_handler(MessageHandler(filters.TEXT, self.handle_message))
            await self.application.updater.start_polling()
            await asyncio.create_task(self.send_messages())
            while True:
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            print('Bot stopped!')
        finally:
            await self.application.stop()

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Hello! I am {context.bot.username}')
        time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        await self.bot.send_message(chat_id=self.chat_id, text=f'Hello! I started ! it\'s {time_now}')
        self.is_sending_messages = True

    async def stop_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.is_sending_messages = False
        # await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Bye !')
        time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        await self.bot.send_message(chat_id=self.chat_id, text=f'Bye ! it\'s {time_now}')


    async def help_command(self, update, context):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='Help!')

    async def custom_command(self, update, context):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='Custom command!')

    async def handle_message(self, update, context):
        text = update.message.text.lower()
        response = self.handle_response(text)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=response)

    @staticmethod
    def handle_response(text):
        if 'hello' in text:
            return 'Hello!'
        elif 'how are you' in text:
            return 'I am fine, thank you!'
        elif 'bye' in text:
            return 'Goodbye!'
        else:
            return 'I do not understand you!'

    async def send_messages(self):
        while True:
            if self.is_sending_messages:
                time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                await self.bot.send_message(chat_id=self.chat_id, text=f'Message sent at {time_now}')
            await asyncio.sleep(5)
