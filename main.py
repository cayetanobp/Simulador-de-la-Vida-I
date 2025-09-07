import pygame as pg

pg.init()

jumping = False
GRAVITY = 1
JUMP_HEIGHT = 15
VELOCITY_Y = JUMP_HEIGHT

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pg.display.set_caption("Simulador de la Vida I")

personaje = pg.image.load("personaje.png").convert_alpha() # Cargamos el personaje
rectPersonaje = personaje.get_rect()              

### Configuramos una serie de figuras
rect = pg.Rect(0, 670, 1280, 50)  

clock = pg.time.Clock()

run = True

def movement():
    global VELOCITY_Y, jumping, GRAVITY, JUMP_HEIGHT
    if jumping:
        rectPersonaje.y -= VELOCITY_Y
        VELOCITY_Y -= GRAVITY
        if VELOCITY_Y < -JUMP_HEIGHT:
            VELOCITY_Y = JUMP_HEIGHT
            jumping = False

    key = pg.key.get_pressed()  # Obtenemos las teclas pulsadas
    if key[pg.K_a] == True:
        rectPersonaje.x -= 5
    if key[pg.K_d] == True:
        rectPersonaje.x += 5
    if key[pg.K_w] == True and not jumping:
        jumping = True
        
def physics():
    if rectPersonaje.colliderect(rect):  # Colisión del personaje con el rectángulo rojo
        rectPersonaje.y -= 5  # Si colisiona, lo movemos hacia arriba


def coordenadas_mouse(): 
    point = pg.mouse.get_pos()  
    coordenadas = f"X: {point[0]} Y: {point[1]}"
    pg.display.set_caption(f"Simulador de la Vida I - {coordenadas}")  # Mostramos las coordenadas en el título de la ventana

pg.draw.rect(screen, (0, 0, 255), rectPersonaje) # Dibujamos el rectángulo azul detras del personaje
screen.blit(personaje, rectPersonaje)          # Dibujamos el personaje
pg.Rect.update(rectPersonaje, (0,378), personaje.get_size())          # Actualizamos la posición del personaje

while run: 

    screen.fill((255, 255, 255))    # Establecemos el fondo blanco  

    pg.draw.rect(screen, (0, 0, 255), rectPersonaje) # Dibujamos el rectángulo azul detras del personaje
    pg.draw.rect(screen, (255, 0, 0), rect)  # Dibujamos el rectángulo rojo
    
    screen.blit(personaje, rectPersonaje)          # Dibujamos el personaje
    ### Movimiento del personaje
    movement()
    physics()
    coordenadas_mouse()


    
    # Manejamos los eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()               # Actualizamos la pantalla
    clock.tick(60)
