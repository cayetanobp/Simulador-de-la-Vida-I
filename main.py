import pygame
from personaje import Personaje

pygame.init()

### Variables ###
jumping = False
GRAVITY = 1
JUMP_HEIGHT = 15
VELOCITY_Y = JUMP_HEIGHT

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

CAPTION = "Simulador de la Vida I"
PERSONAJE_FILE = "personaje.png"     # Archivo de la imagen del personaje
COLORS = {
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'BLUE': (0, 0, 255),
    'BLACK': (0, 0, 0)
}
run = True
FPS = 60



### Configuración inicial ###
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

jugador = Personaje(150, 297, PERSONAJE_FILE)

plataformas = [
    pygame.Rect(0, 670, 1280, 50),  # Suelo
    pygame.Rect(500, 600, 280, 50)
]  



### Funciones ###
def draw():
    """Dibuja todos los elementos en la pantalla"""
    screen.fill(COLORS['WHITE'])    # Establecemos el fondo blanco  
    for plataforma in plataformas:
        pygame.draw.rect(screen, COLORS['RED'], plataforma)  # Dibujamos el rectángulo rojo
    jugador.dibujar(screen)

def movement():
    """Maneja el movimiento del personaje basado en la entrada del teclado"""
    global VELOCITY_Y, jumping, GRAVITY, JUMP_HEIGHT
    if jumping:
        jugador.rect.y -= VELOCITY_Y
        VELOCITY_Y -= GRAVITY
        if VELOCITY_Y < -JUMP_HEIGHT:
            VELOCITY_Y = JUMP_HEIGHT
            jumping = False

    key = pygame.key.get_pressed()  # Obtenemos las teclas pulsadas
    if key[pygame.K_a] == True:
        jugador.rect.x -= 5
    if key[pygame.K_d] == True:
        jugador.rect.x += 5
    if key[pygame.K_w] == True and not jumping:
        jumping = True
    # if key[pygame.K_s] == True:
    #     jugador.rect.y += 5
        
def physics():
    """Aplica la física al personaje, incluyendo gravedad y colisiones"""
    global jumping, VELOCITY_Y
    # Aplicar gravedad solo si no está saltando
    if not jumping and jugador.rect.y < WINDOW_HEIGHT - jugador.imagen.get_height():
        jugador.rect.y += 5

    # Comprobar colisión después de mover
    idx = jugador.rect.collidelist(plataformas)
    if idx != -1:
        plataforma = plataformas[idx]
        jugador.rect.bottom = plataforma.top
        jumping = False
        VELOCITY_Y = JUMP_HEIGHT
        print("test")


def coordenadas_mouse(): 
    """Muestra las coordenadas del ratón en el título de la ventana"""
    point = pygame.mouse.get_pos()  
    coordenadas = f"X: {point[0]} Y: {point[1]}"
    pygame.display.set_caption(f"Simulador de la Vida I - {coordenadas}")  # Mostramos las coordenadas en el título de la ventana



### Ciclo principal ###
while run: 
    ## Dibujo
    draw()

    ## Movimiento del personaje
    movement()
    physics()
    coordenadas_mouse() # Al comentar esta linea se pone el titulo definido en la variable CAPTION

    ## Manejamos los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ## Actualizamos la pantalla
    pygame.display.flip()
    clock.tick(FPS)
