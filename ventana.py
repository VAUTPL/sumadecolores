
##################################################
#     UNIVERSIDAD TECNICA PARTICULAR DE LOJA     #
##################################################
# Profesor:            	Rodrigo Barba   	       #
# Rodrigo Barba	     	lrbarba@utpl.edu.ec      #
##################################################
# Estudiante:				                         #
# Ruben Baez     	rubenbaezrivera@gmail.com      # 
# Franz Paccha	        franzpaccha@gmail.com     #
##################################################
# Tema: 				       	                      #
# suma de colores mediante opencv		          #
##################################################

#Import packages needed
import pygame, sys,os
from pygame.locals import * 
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Ventana ejemplo")
ventana = pygame.display.get_surface()

nombre_imagen = os.path.join("images","up2.png")
superficie_imagen = pygame.image.load(nombre_imagen)
ventana.blit(superficie_imagen, (50,50))
pygame.display.flip()

def detectarEventos(eventos): 
   for evento in eventos: 
      if evento.type == QUIT: 
         sys.exit(0) 
         
while True: 
   detectarEventos(pygame.event.get())
