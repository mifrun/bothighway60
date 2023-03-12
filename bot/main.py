import telebot
import random
from config import TOKEN, predictions
from conversation_module import start_bot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Привет! Я шар предсказаний из фильма 'Трасса 60'. Напишите мне свой вопрос, чтобы получить предсказание.")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(
        f'данные пользователя: name - {message.chat.first_name}; id - {message.chat.id}')
    print(f'сообщение: {message.text}')
    response = random.choice(predictions)
    print(f'ответ: {response}')
    bot.reply_to(message, response)


if __name__ == '__main__':
    start_bot(bot)
