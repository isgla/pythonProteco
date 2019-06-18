archivo = open("mi_archivo.txt","a")
#La a es de append, para que empiece a escribir de donde se quedó el archivo

archivo.write("Esta es la linea de prueba")
archivo.close()

archivo = open("mi_archivo.txt","a")
archivo.write("\n Esta es otra linea de prueba")