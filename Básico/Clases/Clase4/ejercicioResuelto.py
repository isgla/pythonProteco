class Alumno

	def __init__(self, nombre, apellidos, cuenta, materias,
		calificaciones):

		self.nombre = nombre
		self.apellidos = apellidos
		self.cuenta = cuenta
		self.materias = materias
		self.calificaciones = calificaciones
		self.promedio = sum(self.calificaciones)/5

while True:
	alumnos = []
	opcion = input("¿Desea agregar alumno?")
	if opcion != "Salir":
		nombre = input("Ingrese el nombre: ")
		apellido = input("Ingrese el apellido: ")
		cuenta = input("Ingrese la cuenta: ")
		materias = []
		cuenta = []
		for materia in range(5):
			materia_actual = input("Ingrese materias: ")
			calificacion_actual = input("Ingrese califición: ")
		
