import pygame
from random import randint
pygame.init()
clock = pygame.time.Clock()
width, height = 500, 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Crossing Game")

car_x_y = [490, 100]
def get_new_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))
color = get_new_color()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Clear the screen by filling with black
    window.fill((0,0,0))
    car_x_y[0] -= randint(1,10)
    if car_x_y[0] < -30:
        car_x_y[0] = 500
        car_x_y[1] = randint(0,490)
        color = get_new_color()
    pygame.draw.rect(window, color, (car_x_y[0], car_x_y[1], 30, 10))
    pygame.display.flip()
    clock.tick(120)
# Quit Pygame
pygame.quit()