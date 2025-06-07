import pygame
from random import randint
pygame.init()
clock = pygame.time.Clock()
width, height = 500, 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Crossing Game")


# Turtle Crossing
turtle_x_y = [250, 490]
# Number of cars
number_of_cars = 10
car_x_y = []

for i in range(0,number_of_cars):
    car_x_y.append([490, randint(0, 490)])

def get_new_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))
color = []
for i in range(0, number_of_cars):
    color.append(get_new_color())
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                turtle_x_y[1] -= 10


    if turtle_x_y[1] == 0:
        break
    # Clear the screen by filling with black
    window.fill((0,0,0))
    for i in range(0,number_of_cars):
        car_x_y[i][0] -= randint(1,10)
        if car_x_y[i][0] < -30:
            car_x_y[i][0] = 500
            car_x_y[i][1] = randint(0,490)
            color[i] = get_new_color()

    for i in range(0, number_of_cars):
        pygame.draw.rect(window, color[i], (car_x_y[i][0], car_x_y[i][1], 30, 10))
    
    # Making the turtle
    pygame.draw.rect(window,(255, 255, 255), (turtle_x_y[0], turtle_x_y[1], 10, 10))
    pygame.display.flip()
    clock.tick(120)
# Quit Pygame
pygame.quit()