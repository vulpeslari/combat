import pygame
from pygame.locals import *
from config import *

pygame.init()

# Set screen
screen = pygame.display.set_mode((sc_width, sc_height))
frames = pygame.time.Clock()

# Drawing Border
pygame.draw.rect(screen, yellow, (0, 100, sc_width, border_width))
pygame.draw.rect(screen, yellow, (0, 100, border_width, sc_height - 100))
pygame.draw.rect(screen, yellow, (0, sc_height - border_width, sc_width, border_width))
pygame.draw.rect(screen, yellow, (sc_width - border_width, 100, border_width, sc_height - 100))

# Drawing other elements
pygame.draw.rect(screen, yellow, (250, (sc_height - 100) // 2 + 100, border_width, 50))

# Drawing tanks
tank1 = pygame.image.load("tank1.png")
tank1_rect = tank1.get_rect()
tank2 = pygame.image.load("tank2.png")
tank2_rect = tank2.get_rect()

# Font
font = pygame.font.Font("PressStart2P.ttf", 80)

while True:
    # Redrawing the scenario
    pygame.draw.rect(screen, yellow, (0, 100, sc_width, border_width))
    pygame.draw.rect(screen, yellow, (0, 100, border_width, sc_height - 100))
    pygame.draw.rect(screen, yellow, (0, sc_height - border_width, sc_width, border_width))
    pygame.draw.rect(screen, yellow, (sc_width - border_width, 100, border_width, sc_height - 100))

    pygame.draw.rect(screen, yellow,
                     (160, ((sc_height - 225) // 2 + 100) - border_width, border_width * 1.2, border_width * 7))
    pygame.draw.rect(screen, yellow,
                     (135, ((sc_height - 225) // 2 + 100) - border_width, border_width, border_width))
    pygame.draw.rect(screen, yellow,
                     (135, ((sc_height + 75) // 2 + 100) - border_width, border_width, border_width))

    pygame.draw.rect(screen, yellow,
                     (830, ((sc_height - 225) // 2 + 100) - border_width, border_width * 1.2, border_width * 7))
    pygame.draw.rect(screen, yellow,
                     (855, ((sc_height - 225) // 2 + 100) - border_width, border_width, border_width))
    pygame.draw.rect(screen, yellow,
                     (855, ((sc_height + 75) // 2 + 100) - border_width, border_width, border_width))

    pygame.draw.rect(screen, yellow,
                     (160, ((sc_height - 440) // 2 + 100) - border_width, border_width * 3.4, border_width * 1.15))
    pygame.draw.rect(screen, yellow,
                     (160, ((sc_height + 300) // 2 + 100) - border_width, border_width * 3.4, border_width * 1.15))
    pygame.draw.rect(screen, yellow,
                     (780, ((sc_height - 440) // 2 + 100) - border_width, border_width * 3.4, border_width * 1.15))
    pygame.draw.rect(screen, yellow,
                     (780, ((sc_height + 300) // 2 + 100) - border_width, border_width * 3.4, border_width * 1.15))

    pygame.draw.rect(screen, yellow,
                     (250, ((sc_height - 100) // 2 + 100) - border_width, border_width * 2, border_width * 2))
    pygame.draw.rect(screen, yellow,
                     (740 - border_width, ((sc_height - 100) // 2 + 100) - border_width, border_width * 2,
                      border_width * 2))

    pygame.draw.rect(screen, yellow,
                     (350, ((sc_height - 350) // 2 + 100) - border_width, border_width * 3, border_width))
    pygame.draw.rect(screen, yellow,
                     (350, ((sc_height - 300) // 2 + 100) - border_width, border_width, border_width * 1))
    pygame.draw.rect(screen, yellow,
                     (350, ((sc_height + 200) // 2 + 100) - border_width, border_width * 3, border_width))
    pygame.draw.rect(screen, yellow,
                     (350, ((sc_height + 150) // 2 + 100) - border_width, border_width, border_width * 1))
    pygame.draw.rect(screen, yellow,
                     (590, ((sc_height - 350) // 2 + 100) - border_width, border_width * 3, border_width))
    pygame.draw.rect(screen, yellow,
                     (640, ((sc_height - 300) // 2 + 100) - border_width, border_width, border_width * 1))
    pygame.draw.rect(screen, yellow,
                     (590, ((sc_height + 200) // 2 + 100) - border_width, border_width * 3, border_width))
    pygame.draw.rect(screen, yellow,
                     (640, ((sc_height + 150) // 2 + 100) - border_width, border_width, border_width * 1))

    pygame.draw.rect(screen, yellow,
                     (480, (sc_height - 50) - border_width, border_width * 2, border_width * 2))
    pygame.draw.rect(screen, yellow,
                     (480, (sc_height - 550) - border_width, border_width * 2, border_width * 2))

    # Updating tanks
    rotated_tank1 = pygame.transform.rotate(tank1, angle)

    screen.blit(rotated_tank1, tank1_position)
    screen.blit(tank2, tank2_position)

    # Drawing the score
    score_format = font.render("{}".format(score_player1), False, green)
    screen.blit(score_format, (225, 10))

    score_format = font.render("{}".format(score_player2), False, blue)
    screen.blit(score_format, (725, 10))

    for event in pygame.event.get():
        # Quits if you close the window
        if event.type == QUIT:
            pygame.display.quit()
            exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if tank1_position[0] >= sc_width - border_width * 4:
                tank1_position[0] = tank1_position[0]
            else:
                tank1_position[0] += 1

        if key[pygame.K_a]:
            angle += 1

        if key[pygame.K_UP]:
            if tank2_position[0] <= 0 - border_width * 1.5:
                tank2_position[0] = tank2_position[0]
            else:
                tank2_position[0] -= 1

        if key[pygame.K_LEFT]:
            pygame.transform.flip(tank2, 100, 100)

    # Screen in loop
    frames.tick(200)
    pygame.display.update()
    screen.fill(red)
