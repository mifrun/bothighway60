import os

# Получаем токен бота из переменной окружения, чтобы не хранить его в коде
TOKEN = os.environ.get('TELEGRAM_TOKEN')

# Если переменная окружения не была найдена, то используем значение по умолчанию
if not TOKEN:
    TOKEN = 'your-telegram-bot-token-here'
