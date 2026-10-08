import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity and Bouncing Ball")

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (60, 60))

x = 370
y = 20

velocity = 0
gravity = 0.5
bounce = -0.8

clock = pygame.time.Clock()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    velocity += gravity
    y += velocity

    if y + 60 >= HEIGHT:
        y = HEIGHT - 60
        velocity *= bounce

    screen.blit(background, (0, 0))
    screen.blit(ball, (x, int(y)))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
