#Dinosaurio de google con pygame
# adriana.proteco@gmail.com
import pygame
from time import sleep
#Punto de referencia inicial del objeto en pygame es arriba a la izquierda

"""
Para completar el juego:
Poner varios cactus
Declaras dos números random
Posicios el cactus en esas coordenadas

Eliges un cactus aleatorio
Posicion en x,y aleatorio
"""

#Inicializamos pygame
pygame.init()

altoVentana=228
anchoVentana=510

#Creamos nuestra ventana
ventana =pygame.display.set_mode((anchoVentana,altoVentana))
pygame.display.set_caption("Mi primer juego con Pygame")
reloj = pygame.time.Clock()

#Guardamos en la variable fondo nuestra imagen del desierto
fondo= pygame.image.load('Sprites/desierto.png')

#Declaramos los sprites
spritesDino = [pygame.image.load("Sprites/d1.png"), pygame.image.load("Sprites/d2.png"), pygame.image.load("Sprites/d3.png"), pygame.image.load("Sprites/d4.png")]

gameOver = pygame.image.load("Sprites/game_over.png")
#Declaramos características de dinosaurio: coordenadas (x, y), ancho, alto y velocidad
x= 0
y= 158
anchoDinosaurio=44
altoDinosaurio=53
velocidad= 5

#Cactus
cactus = pygame.image.load("Sprites/cactus.png")
xCactus = 325
yCactus = 160
anchoCactus = 25
altoCactus = 48



#Variable juegoCorriendo que es verdadero mientras estamos jugando
juegoCorriendo= True
#Variable que nos dice si está saltando o no el dinosaurio
estadoSaltando=False
contadorSalto = 10
contadorPasos = 0



#Mientras sea verdadero juegoCorriendo
while juegoCorriendo:
	#pygame.time.delay(50) #Esta línea es temporal luego declararemos un reloj de pygame
    #4 por los sprites
	reloj.tick(12)
	#El 12 en el tick es para pasarle tres veces la misma imagen
	for evento in pygame.event.get(): #recibimos uno por uno los eventos(interacciones con usuario)
		if evento.type == pygame.QUIT: #Si el evento es QUIT (presionar X de ventana)
			juegoCorriendo=False #El juego ya no está corriendo 

	teclas = pygame.key.get_pressed() #Aquí se guardarán las teclas que vayamos presionando

	if teclas[pygame.K_LEFT] and x>velocidad: #x>velocidad sirve para delimitar movimiento del dinosaurio a la ventana
		x= x-velocidad #Para moverlo cambios su coordenada x
		#x-=velocidad
	if teclas[pygame.K_RIGHT] and x<(anchoVentana-anchoDinosaurio):
		x= x+velocidad
	if teclas[pygame.K_SPACE]:
		estadoSaltando=True
	if estadoSaltando == True:
		if contadorSalto>=-10:
			aux=1
			if contadorSalto<0:
				aux=-1
			y-=(contadorSalto**2)*aux*.35
			contadorSalto-=1
		else:
			estadoSaltando = False
			contadorSalto=10
		contadorPasos += 1
	if contadorPasos>=4:
		contadorPasos=0

	rectanguloDino = pygame.Rect(x,y,anchoDinosaurio, altoDinosaurio)
	rectanguloCactus = pygame.Rect(xCactus, yCactus, anchoCactus, altoCactus)
	if rectanguloDino.colliderect(rectanguloCactus):
		ventana.blit(gameOver, (50,-10))
		pygame.display.update()
		sleep(2)
		juegoCorriendo =False



	ventana.blit(fondo,(0,0)) #Dibujamos el fondo de la ventana
	#Division entera //
	ventana.blit(spritesDino[contadorPasos],(x,y))
	ventana.blit(cactus, (xCactus,yCactus))
	
	
	#pygame.draw.rect(ventana,(82,213,163),(x,y,anchoDinosaurio,altoDinosaurio)) #Dibujamos el dinosaurio (temporalmente un rectangulo)
	#(82,213,163) corresponde al color de nuestro rectangulo en código RGB
	pygame.display.update() #Para que se muestren lo que dibujamos debemos actualizar la pantalla

pygame.quit() #Cerramos pygame
