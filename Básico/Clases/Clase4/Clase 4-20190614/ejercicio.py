class Alumno:

	def __init__(self, nombre, apellido, cuenta, materias, calificaciones):

		self.nombre = nombre
		self.apellido = apellido
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
		cuenta = input("Ingrese el cuenta: ")
		materias = []
		calificaciones = []
		for materia in range(5):
			materia_actual = input("Ingrese materia: ")
			calificacion_actual = input("Ingrese calificacion: ")
			materias.append(materia_actual)
			calificaciones.append(calificacion_actual)

		alumno_actual = Alumno(nombre, apellido, cuenta, materias, calificaciones)
		alumnos.append(alumno_actual)


