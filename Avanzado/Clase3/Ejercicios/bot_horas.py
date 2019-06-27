import telebot
from telebot import types
import time

#Insert token there
token = ''

miBot = telebot.TeleBot(token)

#Insert chat_id there
chat_id = #########

"""
while True:
	#Me repite el ciclo y te representa la hora en formato de cadena
	hora = time.strftime("%X")
	if hora == "09:21:30":
		miBot.send_message(chat_id, "Ya despiertate")
		break
"""

#Para que mande la hora cuando le des click en el botón
@miBot.message_handler(commands=["hora"])
def enviarHora(message):
	mensaje = "La hora actual es: " + time.strftime("%X")
	miBot.send_message(chat_id, mensaje)

#Que tenga botones
markup = types.ReplyKeyboardMarkup(row_width = 1)
item1 = types.KeyboardButton('/hora')
markup.add(item1)
miBot.send_message(chat_id, "Elige una opción: ", reply_markup = markup)

miBot.polling()