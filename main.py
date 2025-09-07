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
plataformas = [
    pg.Rect(0, 670, 1280, 50),  # Suelo
    pg.Rect(500, 600, 280, 50)
]  

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
    # if key[pg.K_s] == True:
    #     rectPersonaje.y += 5
        
def physics():
    global jumping, VELOCITY_Y
    # Aplicar gravedad solo si no está saltando
    if not jumping and rectPersonaje.y < WINDOW_HEIGHT - personaje.get_height():
        rectPersonaje.y += 5

    # Comprobar colisión después de mover
    idx = rectPersonaje.collidelist(plataformas)
    if idx != -1:
        plataforma = plataformas[idx]
        rectPersonaje.bottom = plataforma.top
        jumping = False
        VELOCITY_Y = JUMP_HEIGHT


def coordenadas_mouse(): 
    point = pg.mouse.get_pos()  
    coordenadas = f"X: {point[0]} Y: {point[1]}"
    pg.display.set_caption(f"Simulador de la Vida I - {coordenadas}")  # Mostramos las coordenadas en el título de la ventana

pg.draw.rect(screen, (0, 0, 255), rectPersonaje) # Dibujamos el rectángulo azul detras del personaje
pg.Rect.update(rectPersonaje, (rectPersonaje.x, rectPersonaje.y), (rectPersonaje.size[0]+70, rectPersonaje.size[1]+70))      
screen.blit(personaje, rectPersonaje)          # Dibujamos el personaje
pg.Rect.update(rectPersonaje, (0,378), personaje.get_size())          # Actualizamos la posición del personaje

while run: 

    screen.fill((255, 255, 255))    # Establecemos el fondo blanco  
    for rect in plataformas:
        pg.draw.rect(screen, (255, 0, 0), rect)  # Dibujamos el rectángulo rojo

    pg.draw.rect(screen, (0, 0, 255), rectPersonaje) # Dibujamos el rectángulo azul detras del personaje
    
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
