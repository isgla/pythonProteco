import telebot
#Insert token there
token = ''

miBot = telebot.TeleBot(token)
#Ahí ya creaste tu objeto bot que es el que necesitas para mandar cosas

def escucha(mensajes):
	for m in mensajes:
		#Te crea un diccionario, hay un json, id, nombre, etc
		#print(m)
		#id te sale en el mensaje
		#Accedes al elemento del json (en el diccionario)
		chat_id = m.chat.id
		miBot.send_message(chat_id, "Tu id es: " + str(chat_id))
		#Si el mensaje es de tipo text
		if m.content_type == 'text':
			text = m.text
			miBot.send_message(chat_id, "Enviaste el texto: " + text)

#Cuando reciba un mensaje te regresa tu id y el mensaje que le enviaste

miBot.set_update_listener(escucha)
miBot.polling()


