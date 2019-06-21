import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
alumnos = [('Rodrigo',20,310587896,8),
			('Aldo',21,310254689,9),
			('Derek',20,312045789,7) ] #Lista de tuplas, cada tupla almacena un alumno

cursor.executemany("INSERT INTO alumno VALUES (?,?,?,?)",alumnos)

cursor.execute("SELECT * from alumno")
alumnos = cursor.fetchall() #Lista de tuplas 
#print(alumnos)

for alumno in alumnos:
	print(alumno)

#renameTable = "ALTER TABLE alumno RENAME TO student"
#cursor.execute(renameTable)

#cursor.execute("DELETE FROM alumno")

conexion.commit()
conexion.close()