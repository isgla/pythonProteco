import pygame
#Punto de referencia inicial del objeto en pygame es arriba a la izquierda

pygame.init()

altoVentana = 228
anchoVentana = 510

ventana = pygame.display.set_mode((anchoVentana, altoVentana))
fondo = pygame.image.load('Sprites/desierto.png')

#Coordenadas
x = 0
y = 158
anchoDinosaurio = 40
altoDinosaurio = 60

velocidad = 5

juego_corriendo = True
estadoSaltando = False

while juego_corriendo:
	pygame.time.delay(50)
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			juego_corriendo = False

	#Cuando se presiona una tecla, se guarda en tecla
	teclas = pygame.key.get_pressed()

	if teclas[pygame.K_LEFT] and x > velocidad:
		x = x-velocidad
		#x -= velocidad

	if teclas[pygame.K_RIGHT] and x < (anchoVentana-anchoDinosaurio):
		x = x+velocidad

	if teclas[pygame.K_SPACE]:
		estadoSaltando = True


	"""
	if teclas[pygame.K_UP]:
		y = y-velocidad

	if teclas[pygame.K_DOWN]:
		y = y+velocidad
	"""

	ventana.blit(fondo, (0,0))
	pygame.draw.rect(ventana, (82, 213, 163), (x,y, anchoDinosaurio, altoDinosaurio))
	
	pygame.display.update()

pygame.quit()

