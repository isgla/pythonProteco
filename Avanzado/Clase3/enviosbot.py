import telebot
#Insert token there
token = ''

miBot = telebot.TeleBot(token)

#Decorador: y de parametro, que comandos para que ejecute esa funcion
@miBot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
	miBot.reply_to(message, "Hola, soy tu bot de Python")

#Insert chat_id there
chat_id = #########
miBot.send_message(chat_id, "Hola :D")

#Mandar fotos
#rb es para abrirlo en bits Read in Bits
file = open("husky.jpg","rb")
miBot.send_photo(chat_id, file)

#Mandar archivos
doc = open("miprimerbot.py","rb")
miBot.send_document(chat_id,doc)

#Mandar video
#miBot.send_video(chat_id, video)
#miBot.send_audio(chat_id, audio)

#Con py audio pone a la escucha el microfono de tu compu y lo mando como nota de voz

#Mandar localización
latitud = 19.324172
longitud = -99.180137
miBot.send_location(chat_id,latitud, longitud)


#Para que tu bot se quede ahí, si no tiene un listener, solo te manda el mensaje 
#Para que se quede ejecutando el programa
miBot.polling()