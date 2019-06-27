# pip3 install requests --user

import requests
parametros = {
	"q":"perritos"
} 
"""
for i in range(50):
	response = requests.get("https://randomuser.me/api/")
	persona = response.json()
	print(persona)
"""
# requests.post()
# console.cloud.google.com
# developers.google.com

response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyB5tQDTSTcSyCOaN503xtT-dqDZ8gLIDt0")
print(response.json())