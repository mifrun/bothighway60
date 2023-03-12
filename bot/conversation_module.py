from halpers import get_random_answer
import random_answer_module

# Словарь, который хранит состояния пользователей
user_states = {}

# Функция-обработчик входящих сообщений
def handle_messages(message, bot):
    # Получаем состояние текущего пользователя
    user_state = user_states.get(message.chat.id, None)

    # Если состояние не было найдено, то считаем, что пользователь начал новую беседу
    if not user_state:
        bot.send_message(message.chat.id, 'Здравствуйте! Я шар ответов. Задайте мне любой вопрос.')
        user_states[message.chat.id] = 'WAITING_FOR_QUESTION'
    # Если пользователь уже задал вопрос, то отправляем случайный ответ
    elif user_state == 'WAITING_FOR_ANSWER':
        answer = get_random_answer(random_answer_module)
        bot.send_message(message.chat.id, answer)
        user_states[message.chat.id] = None

# Функция-обработчик команды /start
def handle_start(message, bot):
    bot.send_message(message.chat.id, 'Привет! Я шар ответов. Задайте мне любой вопрос.')

# Функция-обработчик команды /help
def handle_help(message, bot):
    bot.send_message(message.chat.id, 'Я могу ответить на любой ваш вопрос!')

# Функция-обработчик команды /stop
def handle_stop(message, bot):
    bot.send_message(message.chat.id, 'До свидания! Возвращайтесь, если у вас появятся еще вопросы.')
    user_states[message.chat.id] = None

# Функция-обработчик неизвестных команд
def handle_unknown(message, bot):
    bot.send_message(message.chat.id, 'Извините, я не понимаю вашу команду. Введите /help для списка команд.')

# Функция для запуска бота
def start_bot(bot):
    # Обработчики команд
    bot.add_message_handler(handle_start, commands=['start'])
    bot.add_message_handler(handle_help, commands=['help'])
    bot.add_message_handler(handle_stop, commands=['stop'])

    # Обработчик всех входящих сообщений
    bot.add_message_handler(handle_messages)

    # Обработчик неизвестных команд
    bot.add_message_handler(handle_unknown)

    # Запускаем бота
    bot.polling(none_stop=True)
