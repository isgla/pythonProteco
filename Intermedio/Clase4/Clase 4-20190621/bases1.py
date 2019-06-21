import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
#cursor.execute("DROP TABLE alumno")
try: 
	cursor.execute("CREATE TABLE alumno(nombre varchar(30), edad integer, num_cuenta integer, calificacion integer CHECK(calificacion>0 and calificacion<=10))")
except sqlite3.OperationalError:
	print("Valió")

finally:
	cursor.execute("INSERT INTO alumno VALUES('Alicia', 20, 123456, 10)")
	cursor.execute("INSERT INTO alumno VALUES('Rodrigo', 23, 129897, 10)")
	cursor.execute("INSERT INTO alumno VALUES('Aldo', 23, 457865, 10)")
	cursor.execute("INSERT INTO alumno VALUES('Adriana',19,32321,10)")
	cursor.execute("INSERT INTO alumno VALUES ('Derek', 21, 3213, 10)")
#Recuperando contenido de las tablas
cursor.execute("SELECT * FROM alumno")
alumno = cursor.fetchone()
print(alumno)
alumnos = cursor.fetchmany(3)
print(alumnos)
conexion.commit()
conexion.close()


