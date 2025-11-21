import pygame

pygame.init()

# screen resolution
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# screen resolution
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#title & icon
pygame.display.set_caption("sneeeyk")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
