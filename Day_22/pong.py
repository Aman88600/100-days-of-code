import pygame
from random import randint
pygame.init()
clock = pygame.time.Clock()
width, height = 500, 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Left paddle
left_down_down = False
left_up_down = False
left_paddle_y = 0

# Right Paddle
right_down_down = False
right_up_down = False
right_paddle_y = 0


# ball
ball_x = 240
ball_y = 240
ball_right = True
ball_left = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # For right Paddle
            if event.key == pygame.K_DOWN:
                right_down_down = True
            if event.key == pygame.K_UP:
                right_up_down = True

            # For left Paddle
            if event.key == pygame.K_s:
                left_down_down = True
            if event.key == pygame.K_w:
                left_up_down = True
        if event.type== pygame.KEYUP:

            # For right paddle
            if event.key == pygame.K_DOWN:
                right_down_down = False
            if event.key == pygame.K_UP:
                right_up_down = False

            # For left paddle
            if event.key == pygame.K_s:
                left_down_down = False
            if event.key == pygame.K_w:
                left_up_down = False
    if right_down_down:
        right_paddle_y += 1
    if right_up_down:
        right_paddle_y -= 1
    if left_down_down:
        left_paddle_y += 1
    if left_up_down:
        left_paddle_y -= 1
    window.fill((0, 0, 0))

    pygame.draw.rect(window, (255,255,255), (0,left_paddle_y,10,100))
    pygame.draw.rect(window, (255,255,255), (490, right_paddle_y, 10, 100))

    pygame.draw.rect(window, (255,255,255), (ball_x,ball_y , 10, 10))
    if ball_right:
        ball_x += 1
    elif ball_left:
        ball_x -= 1

    if ball_x == 400:
        ball_right = False
        ball_left = True
    if ball_x == 0:
        ball_right = True
        ball_left = False
    clock.tick(60)
    pygame.display.flip()
# Quit Pygame
pygame.quit()