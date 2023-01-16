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

# Setting sprites
drawGroup = pygame.sprite.Group()
tank1 = pygame.sprite.Sprite(drawGroup)
tank2 = pygame.sprite.Sprite(drawGroup)

# Drawing Tanks
tank1.image = pygame.image.load("tank1.png")
tank2.image = pygame.image.load("tank2.png")
tank1.rect = pygame.rect.Rect(55, 330, 0, 0)
tank2.rect = pygame.rect.Rect(815, 330, 0, 0)

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
    rotated_tank1 = pygame.transform.rotate(tank1.image, angle1)
    rotated_tank2 = pygame.transform.rotate(tank2.image, angle2)

    screen.blit(rotated_tank1, (tank1.rect.x, tank1.rect.y))
    screen.blit(rotated_tank2, (tank2.rect.x, tank2.rect.y))

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

    # Keyboard movements
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if tank1.rect.x >= sc_width - border_width * 4:
                tank1.rect.x = tank1.rect.x
            else:
                tank1.rect.x += 1
            if angle1 > 0:
                tank1.rect.y -= 0.5
            if angle1 < 0:
                tank1.rect.y += 1

        if key[pygame.K_a]:
            angle1 += 0.5
            tank1.rect.x -= 0.5

        if key[pygame.K_d]:
            angle1 -= 0.5
            tank1.rect.x -= 0.3

        if key[pygame.K_UP]:
            if tank2.rect.x <= 0 - border_width * 4:
                tank2.rect.x = tank2.rect.x
            else:
                tank2.rect.x -= 1
            if angle2 > 0:
                tank2.rect.y += 1
            if angle2 < 0:
                tank2.rect.y -= 1

        if key[pygame.K_RIGHT]:
            angle2 -= 0.5
            tank1.rect.x -= 0.3

        if key[pygame.K_LEFT]:
            angle2 += 0.5
            tank2.rect.x -= 0.3

    # Collision with the walls
    def collide(obj):
        if obj.rect.x <= -30:
            obj.rect.x = obj.rect.x + 5

        if obj.rect.y >= 585:
            tank1.rect.y = tank1.rect.y - 5

        if obj.rect.y <= 70:
            obj.rect.y = obj.rect.y + 5

        if obj.rect.x >= 890:
            obj.rect.x = obj.rect.x - 5

    collide(tank1)
    collide(tank2)


    # Screen in loop
    frames.tick(200)
    pygame.display.update()
    screen.fill(red)
