import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Parkour Jump")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.Surface((800,400))
sky_surface.fill("darkslategray1")
ground_surface = pygame.Surface((800,60))
ground_surface.fill("saddlebrown")
grass_surface = pygame.Surface((800,10))
grass_surface.fill("green3")
text_surface = test_font.render("Parkour Jump", False, "grey0")

obstacle_surface = pygame.Surface((50,50))
obstacle_surface.fill("azure4")
obstacle_x_pos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,340))
    screen.blit(grass_surface,(0,340))
    screen.blit(text_surface,(300,50))
    obstacle_x_pos -= 5
    if obstacle_x_pos <= -50:
        obstacle_x_pos = 800
    screen.blit(obstacle_surface,(obstacle_x_pos,290))



    pygame.display.update()
    clock.tick(60)