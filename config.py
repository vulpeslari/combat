import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Colors
white = (255,255,255)
yellow = (230, 200, 0)
blue = (0, 0, 255)
red = (230, 0, 0)
green = (0, 150, 0)

# Screen
sc_width = 1000
sc_height = 700
screen = pygame.display.set_mode((sc_width, sc_height))
frames = pygame.time.Clock()

# Borders
border_width = 25

pygame.draw.rect(screen, yellow, (0, 100, sc_width, border_width))
pygame.draw.rect(screen, yellow, (0, 100, border_width, sc_height - 100))
pygame.draw.rect(screen, yellow, (0, sc_height - border_width, sc_width, border_width))
pygame.draw.rect(screen, yellow, (sc_width - border_width, 100, border_width, sc_height - 100))

# Score
score_player1 = 0
score_player2 = 0

# Não consegui ativar a fonte, mas coloquei o arquivo na mesma pasta
font = pygame.font.SysFont("Press Start 2P", 140, True, False)

# Drawing other elements
pygame.draw.rect(screen, yellow, (250, (sc_height-100)//2+100, border_width, 50))

while True:
    # Linhas pra teste (depois eu apago)
    pygame.draw.line(screen, white, (500, 700), (500, 100))
    pygame.draw.line(screen, white, (0, 400), (1000, 400))

    # Redrawing the scenario
    pygame.draw.rect(screen, yellow, (0, 100, sc_width, border_width))
    pygame.draw.rect(screen, yellow, (0, 100, border_width, sc_height - 100))
    pygame.draw.rect(screen, yellow, (0, sc_height - border_width, sc_width, border_width))
    pygame.draw.rect(screen, yellow, (sc_width - border_width, 100, border_width, sc_height - 100))

    pygame.draw.rect(screen, yellow,
                     (250, ((sc_height - 100) // 2 + 100) - border_width, border_width*2, border_width*2))
    pygame.draw.rect(screen, yellow,
                     (750-border_width, ((sc_height - 100) // 2 + 100) - border_width, border_width * 2, border_width * 2))

    score_format = font.render("{}".format(score_player1), False, green)
    screen.blit(score_format, (300, 10))

    score_format = font.render("{}".format(score_player2), False, blue)
    screen.blit(score_format, (600, 10))

    for event in pygame.event.get():
        # Quits if you close the window
        if event.type == QUIT:
            pygame.display.quit()
            exit()

    # Screen in loop
    frames.tick(200)
    pygame.display.update()
    screen.fill(red)
