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
floor_rect = floor_surface.get_rect(topleft = (0,380))

end_surface = pygame.Surface((20,20))
end_surface.fill("green")
end_rect = end_surface.get_rect(center=(770,350))

plat1 = pygame.Surface((100,20))
plat1.fill("black")
plat1_rect = plat1.get_rect(center=(-1000,-1000))

plat2 = pygame.Surface((100,20))
plat2.fill("black")
plat2_rect = plat2.get_rect(center=(-1000,-1000))

plat3 = pygame.Surface((100,20))
plat3.fill("black")
plat3_rect = plat3.get_rect(center=(-1000,-1000))

plat4 = pygame.Surface((100,20))
plat4.fill("black")
plat4_rect = plat4.get_rect(center=(-1000,-1000))

player_surface = pygame.Surface((30,30))
player_surface.fill("blue")
player_rect = player_surface.get_rect(bottomleft = (80,380))
player_gravity = 0
player_x = 0
player_velocity = 0
level = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_rect.y >= 30:
                if player_rect.y == 350:
                    player_gravity = -15
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player_rect = player_surface.get_rect(bottomleft=(80, 380))
            elif event.key == pygame.K_e:
                level = level+1
                player_rect = player_surface.get_rect(bottomleft=(80, 380))

    keys = pygame.key.get_pressed()
    realtime_keys = []
    if player_rect.x >= 0:
        if keys[pygame.K_LEFT]:
            player_x += (-6-player_x*0.7)
    if player_rect.x <= 800:
        if keys[pygame.K_RIGHT]:
            player_x += (6-player_x*0.7)
    player_velocity = abs(player_x)
    #print(player_velocity)

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

    if player_rect.colliderect(end_rect):
        level = level+1
        player_rect = player_surface.get_rect(bottomleft=(80, 380))

    if level == 0:
        end_rect = end_surface.get_rect(center=(770,350))
        screen.blit(end_surface, end_rect)
    elif level == 1:
        end_rect = end_surface.get_rect(center=(50,180))
        plat1_rect = plat1.get_rect(center=(700, 300))
        screen.blit(plat1,plat1_rect)
        plat2_rect = plat2.get_rect(center=(500, 250))
        screen.blit(plat2, plat2_rect)
        plat3_rect = plat3.get_rect(center=(300, 200))
        screen.blit(plat3, plat3_rect)
        plat4_rect = plat4.get_rect(center=(200, 200))
        screen.blit(plat4, plat4_rect)
        screen.blit(end_surface, end_rect)

    pygame.display.update()
    clock.tick(60)