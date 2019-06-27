#pip3 install requests --user

import requests
import pprint #Imprimir jsons de manera legible

API_TOKEN = "#######"
GEOCODING_URL = "https://maps.gogleapis.com/maps/api/geocode/json"
direccion = input("¿Qué lugar buscar? ")
parametros = {
	"key" : API_TOKEN,
	"address" : direccion
}
response = requests.get(GEOCODING_URL, params=parametros)
#Sirve para debuggear
pprint.pprint(response.text, indent = 4)

#Errores si no encunentra nada (Sirve para)
pprint.pprint(response.json(), indent = 4)




