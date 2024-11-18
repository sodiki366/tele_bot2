import telebot

# Токен вашего бота
API_TOKEN = '7822532225:AAExL_QrBJidJWkhP-UIcsaiLPkp52_0UYc'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

# Вопросы и ответы для разных уровней сложности
questions = {
    'easy': [
        {'question': 'Какой город является столицей Франции?', 'answer': 'Париж'},
        {'question': 'Какое самое большое озеро в мире?', 'answer': 'Каспийское море'},
        {'question': 'В каком городе находится Эйфелева башня?', 'answer': 'Париж'}
    ],
    'normal': [
        {'question': 'Какая страна имеет самую большую площадь в мире?', 'answer': 'Россия'},
        {'question': 'Какой самый длинный горный хребет в мире?', 'answer': 'Анды'},
        {'question': 'Какой океан является самым глубоким?', 'answer': 'Тихий океан'}
    ],
    'hard': [
        {'question': 'Как называется самая длинная река в мире?', 'answer': 'Нил'},
        {'question': 'Какой остров является крупнейшим в мире?', 'answer': 'Гренландия'},
        {'question': 'Какая страна имеет наибольшее количество озёр?', 'answer': 'Канада'}
    ]
}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет! Хочешь сыграть в викторину? Выбери уровень сложности:\n/level_easy\n/level_normal\n/level_hard")


# Обработчики команд выбора уровня сложности
@bot.message_handler(commands=['level_easy'])
def start_easy_level(message):
    ask_question('easy', message.chat.id, 0)


@bot.message_handler(commands=['level_normal'])
def start_normal_level(message):
    ask_question('normal', message.chat.id, 0)


@bot.message_handler(commands=['level_hard'])
def start_hard_level(message):
    ask_question('hard', message.chat.id, 0)


# Функция для отправки вопросов
def ask_question(level, chat_id, question_index):
    if question_index < len(questions[level]):
        current_question = questions[level][question_index]
        markup = telebot.types.ForceReply(selective=False)
        bot.send_message(chat_id, current_question['question'], reply_markup=markup)
        bot.register_next_step_handler_by_chat_id(chat_id, lambda message: check_answer(message, level, question_index))
    else:
        bot.send_message(chat_id, "Молодец! Ты ответил на все вопросы этого уровня.")


# Проверка ответа
def check_answer(message, level, question_index):
    current_question = questions[level][question_index]
    if message.text.lower() == current_question['answer'].lower():
        bot.send_message(message.chat.id, "Правильно!")
    else:
        bot.send_message(message.chat.id, f"Неправильно. Правильный ответ: {current_question['answer']}")

    # Переход к следующему вопросу
    next_question_index = question_index + 1
    ask_question(level, message.chat.id, next_question_index)


# Запускаем бота
if __name__ == '__main__':
    bot.polling()