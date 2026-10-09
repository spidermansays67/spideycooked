import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Riddhi Utekar 100")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_x = WIDTH // 2
ball_y = 50
radius = 25

velocity_y = 0
gravity = 0.5
bounce = -12


clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    velocity_y += gravity
    ball_y += velocity_y

    if ball_y + radius >= HEIGHT:
        ball_y = HEIGHT - radius
        velocity_y = bounce

    screen.fill(WHITE)

    pygame.draw.circle(
        screen,
        RED,
        (int(ball_x), int(ball_y)),
        radius
    )

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()