import telebot
#Insert token there
token = ''
miBot = telebot.TeleBot(token)
#Insert chat_id there
chat_id = #########


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


