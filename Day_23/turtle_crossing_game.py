import pygame
from random import randint
pygame.init()
clock = pygame.time.Clock()
width, height = 500, 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Crossing Game")

car_x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.draw.rect(window, (255, 255, 255), (car_x, 10, 10, 10))
    car_x += 1
    clock.tick(60)
    pygame.display.flip()
# Quit Pygame
pygame.quit()