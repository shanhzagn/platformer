import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("platformer")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

background_surface = pygame.Surface((800,400))
background_surface.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0,0))

    pygame.display.update()
    clock.tick(60)