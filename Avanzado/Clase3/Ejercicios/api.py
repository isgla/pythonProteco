# pip3 install requests --user

import requests


#get nos regresa un objeto de la clase response
response = requests.get("https://www.google.com")
print(response)

#Imprime Status code 
#<Response [200]> 
# Todos los 200 son éxito, 300 errores de autorización, 
# 400 Error de la petición (bad request), 500 error de servidor


print('-'*30)
print(dir(response))
#Te regresa la dirccion en un json

print('-'*30)
print(response.text)
#Regresa la informacion HTML de la pagina


print('-'*30)
#Búsqueda en Google

#Creamos un diccionario
parametros = {
    "q" : "perritos"       
}
#Crea una nueva llave que se llava parametros (params) asi debe llamarse y se le pasa el nombre del diccionario
response = requests.get("https://www.google.com", params = parametros) 
print(response.text)


print('-'*30)
#Random url

#Usamos una api publica
#regresa informacion falsa de una persona
response = requests.get("https://randomuser.me/api/") 
#Metodo para convertir a diccionario
persona = response.json()
for i in persona:
    print(i, persona[i])




print('-'*30)
for i in range(50):
    response = requests.get("https://randomuser.me/api/") 
    persona = response.json()
    print(persona)


print('-'*30)
#requests.post()
#console.cloud.google.com
response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyCL7zTctHm9qHNOjNA_7unqlqbP10ZANZ8")
#print(response.status_code)
print(response.json())

"""
Si sale bien imprime la direccion predeterminada
{'results': [{'address_components': [{'long_name': '1600', 'short_name': '1600', 'types': ['street_number']}, {'long_name': 'Amphitheatre Parkway', 'short_name': 'Amphitheatre Pkwy', 'types': ['route']}, {'long_name': 'Mountain View', 'short_name': 'Mountain View', 'types': ['locality', 'political']}, {'long_name': 'Santa Clara County', 'short_name': 'Santa Clara County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'California', 'short_name': 'CA', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '94043', 'short_name': '94043', 'types': ['postal_code']}], 'formatted_address': '1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA', 'geometry': {'location': {'lat': 37.4224095, 'lng': -122.0856043}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 37.4237584802915, 'lng': -122.0842553197085}, 'southwest': {'lat': 37.4210605197085, 'lng': -122.0869532802915}}}, 'place_id': 'ChIJtYuu0V25j4ARwu5e4wwRYgE', 'plus_code': {'compound_code': 'CWC7+XQ Mountain View, California, United States', 'global_code': '849VCWC7+XQ'}, 'types': ['street_address']}], 'status': 'OK'}
"""