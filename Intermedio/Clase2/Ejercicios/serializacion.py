import json
# json.dump() Convertir diccionarios a json
# json.load() Convertir json a diccionarios
archivo_json = open("clase.json", "r")
diccionario = json.load(archivo_json)
print(diccionario)

diccionario["estatura"] = 1.70
habilidades = diccionario["habilidades"]
habilidades.append("bailar")
print(diccionario)
archivo_json.close()

archivo_json = open("clase.json","w")
json.dump(diccionario, archivo_json, indent=4)





import csv

row = ["Rodrigo", 23, "Vivas"]
#Haces un archivo nuevo
archivo_csv = open("clase.csv","w")

# csv.reader() y csv.writer()

#Writer es el método que primero convierte en lista y te permite ir agregando rows, append a la lista. 
#No necesité poner append y no se sobreescribe.
salida = csv.writer(archivo_csv)
salida.writerow(row)

row = ["Aldo", 21, "Vázquez"]
salida.writerow(row)


archivo_csv.close()


archivo_csv = open("clase.csv", "r")
#Reader es el método que tiene el csv para convertir un archivo en una lista
lector = csv.reader(archivo_csv)
for row in lector:
	print(row)





