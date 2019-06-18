try:
	x=1/0
#inst sera nuestra variable
except ZeroDivisionError as inst:
	print(type(inst)) #la instancia de la excepcion
	print(inst.args) # imprimir los argumentos guardados en .args
	print(inst) # __str__ permitie imprimir directamente los argumentos