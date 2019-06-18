try:
	print(x)#tratamos de imprimir la variable x
except NameError:
	print("La variable x no esta definida")
except:
	print("Algo mas no esta funcionando")