class Alumno:
    #Son parte de la clase y necesitan un objeto
    def __init__(self, nombre, apellidos, cuenta, materias,
                 calificaciones):
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.cuenta = cuenta
        self.materias = materias
        self.calificaciones = calificaciones
        self.promedio = sum(self.calificaciones)/len(calificaciones) #o 5
    
    def __str__(self):
        return("Nombre: {0}, Matrícula: {1}, Promedio: {2}".format(self.nombre, self.cuenta, self.promedio) )

#No necesitan un objeto y son funciones
def leer_calificaciones():
    calificaciones = []
    for iterador in range(5):
        calificacion = float(input("Ingrese la calificación: "))
        calificaciones.append(calificacion)
    return calificaciones

def leer_materias():
    materias = []
    for iterador in range(5):
        materia = input("Ingrese la materia: ")
        materias.append(materia)
    return materias



alumnos = []
while True:
    
    opcion = input("¿Desea agregar alumno? / Escriba salir para terminar el programa: " )
    if opcion != "salir":
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        cuenta = input("Ingrese la cuenta: ")
        materias = leer_materias()
        calificaciones = leer_calificaciones()
        
        alumno = Alumno(nombre, apellido, cuenta, materias, calificaciones)
        alumnos.append(alumno)
        
        #Imprimiría la memoria de la lista de alumnos print(str(alumnos))
        for alumno in alumnos:
            print(alumno) #print(str(alumno))

    else:
        break
		
