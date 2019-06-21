import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
alumnos = [('Derek',21,456789,6), ('Adri',19,563478,10), ('Adri',19,563478,10)]
cursor.executemany("INSERT INTO alumno VALUES(?,?,?,?)", alumnos)
cursor.execute("SELECT * FROM alumno")
alumnitos = cursor.fetchall()
print(alumnitos)
#Cambiando el nombre de la tabla
#renombrar = "ALTER TABLE alumno RENAME TO student"
#cursor.execute(renombrar)

conexion.commit()
conexion.close()