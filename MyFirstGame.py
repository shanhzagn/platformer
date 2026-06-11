import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Parkour Jump")
clock = pygame.time.Clock()

sky_surface = pygame.Surface((800,400))
sky_surface.fill("darkslategray1")
ground_surface = pygame.Surface((800,60))
ground_surface.fill("saddlebrown")
grass_surface = pygame.Surface((800,10))
grass_surface.fill("green3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,340))
    screen.blit(grass_surface,(0,340))

    pygame.display.update()
    clock.tick(60)