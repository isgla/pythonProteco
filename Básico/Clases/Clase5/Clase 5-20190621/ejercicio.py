"""
Clase alumno que tenga:
	- Nombre
	- Apellido
	- Matricula
	- Materias (5)
	- Calificaciones (5)
	- Promedio

El usuario va a ingresar todos los datos hasta que escriba salir
Los alumnos se almacenarán en una lista
"""

class Alumno:

	def __init__(self, nombre, apellido, matricula, materias, calificaciones):

		self.nombre = nombre
		self.apellido = apellido
		self.matricula = matricula
		self.materias = materias
		self.calificaciones = calificaciones
		self.promedio = sum(calificaciones) / 5

	def __str__(self):

		return "El alumno {alumno} tiene {promedio} de promedio".format(alumno=self.nombre, promedio=self.promedio)



def leer_calificaciones():

	calificaciones = [] 
	for iterador in range(5):
		calificacion = float(input("Ingrese la calificación: "))
		calificaciones.append(calificacion)

	return calificaciones

def leer_materias():

	materias = []
	for iterador in range(5):
		materia = input("Ingrese materia: ")
		materias.append(materia)

	return materias


alumnos = []

while True:

	opcion = input("¿Desea agregar otro alumno? / Escriba Salir para terminar el programa: ")

	if opcion == "Salir":
		break

	else:
		nombre = input("Escriba el nombre del alumno: ")
		apellido = input("Escriba el apellido del alumno: ")
		matricula = input("Escriba la matrícula del alumno: ")
		materias = leer_materias()
		calificaciones = leer_calificaciones()
		
		alumno = Alumno(nombre, apellido, matricula, materias, calificaciones)
		alumnos.append(alumno)

		for alumno in alumnos:
			print(alumno)

