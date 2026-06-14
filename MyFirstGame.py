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
text_surface = test_font.render("Parkour Jump", False, (64,64,64))
text_rect = text_surface.get_rect(center = (400,50))

obstacle_surface = pygame.Surface((50,50))
obstacle_surface.fill("azure4")
obstacle_rect = obstacle_surface.get_rect(bottomleft = (800,340))
obstacle_x_pos = 800

player_surface = pygame.Surface((50,50))
player_surface.fill("blue")
player_rect = player_surface.get_rect(bottomleft = (150,340))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mousedown")
        if event.type == pygame.KEYDOWN
            print("keydown")

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,340))
    screen.blit(grass_surface,(0,340))
    pygame.draw.rect(screen, "#c0e8ec", text_rect)
    screen.blit(text_surface,text_rect)

    # player_rect.y
    screen.blit(player_surface,player_rect)

    obstacle_rect.x -= 5
    if obstacle_rect.right <= 0:
        obstacle_rect.left = 800
    screen.blit(obstacle_surface,obstacle_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("jump")

    #if player_rect.colliderect(obstacle_rect):
    #    print("collision")

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60)