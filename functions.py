import pygame
def draw(screen, plataformas, hitboxPJ, personaje):
    screen.fill((255, 255, 255))    # Establecemos el fondo blanco  
    for rect in plataformas:
        pygame.draw.rect(screen, (255, 0, 0), rect)  # Dibujamos el rectángulo rojo

    pygame.draw.rect(screen, (0, 0, 255), hitboxPJ) # Dibujamos el rectángulo azul detras del personaje

    screen.blit(personaje, hitboxPJ)          # Dibujamos el personaje

def movement():
    global VELOCITY_Y, jumping, GRAVITY, JUMP_HEIGHT
    if jumping:
        hitboxPJ.y -= VELOCITY_Y
        VELOCITY_Y -= GRAVITY
        if VELOCITY_Y < -JUMP_HEIGHT:
            VELOCITY_Y = JUMP_HEIGHT
            jumping = False

    key = pygame.key.get_pressed()  # Obtenemos las teclas pulsadas
    if key[pygame.K_a] == True:
        rectPersonaje.x -= 5
    if key[pygame.K_d] == True:
        rectPersonaje.x += 5
    if key[pygame.K_w] == True and not jumping:
        jumping = True
    # if key[pygame.K_s] == True:
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
        print("test")


def coordenadas_mouse(): 
    point = pygame.mouse.get_pos()  
    coordenadas = f"X: {point[0]} Y: {point[1]}"
    pygame.display.set_caption(f"Simulador de la Vida I - {coordenadas}")  # Mostramos las coordenadas en el título de la ventana
