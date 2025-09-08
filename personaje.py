"""
Clase que representa a un personaje en el juego, por 
ahora es el unico personaje jugable
"""

import pygame

class Personaje:
    def __init__(self, eje_x, eje_y, imagen_del_personaje):
        ### Cargamos el personaje y estructuras ###
        self.imagen = pygame.image.load(imagen_del_personaje).convert_alpha()    # Cargamos el personaje
        self.rect = self.imagen.get_rect()                            # Hitbox del personaje
        self.rect.center = (eje_x, eje_y)


    def dibujar(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)                # Dibujamos el rectángulo azul detras del personaje
        surface.blit(self.imagen, self.rect)                               # Dibujamos el personaje
