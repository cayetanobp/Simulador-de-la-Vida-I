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
        
        """
        Vamos a crear el sistema de mapa añadiendo un mapa en este inicializador que vamos a poder cambiar
        cuando queramos, mas adelante se explicara el sistema de mapas
        """

        # Hay un problema con el mapa si se pone "...","##...", ..., ahora mismo tengo sueño por lo que si puedes mirar eso para ponerlo en forma de array
        self.mapa = [
            "...#.....#.................................#.................###..............##...............##..............########################."
        ]

        # Cargar los tiles 
        self.tile_img = pygame.image.load(CUADRICULAS_FILE).convert_alpha()
        self.tile_img = pygame.transform.scale(self.tile_img, (TILE_SIZE, TILE_SIZE))

        # Creamos cada cuadricula y guardamos la lista como instancia de clase
        self.tiles = []

        # Inicializamos el mapa
        self.parser_mapa() 

        self.running = running

    ### Funciones ###

    def parser_mapa(self):
        for fila_idx, fila in enumerate(self.mapa):
            for celda_idx, celda in enumerate(fila):
                x = celda_idx * TILE_SIZE
                y = SUELO_EJE_Y

                # Si la celda es un "." digamos que es el suelo
                if celda == ".":
                    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                    self.tiles.append(rect)
                # Si la celda es un "#" vamos a poner de momento que sea un obstaculo (no es definitivo evidentemente)
                elif celda == "#":
                    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                    rect2 = pygame.Rect(x, y - TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    self.tiles.extend([rect, rect2])
        


    def draw(self, cam_offset):
        """Dibuja todos los elementos en la pantalla usando el offset de cámara"""
        # Fondo
        self.screen.fill(COLORS['SKYBLUE'])    
        
        # Tiles del suelo con offset
        for rect in self.tiles:
            rect_offset = rect.move(cam_offset[0], cam_offset[1])
            self.screen.blit(self.tile_img, rect_offset)

        # Personaje
        self.jugador.dibujar(self.screen, cam_offset)
        

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

            # Coordenadas del raton
            self.coordenadas_mouse() # Al comentar esta linea se pone el titulo definido en la variable CAPTION

            # Dibujo con offset de cámara
            self.draw(POSICION_CAMARA)

            # Manejamos los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Actualizamos la pantalla
            pygame.display.flip()
            self.clock.tick(FPS)
