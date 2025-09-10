"""
Clase que representa a un personaje en el juego, por 
ahora es el unico personaje jugable
"""

import pygame
from config import VELOCITY_Y, JUMP_HEIGHT, GRAVITY, WINDOW_WIDTH, WINDOW_HEIGHT, jumping, COLORS, LIMITE_PANTALLA

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
    


    def dibujar(self, surface, cam_offset):
        jugador_offset = self.rect.move(cam_offset[0], cam_offset[1])
        pygame.draw.rect(surface, (0, 0, 255), jugador_offset, 1) # Hitbox azul del personaje
        surface.blit(self.imagen, jugador_offset)                             # Dibujamos el personaje

    def movimiento(self):
        """Maneja el movimiento del personaje basado en la entrada del teclado"""
        # Salto
        if self.jumping:
            self.rect.y -= self.VELOCITY_Y
            self.VELOCITY_Y -= self.GRAVITY
            if self.VELOCITY_Y < -self.JUMP_HEIGHT:
                self.VELOCITY_Y = self.JUMP_HEIGHT
                self.jumping = False

        # Obtenemos las teclas pulsadas
        # Con onFloor si se desplaza vuelve a comprobarse la gravedad y colisiones
        key = pygame.key.get_pressed()  
        if key[pygame.K_a] == True:
            self.rect.x -= 5
            self.onFloor = False 
        if key[pygame.K_d] == True:
            self.rect.x += 5
            self.onFloor = False 
        if key[pygame.K_w] == True and not self.jumping:
            self.jumping = True
            self.onFloor = False

        """Vamos a definir la interacción de la camara con el personaje"""
        # Centrar la cámara en el eje X del personaje
        posicion_camara = [0, 0]
        if self.tipo == 1:
            # El offset de cámara es la diferencia entre el centro de la pantalla y el centro del personaje
            posicion_camara[0] = (WINDOW_WIDTH // 2) - self.rect.centerx
            # Si quieres centrar también en Y, descomenta la siguiente línea:
            # posicion_camara[1] = (WINDOW_HEIGHT // 2) - self.rect.centery
            return posicion_camara
        


    def fisicas(self, tiles):
        """Aplica la física al personaje, incluyendo gravedad y colisiones. Si ya está en el suelo, hasta que no se desplace en X no vuelve a actuar la gravedad"""
        if not self.jumping and self.rect.y < WINDOW_HEIGHT - self.imagen.get_height() and not self.onFloor:
            self.rect.y += 5
            print("Applying gravity, move detected")

        # Comprobar colisión después de mover
        idx = self.rect.collidelist(tiles)
        if idx != -1:
            plataforma = tiles[idx]
            self.rect.bottom = plataforma.top
            self.jumping = False
            self.VELOCITY_Y = self.JUMP_HEIGHT
            self.onFloor = True
            print("Colide, should be on floor now")