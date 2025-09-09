"""
Clase que representa a un personaje en el juego, por 
ahora es el unico personaje jugable
"""

import pygame
from config import VELOCITY_Y, JUMP_HEIGHT, GRAVITY, WINDOW_HEIGHT, jumping, COLORS

class Personaje:
    def __init__(self, eje_x, eje_y, imagen_del_personaje, tipo):
        ### Cargamos el personaje y estructuras ###
        self.imagen = pygame.image.load(imagen_del_personaje).convert_alpha()    # Cargamos el personaje
        self.rect = self.imagen.get_rect()                            # Hitbox del personaje
        self.rect.center = (eje_x, eje_y)

        self.jumping = jumping
        self.GRAVITY = GRAVITY
        self.JUMP_HEIGHT = JUMP_HEIGHT
        self.VELOCITY_Y = VELOCITY_Y
        self.onFloor = False
        self.tipo = tipo
    


    def dibujar(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)                # Dibujamos el rectángulo azul detras del personaje
        surface.blit(self.imagen, self.rect)                               # Dibujamos el personaje

    def movimiento(self):

        """Vamos a definir la interacción de la camara con el personaje"""
        posicion_camara = [0,0]

        # Debemos saber donde esta el personaje dentro de nuestro espacio
        self.rect.x = self.rect.x + delta_x
        self.rect.y = self.rect.y + delta_y

        if self.tipo == 1:
            # Si el jugador es de tipo 1, quiere decir que es nuestro personaje
            # la camara se moveria de izquierda a darecha, de momento solo existe
            # este tipo pero en un futuro existiran mas
            if self.rect.derecha > (config.WINDOW_WIDTH - config.LIMITE_PANTALLA):

                posicion_camara[0] = (config.WINDOW_WIDTH - config.LIMITE_PANTALLA) - self.rect.derecha
                self.rect.x = config.WINDOW_WIDTH - config.LIMITE_PANTALLA

            if self.rect.izquierda < config.LIMITE_PANTALLA:
                
                posicion_camara[0] = config.LIMITE_PANTALLA - self.rect.izquierda
                self.rect.y = config.LIMITE_PANTALLA
            return posicion_camara



        """Maneja el movimiento del personaje basado en la entrada del teclado"""
        if self.jumping:
            self.rect.y -= self.VELOCITY_Y
            self.VELOCITY_Y -= self.GRAVITY
            if self.VELOCITY_Y < -self.JUMP_HEIGHT:
                self.VELOCITY_Y = self.JUMP_HEIGHT
                self.jumping = False

        key = pygame.key.get_pressed()  # Obtenemos las teclas pulsadas
        if key[pygame.K_a] == True:
            self.rect.x -= 5
            self.onFloor = False # Si se desplaza vuelve a comprobarse la gravedad y colisiones
        if key[pygame.K_d] == True:
            self.rect.x += 5
            self.onFloor = False # Si se desplaza vuelve a comprobarse la gravedad y colisiones
        if key[pygame.K_w] == True and not self.jumping:
            self.jumping = True
            self.onFloor = False # Si se desplaza vuelve a comprobarse la gravedad y colisiones
        


    def fisicas(self, plataformas):
        """Aplica la física al personaje, incluyendo gravedad y colisiones. Si ya está en el suelo, hasta que no se desplace en X no vuelve a actuar la gravedad"""
        if not self.jumping and self.rect.y < WINDOW_HEIGHT - self.imagen.get_height() and not self.onFloor:
            self.rect.y += 5
            print("Applying gravity, move detected")

        # Comprobar colisión después de mover
        idx = self.rect.collidelist(plataformas)
        if idx != -1:
            plataforma = plataformas[idx]
            self.rect.bottom = plataforma.top
            self.jumping = False
            self.VELOCITY_Y = self.JUMP_HEIGHT
            self.onFloor = True
            print("Colide, should be on floor now")