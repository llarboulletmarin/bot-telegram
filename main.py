from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')
BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN')
BOT_CHAT_ID = getenv('TELEGRAM_BOT_CHAT_ID')
BOT_USERNAME = getenv('TELEGRAM_BOT_USERNAME')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello! I am {BOT_USERNAME}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Help!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom command!')


def handle_response(text: str) -> str:
    processed_text = text.lower()

    if 'hello' in processed_text:
        return 'Hello!'

    if 'how are you' in processed_text:
        return 'I am fine, thank you!'

    if 'bye' in processed_text:
        return 'Goodbye!'

    return 'I do not understand you!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in chat({message_type}) sent: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print(f'Response: {response}')
    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    await update.message.reply_text('An error occurred!')

if __name__ == '__main__':
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error_handler)

    print('Polling...')
    app.run_polling(poll_interval=3)
