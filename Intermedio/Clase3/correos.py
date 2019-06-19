import smtplib
import getpass

#tls le agrega una capa más de seguridad
def enviar_correo(remitente, password, destinatario, asunto, cuerpo):
	print("Preparando el correo...")
	
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	#Se pone el servidor de correo, 587 es el puerto que utiliza gmail
	#smtp es el protocolo

	#Pasos del protocolo SMTP
	smtpserver.ehlo() #Saludo al servidor
	smtpserver.starttls() #Agrega otra capa de seguridad
	try:
		smtpserver.login(remitente, password)
	except:
		print("No has configurado tu correo, favor de revisar")

	#Se usan expresiones regulares para checar que el header esté bien escrito
	#Header son cabeceras que llevan metadatos, los datos se compartan con json y 
	#El header es como la llave del diccionario.
	#Los header llevam el from y el subject en este caso.
	header = "To: {0}\nFrom: {1}\nSubject: {2}\n".format(destinatario, remitente, asunto)
	msg = header + "\n{0}\n\n".format(cuerpo)
	print(msg)

	smtpserver.sendmail(remitente, destinatario, msg)
	smtpserver.close()
	#Siempre cerrar flujos

if __name__ == "__main__":
	usuario = input("Escribe el remitente: ")
	password = getpass.getpass("Escriba su contraseña: ")
	destinatario = input("Escriba el destinatario: ")
	asunto = input("Escriba el asunto: ")
	cuerpo = input("Escriba su mensaje: ")

	for x in range (1,4):
		enviar_correo(usuario, password, destinatario, asunto, cuerpo)

	


