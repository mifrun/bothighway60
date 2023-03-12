import telebot
from config import TOKEN
from conversation_module import start_bot

bot = telebot.TeleBot(TOKEN)

if __name__ == '__main__':
    start_bot(bot)
