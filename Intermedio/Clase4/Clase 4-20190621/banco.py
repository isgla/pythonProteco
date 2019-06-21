import sqlite3
conexion = sqlite3.connect("banco.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cliente(cliente_id integer PRIMARY KEY AUTOINCREMENT, nombre varchar(30), edad integer, curp varchar(18))")
cursor.execute("CREATE TABLE IF NOT EXISTS tarjeta(tarjeta_id integer PRIMARY KEY AUTOINCREMENT, numero varchar(16) UNIQUE, clave varchar(3), fecha_vencimiento DATE, cliente_id INTEGER references cliente(cliente_id))")
bandera = True
while bandera:
	try:
		print("Selecciona la opción")
		print("\t1.-Insertar un cliente")
		print("\t2.-Insertar un Tarjeta")
		print("\t3.-Consultar un cliente")
		print("\t4.-Actualizar un cliente")
		print("\t5.-Borrar un cliente")
		print("\t6.-Salir")
		opcion = int(input("\t=>"))
		if opcion == 1:
			nombre = input("Dame el nombre:")
			edad = int(input("Dame la edad:"))
			curp = input("Dame el curp:")
			cursor.execute("INSERT INTO cliente(nombre,edad,curp) VALUES ('%s','%d','%s')"%(nombre, edad, curp))
			print("Dato insertado :)")
			conexion.commit()

		elif opcion == 2:
			numero = input("Dame el número:")
			clave = input("Dame la clave:")
			fecha = input("Dame la fecha en el formato: yyyy/mm/dd")
			cliente = input("Dame el nombre cliente:")
			cursor.execute("SELECT cliente_id from cliente where nombre='%s'"%(cliente))
			num_cliente = cursor.fetchone()
			cursor.execute("INSERT INTO tarjeta(numero,clave, fecha_vencimiento, cliente_id) VALUES ('%s', '%s', DATE(%s,'YYYY/MM/DD'), '%s')"%(numero, clave, fecha, num_cliente[0]))
			print("Dato insertado correctamente :)")
			conexion.commit()

		elif opcion == 3:
			cliente = input("Dame el nombre del cliente a consultar: ")
			cursor.execute("SELECT c.nombre, c.edad, c.curp, t.numero FROM cliente c, tarjeta t WHERE c.cliente_id = t.cliente_id and c.nombre='%s'"%(cliente))
			cliente = cursor.fetchall()
			if cliente != []:
				print("Nombre: ",cliente[0][0])
				print("Edad: ",cliente[0][1])
				print("CURP: ",cliente[0][2])
				print("Numero de tarjeta: ", cliente[0][3])
			else:
				print("NO SE ENCONTRARON DATOS")

		elif opcion == 4:
			nombre = input("Dame el nombre del cliente a actualizar:")
			edad = int(input("Dame la nueva edad:"))
			curp = input("Dame el nuevo CURP")
			cursor.execute("UPDATE cliente SET edad=%d where nombre='%s'"%(edad, nombre))
			cursor.execute("UPDATE cliente SET curp='%s' where nombre='%s'"%(curp, nombre))
			print("Dato actualizado correctamente :)")
			conexion.commit()
		elif opcion == 5:
			nombre = input("Dame el cliente a borrar: ")
			cursor.execute("DELETE FROM cliente where nombre = '%s'"%(nombre))
			print("Cliente eliminado correctamente")
		elif opcion == 6:
			print("Adiós")
			bandera = False
	except Exception:
		print("Error en la ejecución")
conexion.commit()
conexion.close()