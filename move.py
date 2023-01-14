import pygame

# initializing pygame
pygame.init()

# setting the game screen
screen = pygame.display.set_mode((1000, 700))

# creating tank 1 image
tank1_image = pygame.image.load("tank1.png")

#  inicial position of tank 1
tank1_x = 55
tank1_y = 330

# tank 1 speed
tank1_speed = 50

# rotation angle of tank 1
tank1_angle = 0

# creating tank 2 image
tank2_image = pygame.image.load("tank2.png")

# inicial position of tank 2
tank2_x = 815
tank2_y = 330

# speed of tank 2
tank2_speed = 50

# rotation os tank 2
tank2_angle = 90

# game loop
running = True
while running:
    # fill the screan with black
    screen.fill((0, 0, 0))

    # tank 1 on the screen
    screen.blit(tank1_image, (tank1_x, tank1_y))

    # thank 2 on the screen
    screen.blit(tank2_image, (tank2_x, tank2_y))

    # Rotate the image of tank 1
    rotated_image1 = pygame.transform.rotate(tank1_image, tank1_angle)

    # tank 2 on the screen
    screen.blit(rotated_image1, (tank1_x, tank1_y))

    # rotate the image of tank 2
    rotated_image2 = pygame.transform.rotate(tank2_image, tank2_angle)

    # tank 2 rotated on the screen
    screen.blit(rotated_image2, (tank2_x, tank2_y))

    # keyboard controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tank1_x -= tank1_speed
            elif event.key == pygame.K_RIGHT:
                tank1_x += tank1_speed
            elif event.key == pygame.K_UP:
                tank1_y -= tank1_speed


# quit pygame
pygame.quit()
