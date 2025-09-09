import pygame
from personaje import Personaje
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, PERSONAJE_FILE, COLORS, running, FPS


class Game:

    def __init__(self):
        pygame.init()

        ### Configuración inicial ###
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        self.jugador = Personaje(150, 297, PERSONAJE_FILE)

        self.plataformas = [
            pygame.Rect(0, 670, 1280, 50),  # Suelo
            pygame.Rect(500, 600, 280, 50)
        ]  

        self.running = running
        self.FPS = FPS



    ### Funciones ###
    def draw(self):
        """Dibuja todos los elementos en la pantalla"""
        self.screen.fill(COLORS['WHITE'])    # Establecemos el fondo blanco  
        for plataforma in self.plataformas:
            pygame.draw.rect(self.screen, COLORS['RED'], plataforma)  # Dibujamos el rectángulo rojo
        self.jugador.dibujar(self.screen)

    def coordenadas_mouse(self): 
        """Muestra las coordenadas del ratón en el título de la ventana"""
        point = pygame.mouse.get_pos()  
        coordenadas = f"X: {point[0]} Y: {point[1]}"
        pygame.display.set_caption(f"Simulador de la Vida I - {coordenadas}")  # Mostramos las coordenadas en el título de la ventana



    ### Ciclo principal ###
    def run(self):
        while self.running: 
            ## Dibujo
            self.draw()

            ## Movimiento del personaje
            self.jugador.movement()
            self.jugador.physics(self.plataformas)
            self.coordenadas_mouse() # Al comentar esta linea se pone el titulo definido en la variable CAPTION

            ## Manejamos los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            ## Actualizamos la pantalla
            pygame.display.flip()
            self.clock.tick(self.FPS)
