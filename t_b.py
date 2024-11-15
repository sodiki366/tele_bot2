import telebot

# Вставьте сюда ваш токен от BotFather
API_TOKEN = '7332975406:AAG8fCx2YkOz_lGxGpFXnVmJVrjnsITQKRI'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)
# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, 'Привет!Попугай Джон звонит , попугай Джон звонит'
                          ',попугай Джон звонит , у него все хорошо , и тебе того же!!!!')

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки событий
    bot.polling()