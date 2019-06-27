import telebot
from telebot import types
import time

token = '833902778:AAFlxSu9ChtJSZIvJ7wfKvEaMoFHSKbZmkY'

miBot = telebot.TeleBot(token)

chat_id = 376113937

"""
while True:
	hora = time.strftime("%X")
	if hora == "09:21:00":
		miBot.send_message(chat_id, "Ya despiertate!")
		break
"""
@miBot.message_handler(commands=["hora"])
def enviarHora(message):
	mensaje = "La hora actual es: "+time.strftime("%X")
	miBot.send_message(chat_id,mensaje)

markup = types.ReplyKeyboardMarkup(row_width=1)
item1 = types.KeyboardButton('/hora')
markup.add(item1)

miBot.send_message(chat_id,"Elige una opcion: ",reply_markup=markup)
miBot.polling()