import pygame
import random
import sys


def mimaras_animation():
    mimaras.y += mimaras.dy
    mimaras.x += mimaras.dx

    if mimaras.top <= 0:
        mimaras.top = 0
    if mimaras.left <= 0:
        mimaras.left = 0
    if mimaras.bottom >= SCREEN_HEIGHT:
        mimaras.bottom = SCREEN_HEIGHT
    if mimaras.right >= SCREEN_WIDTH:
        mimaras.right = SCREEN_WIDTH


def thanasis_movement():
    global t0
    global t1

    thanasis.x += thanasis.dx
    thanasis.y += thanasis.dy

    t1 = pygame.time.get_ticks()
    if t1 - t0 >= 1000:
        thanasis.dx *= random.choice((-1, 1))
        thanasis.dy *= random.choice((-1, 1))
        t0 = pygame.time.get_ticks()
    if thanasis.top <= 0:
        thanasis.top = 0
        thanasis.dy *= -1
    if thanasis.bottom >= SCREEN_HEIGHT:
        thanasis.bottom = SCREEN_HEIGHT
        thanasis.dy *= -1
    if thanasis.left <= 0:
        thanasis.left = 0
        thanasis.dx *= -1
    if thanasis.right >= SCREEN_WIDTH:
        thanasis.right = SCREEN_WIDTH
        thanasis.dx *= -1


def main_loop():
    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                mimaras.dy += mimaras.speed
            elif event.key == pygame.K_UP:
                mimaras.dy -= mimaras.speed
            elif event.key == pygame.K_RIGHT:
                mimaras.dx += mimaras.speed
            elif event.key == pygame.K_LEFT:
                mimaras.dx -= mimaras.speed
            elif event.key == pygame.K_r:
                # Reset Game
                # -- Reset Thanos
                thanasis.x = random.randint(20, SCREEN_WIDTH - 50)
                thanasis.y = random.randint(20, SCREEN_HEIGHT - 50)
                thanasis.dx = random.choice((-1, 1)) * thanasis.speed
                thanasis.dy = random.choice((-1, 1)) * thanasis.speed
                # -- Reset Mimaras
                mimaras.x = SCREEN_WIDTH / 2 - 15
                mimaras.y = SCREEN_HEIGHT / 2 - 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                mimaras.dy -= mimaras.speed
            elif event.key == pygame.K_UP:
                mimaras.dy += mimaras.speed
            elif event.key == pygame.K_RIGHT:
                mimaras.dx -= mimaras.speed
            elif event.key == pygame.K_LEFT:
                mimaras.dx += mimaras.speed
        if event.type == pP.PARTICLE_EVENT:
            if mimaras.dx != 0 or mimaras.dy != 0:
                mimaras.add_particles()
            thanasis.add_particles()

    # Game Logic
    mimaras_animation()
    thanasis_movement()

    # Visuals
    screen.fill(bg_color)
    screen.blit(game_label, (SCREEN_WIDTH / 2 - 90, SCREEN_HEIGHT / 2 - 20))

    thanasis.show()
    mimaras.show()

    # Updating the main window
    pygame.display.flip()
    clock.tick(144)


if __name__ == '__main__':
    # General Setup
    pygame.init()
    clock = pygame.time.Clock()

    from Classes import Entity
    from Classes import ParticlePrinciple as pP

    # Main window
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Mimaras movement simulator')
    icon = pygame.image.load(R'icons\crown.png')
    pygame.display.set_icon(icon)

    # SFX
    pygame.mixer.init()
    fart = pygame.mixer.Sound(R'sounds\rigid-fart.wav')
    fart.set_volume(0.3)

    # Colors
    bg_color = pygame.Color('grey12')
    deep_pink = pygame.Color('deeppink')
    light_grey = (200, 200, 200)

    # Players
    entity_list = []

    mimaras = Entity(screen,
                     SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30,
                     light_grey, 'Mimaras')
    mimaras.speed = 10
    mimaras.dx = 0
    mimaras.dy = 0
    entity_list.append(mimaras)

    thanasis = Entity(screen,
                      random.randint(20, SCREEN_WIDTH - 50), random.randint(20, SCREEN_HEIGHT - 50), 30, 30,
                      deep_pink, 'Thanasis')
    thanasis.speed = 4
    thanasis.dx = random.choice((-1, 1)) * thanasis.speed
    thanasis.dy = random.choice((-1, 1)) * thanasis.speed
    entity_list.append(thanasis)

    print('\nEntities: ')
    for entity in entity_list:
        print(entity)

    # Text parameters
    game_font = pygame.font.Font('freesansbold.ttf', 32)
    game_label = game_font.render('Hello guys!', True, light_grey)

    # Time parameters
    t0 = pygame.time.get_ticks()
    t1 = pygame.time.get_ticks()

    # Main game loop
    while True:
        main_loop()
