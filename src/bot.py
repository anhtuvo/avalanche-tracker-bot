import os
import telebot
from dotenv import load_dotenv
from src.tracker import gas_command
load_dotenv()


def run_telegram_bot():
    bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Avalanche Gas Tracker Bot\n\n" +
            "For more information, type /help\n\n"
            "Created by @lelouch1810"
        )

    @bot.message_handler(commands=['gas'])
    def echo_gas(message):
        crawled_data = gas_command()
        bot.reply_to(message, crawled_data)

    @bot.message_handler(commands=['help'])
    def echo_help(message):
        bot.reply_to(message, "Welcome to Avalanche Tracker Bot\n\n" +
            "/gas - Get current gas price\n" +
            "/help - Get help\n" +
            "/donate - Buy me a coffee\n\n" + 
            "If you have any questions or suggestions, please contact @lelouch1810\n\n"
        )

    @bot.message_handler(commands=['donate'])
    def echo_donate(message):
        bot.reply_to(message, "Buy me a coffee\n\n" +
            "Avax C-Chain: 0xfebDCf495e9C2770260FD08234E07beea15735B5\n" +
            "Avax X-Chain: X-avax1v79t84udr0e5585p0vxwhmvxepgz9dtcjarcty\n\n" +
            "Thank you!"
        )

    bot.infinity_polling()
