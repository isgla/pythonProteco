archivo = open("e1.py", "r")

#print(archivo.read())

archivo_salida = open("prueba_salida.txt", "w")
archivo_salida.write("Esta es una prueba de escritura de archivo")
archivo_salida.close()
# Aquí cerramos el flujo de datos

archivo_salida = open("prueba_salida.txt", "w")
archivo_salida.write("Esta es otra linea de prueba")
# Lo volvemos a abrir y a escribir sobre él