import pygame
from random import randint
pygame.init()
clock = pygame.time.Clock()
width, height = 500, 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# Snake head
movement = {'right' : True, 'left' : False, 'up' : False, 'down' : False}
head_x = 0
head_y = 0

# Food
food_x = randint(0,450)
food_y = randint(0,450)
colide_count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                for i in movement:
                    if i == 'right':
                        movement[i] = True
                    else:
                        movement[i] = False
            elif event.key == pygame.K_LEFT:
                for i in movement:
                    if i == 'left':
                        movement[i] = True
                    else:
                        movement[i] = False
            elif event.key == pygame.K_UP:
                for i in movement:
                    if i == 'up':
                        movement[i] = True
                    else:
                        movement[i] = False
            elif event.key == pygame.K_DOWN:
                for i in movement:
                    if i == 'down':
                        movement[i] = True
                    else:
                        movement[i] = False

    window.fill((30, 30, 30))
    for i in movement:
        if i == "right" and movement[i]:
            head_x += 1
        elif i == "left" and movement[i]:
            head_x -= 1
        elif i == "up" and movement[i]:
            head_y -= 1
        elif i == "down" and movement[i]:
            head_y += 1
    if head_x < 0 or head_x > width:
        break
    if head_y < 0 or head_y > height:
        break
    pygame.draw.rect(window, (255,255,255), (head_x,head_y,10,10))

    # Food
    pygame.draw.rect(window, (255,255,255), (food_x,food_y,10,10))

    # collision
    # Left collision
    if food_x - head_x == 10:
        if food_y - head_y <= 10 and food_y - head_y >= -10:
            colide_count += 1
            food_x = randint(0,450)
            food_y = randint(0,450)
            print(' left colide', colide_count)
    # Right collision
    elif food_x - head_x == -10:
        if food_y - head_y <= 10 and food_y - head_y >= -10:
            colide_count += 1
            food_x = randint(0,450)
            food_y = randint(0,450)
            print('right colide', colide_count)

    # top collision
    elif food_y - head_y == 10:
        if food_x - head_x <= 10 and food_x - head_x >= -10:
            colide_count += 1
            food_x = randint(0,450)
            food_y = randint(0,450)
            print(' top colide', colide_count)

    # bottom collision
    elif food_y - head_y == -10:
        if food_x - head_x <= 10 and food_x - head_x >= -10:
            colide_count += 1
            food_x = randint(0,450)
            food_y = randint(0,450)
            print('bottom colide', colide_count)
    clock.tick(120)
    pygame.display.flip()
# Quit Pygame
pygame.quit()