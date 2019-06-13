class Alumno

	
	datos_de_alumons = []

	def __init__(self, nombre, apellidos, cuenta, materias,
		calificaciones):

		self.nombre = nombre
		self.apellidos = apellidos
		self.cuenta = cuenta
		self.materias = materias
		self.calificaciones = calificaciones
		self.promedio = promedio

	#Usar función lambda para sacar promedio

	bandera = True


	while bandera:
		menu = '''
		 MENU
		 1. Ingresa tu nombre
		 2. Ingresa tus apellidos
		 3. Ingresa tu cuenta
		 4. Ingresa las materias que llevaste este semestre
		 5. Ingresa tus calificaciones de este semestre
		 6. Recibe tu promedio de este semestre
		 7. Salir
		'''
		opc = int(input("Ingresa el número de la opción que quieras realizar: "))
		
		if (opc == 1):


		elif (opc == 2):


		elif (opc == 3):

		elif (opc == 4):

		elif (opc == 5):

		elif (opc == 6):

		elif (opc == 7):
			bandera = false
			break




		







'''
Ejercicio:

1. Lista de objetos de la clase Alumno
2. Alumno tendrá:
	-Nombre
	-Apellidos
	-Cuenta
	-Materias
	-Calificaciones
	-Promedio
3.se debe poder ingresar todos los datos a través de la terminal 
hasta que el usuario escriba salir
'''

