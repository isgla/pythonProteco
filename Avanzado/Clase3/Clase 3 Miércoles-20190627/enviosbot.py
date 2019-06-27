import telebot

token = '833902778:AAFlxSu9ChtJSZIvJ7wfKvEaMoFHSKbZmkY'

miBot = telebot.TeleBot(token)

@miBot.message_handler(commands = ['start','help'])
def send_welcome(message):
	miBot.reply_to(message, "Hola, soy tu bot de Python :)")


chat_id = 376113937

miBot.send_message(chat_id, "Hola :3")

file = open("crash.png","rb")
miBot.send_photo(chat_id, file)

doc = open("miprimerbot.py","rb")
miBot.send_document(chat_id,doc)

#miBot.send_video(chat_id,video)
#miBot.send_audio(chat_id,audio)

latitud = 19.325824
longitud = -99.182353
miBot.send_location(chat_id,latitud,longitud)

miBot.polling()