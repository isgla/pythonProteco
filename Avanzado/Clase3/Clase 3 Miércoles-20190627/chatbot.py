from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot("EjemploBot")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.spanish.conversations")

while True:
	mensaje = input("->")
	if mensaje == "salir":
		break
	respuesta = chatbot.get_response(mensaje)
	print("BOT: "+str(respuesta))

	