import sqlite3
#A todas las bases de datos les vamos a pasar un archivo de tipo data base
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
#El cursor es el que me permite ejecutar las acciones
#Intrucción y el nombre de la table
#En sql varchar es equivalente a un cadena en python
#Atributos
try:
	#Marca un error cuando la tabla ya esta creada
	cursor.execute("CREATE TABLE alumno(nombre varchar(30), edad integer, num_cuenta integer, calificacion integer CHECK(calificacion>0 and calificacion<=10))")
#General para todas las excepciones
except sqlite3.OperationalError:
	print("Ocurrió un error")
#El else se ejecuta si cacha la excepcion
#Finally se ejecuta siempre
finally:
	cursor.execute("INSERT INTO alumno VALUES('Hannah', 19, 54321, 10)")
	cursor.execute("INSERT INTO alumno VALUES('Ariana', 18, 56783, 10)")
	cursor.execute("INSERT INTO alumno VALUES('Mali', 22, 23456, 10)")
#Recuperando contenido de las tablas
cursor.execute("SELECT * FROM alumno")
alumno = cursor.fetchone()
print(alumno)
alumnos = cursor.fetchmany(3)
print(alumnos)

#Para ver que todo lo que le pediste que hiciera se haya hechos
conexion.commit()
conexion.close()