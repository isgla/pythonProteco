import sqlite3 
#Misma base de datos de bases1.py
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
alumnos = [('Derek', 21, 74367, 6), ('Adri', 19, 7556, 10)]
cursor.executemany("INSERT INTO alumno VALUES(?,?,?,?)", alumnos)
cursor.execute("SELECT * FROM alumno")
alumnitos = cursor.fetchall()
print(alumnitos)

#Cambiando el nombre de la tabla
#renombrar = "ALTER TABLE alumno RENAME TO etudiant"
#cursor.execute(renombrar)

conexion.commit()
conexion.close()