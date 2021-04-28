import telebot
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f'Меня зовут MathingBot! Рад знакомству, {message.from_user.first_name} :)')
@bot.message_handler(content_types=['text'])
def get_text_message(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.from_user.id, 'Привет!')
	else:
		bot.send_message(message.from_user.id, 'Извини, меня еще не научили этому слову :(')
		bot.polling(none_stop=True)