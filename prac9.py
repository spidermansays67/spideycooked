import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Level Game with AI Enemy ~~Ruchit Patil 71")
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont("arial", 36)

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)

# Load Sounds
coin_sound = pygame.mixer.Sound("coin.mp3")
gameover_sound = pygame.mixer.Sound("gameover.mp3")

# Player
player_size = 40
player = pygame.Rect(50, HEIGHT - player_size, player_size, player_size)
player_speed = 5

# Enemy (chasing AI)
enemy_size = 40
enemy = pygame.Rect(600, 100, enemy_size, enemy_size)
enemy_speed = 2

# Levels
level = 1
max_levels = 3
coins = []
game_over = False

# Functions
def generate_coins(n=5):
    return [pygame.Rect(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 100), 20, 20) for _ in range(n)]

def reset_level():
    global player, coins, enemy
    player.x, player.y = 50, HEIGHT - player_size
    coins = generate_coins()
    enemy.x = random.randint(WIDTH // 2, WIDTH - 50)
    enemy.y = 100

def draw_text(text, size, color, x, y):
    f = pygame.font.SysFont("arial", size)
    t = f.render(text, True, color)
    rect = t.get_rect(center=(x, y))
    screen.blit(t, rect)

def show_game_over():
    screen.fill(BLACK)
    draw_text("GAME OVER", 64, RED, WIDTH//2, HEIGHT//2 - 40)
    draw_text("Press R to Restart", 32, WHITE, WIDTH//2, HEIGHT//2 + 20)
    pygame.display.flip()

def show_level_up():
    screen.fill(BLACK)
    draw_text(f"Level {level} Complete!", 48, GOLD, WIDTH//2, HEIGHT//2 - 40)
    draw_text("Press any key to continue", 32, WHITE, WIDTH//2, HEIGHT//2 + 20)
    pygame.display.flip()
    pygame.time.wait(500)
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                wait = False

# Coin Initialization
coins = generate_coins()

# Main Loop
running = True
while running:
    if not game_over:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x -= player_speed
        if keys[pygame.K_RIGHT]: player.x += player_speed
        if keys[pygame.K_UP]: player.y -= player_speed
        if keys[pygame.K_DOWN]: player.y += player_speed

        # Stay within screen
        player.x = max(0, min(WIDTH - player_size, player.x))
        player.y = max(0, min(HEIGHT - player_size, player.y))

        # AI Enemy Chase Logic
        dx = player.centerx - enemy.centerx
        dy = player.centery - enemy.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
            enemy.x += dx * enemy_speed
            enemy.y += dy * enemy_speed

        # Coin Collection
        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                coin_sound.play()

        # Collision with enemy
        if player.colliderect(enemy):
            gameover_sound.play()
            game_over = True

        # Check if level complete
        if not coins:
            if level < max_levels:
                level += 1
                show_level_up()
                reset_level()
            else:
                screen.fill(BLACK)
                draw_text("You Win!", 64, GOLD, WIDTH//2, HEIGHT//2)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

        # Draw all elements
        pygame.draw.rect(screen, BLUE, player)
        pygame.draw.rect(screen, RED, enemy)
        for coin in coins:
            pygame.draw.ellipse(screen, GOLD, coin)

        draw_text(f"Level: {level}", 24, BLACK, 70, 30)

    else:
        show_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                level = 1
                game_over = False
                reset_level()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
