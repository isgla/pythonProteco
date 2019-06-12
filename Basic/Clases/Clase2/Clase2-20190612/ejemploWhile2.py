#Continue
#Break
#Pass

while True:
	cadena = input("Ingrese una cadera (o ingrese salir para terminar con el ciclo while): ")
	if cadena == "continuar":
		continue #Ignora las siguientes líneas, regresando al principio del ciclo
	if cadena == "salir":
		print("Adiós.")
		break	#Rompe con el ciclo
	if cadena == "pasar":	
		pass #Se usa para desarrollares cuando es necesario tomarlo en cuenta pero no queremos ejecutar nada 
	print("Tu cadena es: "+cadena)