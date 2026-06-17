import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("platformer")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

background_surface = pygame.Surface((800,400))
background_surface.fill("white")

floor_surface = pygame.Surface((800,20))
floor_surface.fill("black")
floor_rect = floor_surface.get_rect(bottomleft = (0,400))

player_surface = pygame.Surface((30,30))
player_surface.fill("blue")
player_rect = player_surface.get_rect(bottomleft = (150,380))
player_gravity = 0
player_x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if player_rect.y >= 30:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_gravity = -15
        if player_rect.x >= 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player_x = -15
        if player_rect.x <= 800:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player_x = 15



    screen.blit(background_surface,(0,0))

    screen.blit(floor_surface,floor_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.colliderect(floor_rect):
        player_rect.bottom = floor_rect.top
        player_gravity = 0
    if player_rect.x < 0:
        player_x = 0
        player_rect.x = 0
    if player_rect.x > 770:
        player_x = 0
        player_rect.x = 770

    player_x = player_x*0.9
    player_rect.x += player_x
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)