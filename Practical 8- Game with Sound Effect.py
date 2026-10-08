import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruchit Patil 71")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GOLD = (255, 215, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

jump_sound = pygame.mixer.Sound("fahhh_KcgAXfs.mp3")
coin_sound = pygame.mixer.Sound("aw-hell-nah-man.mp3")
hit_sound = pygame.mixer.Sound("among-us-role-reveal-sound.mp3")

font = pygame.font.Font(None, 40)

player = pygame.Rect(500, HEIGHT - 60, 40, 40)
obstacle = pygame.Rect(300, HEIGHT - 60, 50, 50)
coin = pygame.Rect(600, HEIGHT - 60, 30, 30)

collected = False
hit = False

gravity = 0.5
player_y_velocity = 0
is_jumping = False

speed = 5

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not is_jumping:
        player_y_velocity = -10
        is_jumping = True
        jump_sound.play()

    player_y_velocity += gravity
    player.y += int(player_y_velocity)

    if player.y >= HEIGHT - 60:
        player.y = HEIGHT - 60
        is_jumping = False
        player_y_velocity = 0

    # Move obstacle
    obstacle.x -= speed

    # Move coin
    coin.x -= speed

    # Reset obstacle
    if obstacle.right < 0:
        obstacle.x = WIDTH + 100
        hit = False

    # Reset coin
    if coin.right < 0:
        coin.x = WIDTH + 300
        collected = False

    # Coin collision
    if not collected and player.colliderect(coin):
        collected = True
        coin_sound.play()

    # Obstacle collision
    if not hit and player.colliderect(obstacle):
        hit_sound.play()
        hit = True

        # Restart
        player.x = 500
        player.y = HEIGHT - 60

        obstacle.x = WIDTH + 100
        coin.x = WIDTH + 300

        collected = False
        is_jumping = False
        player_y_velocity = 0

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw coin
    if not collected:
        pygame.draw.ellipse(screen, GOLD, coin)

    # Draw obstacle
    if not hit:
        pygame.draw.rect(screen, RED, obstacle)

    # Collision message
    if hit:
        text = font.render("Collision detected!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 30))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
s