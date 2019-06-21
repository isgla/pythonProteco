archivo = open("mi_archivo.txt","a")


archivo.write("Esta es una linea de prueba")
archivo.close()

archivo = open("mi_archivo.txt","a")
archivo.write("\n Esta es otra linea de prueba")