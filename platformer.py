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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface,(0,0))

    screen.blit(floor_surface,floor_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.colliderect(floor_rect):
        player_rect.bottom = player_rect.bottom
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)