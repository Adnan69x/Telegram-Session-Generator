from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Telegram Bot API token
TOKEN = "your_bot_token_here"

# Channel ID where you want to forward the sessions
CHANNEL_ID = "your_channel_id_here"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Session Logger Bot! Send me your session to log it.")

def log_session(update: Update, context: CallbackContext) -> None:
    session_text = update.message.text
    forward_to_channel(session_text)

def forward_to_channel(session_text: str) -> None:
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHANNEL_ID, text=session_text)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, log_session))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
