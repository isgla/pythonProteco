import sqlite3

#Connect recibe el nombre de la base de datos a conectar
#Si no existe esa base de datos la crea
conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()
cursor.execute("DROP TABLE alumno")
cursor.execute("CREATE TABLE alumno(nombre varchar(30), edad integer, num_cuenta integer, calificacion integer CHECK(calificacion>0 and calificacion<10))")
cursor.execute("INSERT INTO alumno VALUES ('David',20,322181258,9)")
cursor.execute("INSERT INTO alumno VALUES ('David1',20,322181258,9)")
cursor.execute("INSERT INTO alumno VALUES ('David2',20,322181258,9)")

#cursor.execute("INSERT INTO alumno VALUES ('Ana',19,310872429,10)")

#Confirma como permanentes las modificaciones a la tabla.
conexion.commit()

cursor.execute("select * from alumno") #Retornar todos los registros con todos sus atributos
#alumno1 = cursor.fetchone()
variosAlumnos = cursor.fetchmany(3)

#print(alumno1)
print(variosAlumnos)

conexion.close()