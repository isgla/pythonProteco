


def escucha(mensajes):
	for m in mensajes:
		#print(m)
		chat_id = m.chat.id
		miBot.send_message(chat_id,"Tu id es: "+str(chat_id))
		if m.content_type == 'text':
			text = m.text
			miBot.send_message(chat_id,"Enviaste el texto: "+text)

miBot.set_update_listener(escucha)

miBot.polling()