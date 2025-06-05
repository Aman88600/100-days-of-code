import pygame
from random import randint
pygame.init()
clock = pygame.time.Clock()
width, height = 500, 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")


# Font setup
font = pygame.font.SysFont(None, 48)  # None = default font, 48 = font size

# Number to display
number = 42
text_color = (255, 255, 255)  # White
bg_color = (0, 0, 0)          # Black

# Render text surface


# Left paddle
left_down_down = False
left_up_down = False
left_paddle_y = 0
left_score = 0

# Right Paddle
right_down_down = False
right_up_down = False
right_paddle_y = 0
right_score = 0


# ball
ball_x = 240
ball_y = 240
ball_right = True
ball_left = False
ball_up = True
ball_down = False


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

    if ball_up:
        ball_y -= 1
    elif ball_down:
        ball_y += 1

    if ball_x == 490:
        if (ball_y > right_paddle_y) and (ball_y < right_paddle_y + 100):
            ball_right = False
            ball_left = True
        else:
            ball_x = 240
            ball_y = 240
            left_score += 1
            print(f"Left Socre = {left_score} Right Score = {right_score}")
            ball_right = False
            ball_left = True
    if ball_x == 10:
        if (ball_y > left_paddle_y) and (ball_y < left_paddle_y + 100):
            ball_right = True
            ball_left = False
        else:
            ball_x = 240
            ball_y = 240
            right_score += 1
            print(f"Left Socre = {left_score} Right Score = {right_score}")
            ball_right = True
            ball_left = False
    if ball_y == 0:
        ball_up = False
        ball_down = True
    if ball_y == 490:
        ball_down = False
        ball_up = True

    text_surface = font.render(str(left_score), True, text_color)
    window.blit(text_surface, (150, 0))

    text_surface = font.render(str(right_score), True, text_color)
    window.blit(text_surface, (350, 0))
    # Dashed Line
    for i in range(25):
        pygame.draw.rect(window, (255,255,255), (240,i * 20, 5, 10))
    clock.tick(120)
    pygame.display.flip()
# Quit Pygame
pygame.quit()