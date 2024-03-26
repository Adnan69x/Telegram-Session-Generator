import telebot
import logging

# Setup logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the Telegram bot
bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(bot_token)

# Define the handler for String Session messages
@bot.message_handler(func=lambda message: True)
def log_string_session(message):
    if message.text and "String Session" in message.text:
        logger.info(f"String Session message received from {message.from_user.username}: {message.text}")

# Start the bot
bot.polling()