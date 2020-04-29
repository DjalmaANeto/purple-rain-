import pygame, random
from pygame.locals import *

def on_the_grid():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)

def collision(c1, c2):
    return ((c1[0] == c2[0]) and (c1[1] == c2[1]))

# UP = 0
# RIGHT = 1
# DOWN = 2
# LEFT = 3

#inicializando o display
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (200,200), (600,600)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_the_grid()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = K_LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = K_UP
            if event.key == K_DOWN:
                my_direction = K_DOWN
            if event.key == K_LEFT:
                my_direction = K_LEFT
            if event.key == K_RIGHT:
                my_direction = K_RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_the_grid()
        snake.append((0,0))

    for i in range(len(snake) -1, 0, -1):
        snake[1] = (snake[i-1][0], snake[i-1][1])

    if my_direction == K_UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == K_DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == K_RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == K_LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

