import pygame
from personaje import Personaje
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, PERSONAJE_FILE, COLORS, running, FPS, LIMITE_PANTALLA


class Game:

    def __init__(self):
        pygame.init()

        ### Configuración inicial ###
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        self.jugador = Personaje(150, 297, PERSONAJE_FILE, 1)

        self.plataformas = [
            pygame.Rect(0, 670, 3000, 50),  # Suelo extendido
            pygame.Rect(500, 600, 280, 50),
            pygame.Rect(1500, 600, 400, 50),  # Plataforma adicional lejos a la derecha
            pygame.Rect(2500, 500, 200, 50)   # Otra plataforma aún más lejos
        ]  

        self.running = running
        self.FPS = FPS



    ### Funciones ###
    def draw(self, cam_offset):
        """Dibuja todos los elementos en la pantalla usando el offset de cámara"""
        self.screen.fill(COLORS['WHITE'])    # Establecemos el fondo blanco  
        for plataforma in self.plataformas:
            # Dibujar cada plataforma con el offset de cámara
            plataforma_offset = plataforma.move(cam_offset[0], cam_offset[1])
            pygame.draw.rect(self.screen, COLORS['RED'], plataforma_offset)  # Dibujamos el rectángulo rojo
        # Dibujar el personaje con offset
        jugador_offset = self.jugador.rect.move(cam_offset[0], cam_offset[1])
        pygame.draw.rect(self.screen, (0, 0, 255), jugador_offset)
        self.screen.blit(self.jugador.imagen, jugador_offset)

    def coordenadas_mouse(self): 
        """Muestra las coordenadas del ratón en el título de la ventana"""
        point = pygame.mouse.get_pos()  
        coordenadas = f"X: {point[0]} Y: {point[1]}"
        pygame.display.set_caption(f"Simulador de la Vida I - {coordenadas}")  # Mostramos las coordenadas en el título de la ventana



    ### Ciclo principal ###
    def run(self):
        POSICION_CAMARA = [0, 0]
        while self.running: 
            # Movimiento del personaje y obtención del offset de cámara
            cam_offset = self.jugador.movimiento()
            if cam_offset is not None:
                POSICION_CAMARA = cam_offset
            self.jugador.fisicas(self.plataformas)
            self.coordenadas_mouse() # Al comentar esta linea se pone el titulo definido en la variable CAPTION

            # Dibujo con offset de cámara
            self.draw(POSICION_CAMARA)

            # Manejamos los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Actualizamos la pantalla
            pygame.display.flip()
            self.clock.tick(self.FPS)
