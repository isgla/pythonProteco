import telebot

token = '662482108:AAE8zi4Ed22Ty7pykjiAZHZIMoq04yx8DyI'
miBot = telebot.TeleBot(token)
chat_id = 886078749


def escucha(mensajes):
	for m in mensajes:
		chat_id = m.chat.id
		try:
			doc = open(m.text,"rb")
			miBot.send_document(chat_id,doc)
		except Exception as e:
			miBot.send_message(chat_id, "No existe ese archivo :(") 
		
		



miBot.set_update_listener(escucha)
miBot.polling()


