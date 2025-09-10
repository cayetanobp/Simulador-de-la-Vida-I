jumping = False
GRAVITY = 1
JUMP_HEIGHT = 15
VELOCITY_Y = JUMP_HEIGHT

# Limite de la pantalla para la camara
LIMITE_PANTALLA = 150

# Definición de parametros para las cuadriculas (Tiles)
TILE_SIZE = 50
SUELO_EJE_Y = 670
SUELO_WIDTH = 5000 # Suelo de momento largo porque no esta diseñado el final

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

CAPTION = "Simulador de la Vida I"
PERSONAJE_FILE = "personaje.png"     # Archivo de la imagen del personaje
CUADRICULAS_FILE = "cuadricula_tierra.png"  # Archivo de cada cuadricula del suelo

COLORS = {
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'BLUE': (0, 0, 255),
    'BLACK': (0, 0, 0),
    'SKYBLUE': (81, 209, 246)
}
running = True
FPS = 60