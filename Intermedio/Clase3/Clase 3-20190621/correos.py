import smtplib
import getpass

def enviar_correo(remitente, password, destinatario, asunto, cuerpo):
	print("Preparando el correo...")
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

	# Pasos del protocolo SMTP
	smtpserver.ehlo() # Saludo al servidor
	smtpserver.starttls() # Agrega otra capa de seguridad
	try:
		smtpserver.login(remitente, password)
	except:
		print("No has configurado tu correo, favor de revisar")
	header = "To: {0}\nFrom: {1}\nSubject: {2}\n".format(destinatario, remitente, asunto)
	msg = header + "\n{0}\n\n".format(cuerpo)
	print(msg)

	smtpserver.sendmail(remitente, destinatario, msg)
	smtpserver.close()


if __name__ == "__main__":

	usuario = input("Escriba el remitente: ")
	password = getpass.getpass("Escriba su contraseña: ")
	destinatario = input("Escriba el destinatario: ")
	asunto = input("Escriba el asunto: ")
	cuerpo = input("Escriba su mensaje: ")
	for i in range(100):
		enviar_correo(usuario, password, destinatario, asunto, cuerpo)



