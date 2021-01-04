import telebot

bot = telebot.TeleBot('1461337212:AAGi_m0hDOYNShehKYu4ZGwLKhqeth_VhnQ')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет','Спасибо!')
@bot.message_handler(commands=['start'])
def start_message(message): 
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'C днем рождения, Мама!!')
    elif message.text == 'Спасибо!':
        bot.send_message(message.chat.id, 'Желаю тебе всего самого наилучшего и притяного, чтоб не болела и была только счастлива! Я люблю тебя, твой Женя.')
bot.polling()
        