#Comparaciones múltiples con operadores lógicos
# AND ambos deben ser verdaderos  
# OR alguno de los dos debe ser verdadero
# NOT el primero debe ser verdadero y el segundo falso

import random
#x=random.randint(1,101)
x=4

if x==0:
	print("El número es 0")
else:
	if x>0 and x<=10:
		print("El número está entre 0 y 10 y es {0}".format(x))
	else:
		if x>10 and x<=20:
			print("El número está entre 10 y 20 y es {0}".format(x))
		else:
			print("El número es {0}".format(x))

#ELIF: concatenación/fusión entre else e if
#Corresponde a un else y un if consecutivos, da orden al programa

if x==0:
	print("El número es 0")
elif x>0 and x<=10:
	print("El número esta entre 0 y 10 y es {0}".format(x)) 
elif x>10 and x<=20:
	print("El número esta entre 10 y 20 y es {0}".format(x))
else:
	print("Es otro número : {0}".format(x))




