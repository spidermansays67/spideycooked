import pygame 
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sound Effect Game")
clock=pygame.time.Clock()
FPS=60

White=(255, 255, 255)
Blue=(0, 0, 255)
Gold=(255, 215, 0)
Red=(255, 0, 0)

jump_sound = pygame.mixer.Sound("jump.wav")
coin_sound = pygame.mixer.Sound("coin.wav")
hit_sound = pygame.mixer.Sound("hit.wav")

player=pygame.Rect(100, HEIGHT -60,40,40)
player_y_velocity=0 
gravity=0.5
is_jumping=False 

coin=pygame.Rect(500, HEIGHT -60,30,30)
obstacle=pygame.Rect(300, HEIGHT -60,50,50)
collected=False
hit=False

running=True
while running: 
    screen.fill(White)
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            running=False 
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping: 
        player_y_velocity=-10 
        is_jumping=True 
        jump_sound.play()
    player_y_velocity+=gravity 
    player.y+=int(player_y_velocity)

    if player.y>= HEIGHT -60: 
        player.y=HEIGHT -60 
        player_y_velocity=0 
        is_jumping=False

    if not collected and player.colliderect(coin): 
        collected=True 
        coin_sound.play()
    if not hit and player.colliderect(obstacle):
        hit=True
        hit_sound.play()
    pygame.draw.rect(screen, Blue, player) 
    if not collected:
        pygame.draw.ellipse(screen,Gold, coin)
    if not hit:
        pygame.draw.rect(screen, Red, obstacle)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
