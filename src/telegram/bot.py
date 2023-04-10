import os
import telebot
from loguru import logger
from  src.gpt import gpt_api

class TelegramClient:
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))
                  
    def run(self):
        logger.info("Bot is running...")
                          
        @self.bot.message_handler(func=lambda message: True)
        def call_gpt(message):
            logger.info(f"Revieved message to ask to GPT: {message.text}")

            response = gpt_api.handle_response(message.text)
            
            logger.info(f"Response from GPT: {response}")
            
            self.bot.reply_to(message, response)
            
        self.bot.infinity_polling()