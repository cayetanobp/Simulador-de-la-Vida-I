import pygame
from personaje import Personaje
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, PERSONAJE_FILE, COLORS, running, FPS, LIMITE_PANTALLA, TILE_SIZE, CUADRICULAS_FILE, SUELO_WIDTH, SUELO_EJE_Y


class Game:

    def __init__(self):
        pygame.init()

        ### Configuración inicial ###
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        self.jugador = Personaje(150, 297, PERSONAJE_FILE, 1)

        # Cargar los tiles 
        self.tile_img = pygame.image.load(CUADRICULAS_FILE).convert_alpha()
        self.tile_img = pygame.transform.scale(self.tile_img, (TILE_SIZE, TILE_SIZE))

        # Creamos cada cuadricula y guardamos la lista como instancia de clase
        self.tiles = []
        for x in range(0, SUELO_WIDTH, TILE_SIZE):
            # Vamos a crear un rectangulo por cada tile
            rect = pygame.Rect(x, SUELO_EJE_Y, TILE_SIZE, TILE_SIZE)
            self.tiles.append(rect)

        self.running = running
        self.FPS = FPS



    ### Funciones ###
    def draw(self, cam_offset):
        """Dibuja todos los elementos en la pantalla usando el offset de cámara"""
        self.screen.fill(COLORS['SKYBLUE'])    # Establecemos el fondo azul cielo 

        # Dibujamos los tiles del suelo
        for rect in self.tiles:
            rect_offset = rect.move(cam_offset[0], cam_offset[1])
            self.screen.blit(self.tile_img, rect_offset)

        # Dibujar el personaje con offset
        jugador_offset = self.jugador.rect.move(cam_offset[0], cam_offset[1])
        pygame.draw.rect(self.screen, (0, 0, 255), jugador_offset, 1) # Hitbox azul del personaje
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
            self.jugador.fisicas(self.tiles)
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
