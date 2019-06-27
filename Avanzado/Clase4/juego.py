import pygame, sys
from pygame.locals import *

#Ancho y alto de la ventana
width = 640
height = 480


def main():
	screen = pygame.display.set_mode((width, height))
	#Nombre de la ventana
	pygame.display.set_caption("Prueba pygame")
	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit()
	return 0


#Para ver si estamos en el flujo principal
if __name__ == '__main__':
	pygame.init()
	main()