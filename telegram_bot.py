from datetime import datetime
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes
import asyncio


class TelegramBot:
    """
    Cette classe permet de créer un bot Telegram qui peut envoyer des messages à un chat spécifique.
    """

    def __init__(self, bot_token, chat_id):
        """
        Initialisation du bot Telegram.
        :param bot_token: Token du bot Telegram
        :param chat_id: ID du chat où envoyer les messages
        """
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.application = ApplicationBuilder().token(bot_token).build()
        self.bot = Bot(bot_token)
        self.is_started = False

    async def run(self) -> None:
        """
        Fonction principale pour exécuter le bot Telegram.
        :return: None
        """
        try:
            await self.application.initialize()
            await self.application.start()
            self.application.add_handler(CommandHandler('start', self.start_command))
            self.application.add_handler(CommandHandler('stop', self.stop_command))
            self.application.add_handler(CommandHandler('custom', self.custom_command))
            self.application.add_handler(MessageHandler(filters.TEXT, self.handle_message))
            await self.application.updater.start_polling()
            await asyncio.create_task(self.send_messages_interval())
        except asyncio.CancelledError:
            await self.send_message(text='Bot stopped')
        except Exception as e:
            await self.send_message(text=f'Error: {e}')
        finally:
            await self.application.stop()

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Commande pour indiquer au bot de commencer à faire une action.
        :param update: Update contient les informations sur la commande
        :param context: Contexte contient les informations sur le bot
        :return: None
        """
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Started !')
        self.is_started = True

    async def stop_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Commande pour indiquer au bot d'arrêter une action.
        :param update: Update contient les informations sur la commande
        :param context: Contexte contient les informations sur le bot
        :return: None
        """
        self.is_started = False
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Stopped !')

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Gère les messages entrants.
        :param update: Update contient les informations sur le message
        :param context: Contexte contient les informations sur le bot
        :return: None
        """
        text = update.message.text.lower()
        response = self.handle_response(text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    @staticmethod
    async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Commande personnalisée.
        :param update: Update contient les informations sur la commande
        :param context: Contexte contient les informations sur le bot
        :return: None
        """
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Custom command!')

    @staticmethod
    def handle_response(text) -> str:
        """
        Gère la réponse à envoyer en fonction du texte reçu.
        :param text: Texte reçu
        :return: Réponse à envoyer
        """
        if 'hello' in text:
            return 'Hello!'
        elif 'how are you' in text:
            return 'I am fine, thank you!'
        elif 'bye' in text:
            return 'Goodbye!'
        else:
            return 'I do not understand you!'

    async def send_messages_interval(self) -> None:
        """
        Envoie des messages à intervalles réguliers. Il s'agit d'un EXEMPLE de tâche asynchrone qui peut être
        exécutée en parallèle et qui va envoyer démarrer quand le bot aura reçu la commande /start.
        Il s'arrêtera quand le bot aura reçu la commande /stop.
        :return: None
        """
        while True:
            if self.is_started:
                await self.send_message(text=f'Message sent at {datetime.now()}')
            await asyncio.sleep(5)

    async def send_message(self, text: str) -> None:
        """
        Envoie un message au chat.
        :param text: Texte du message à envoyer
        :return: None
        """
        await self.bot.send_message(chat_id=self.chat_id, text=text)
