import pygame
from src import player, SpriteSheet

pygame.init()

#seteo de los valores de la pantalla principal
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 790

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#colores utiles
gris = (50, 50, 50)
negro = (0, 0, 0)
blanco = (255, 255, 255)

pygame.display.set_caption('Jueguito')
pygame_icon = pygame.image.load('imagenes/icono.jpg')
pygame.display.set_icon(pygame_icon)

#creacion del fondo

fondo = pygame.image.load('imagenes/Background.png').convert_alpha()

#creacion de las spritesheets para animacion de personaje
master_animacion = []
nombres_animaciones = ['imagenes/player/Run_right.png',
                       'imagenes/player/Run_left.png',
                       'imagenes/player/Idle.png',
                       'imagenes/player/Jump.png']
n_frames_en_animacion = 6
action = 2

last_update = pygame.time.get_ticks()
cooldown_animacion = 100
frame = 0

for animacion in nombres_animaciones:
    temp_img_list = []
    sprite_sheet_1 = pygame.image.load(animacion).convert_alpha()
    sprite_sheet = SpriteSheet.SpriteSheet(sprite_sheet_1)
    for x in range(n_frames_en_animacion):
        temp_img_list.append(sprite_sheet.get_image(x, 96, 96, 3, negro))
    master_animacion.append(temp_img_list)

#JUGADOR
jugador = player.Player()

run = True
while run:

    #actualiza background
    screen.blit(fondo, (0, 0))

    #actualiza la animacion
    current_time = pygame.time.get_ticks()

    if current_time - last_update >= cooldown_animacion:
        frame += 1
        last_update = current_time
        if frame >= len(master_animacion[action]):
            frame = 0

    jugador.draw(screen, master_animacion[action][frame])
    jugador.handle_keys()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and (action != 1):
                action = 1
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (action != 0):
                action = 0
            elif event.key == pygame.K_w and action != 2:
                action = 2

    pygame.display.update()

pygame.quit()