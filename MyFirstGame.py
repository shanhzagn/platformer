import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f"{current_time}",False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Square Jump")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0

sky_surface = pygame.Surface((800,400))
sky_surface.fill("darkslategray1")
ground_surface = pygame.Surface((800,60))
ground_surface.fill("saddlebrown")
grass_surface = pygame.Surface((800,10))
grass_surface.fill("green3")
#text_surface = test_font.render("Parkour Jump", False, (64,64,64))
#text_rect = text_surface.get_rect(center = (400,50))

obstacle_surface = pygame.Surface((50,50))
obstacle_surface.fill("azure4")
obstacle_rect = obstacle_surface.get_rect(bottomleft = (800,340))
obstacle_x_pos = 800

player_surface = pygame.Surface((50,50))
player_surface.fill("blue")
player_rect = player_surface.get_rect(bottomleft = (150,340))
player_gravity = 0

player_stand = pygame.Surface((50,50))
player_stand.fill("blue")
player_stand_rect = player_stand.get_rect(center = (400,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if player_rect.bottom == 340:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -11
            if player_rect.collidepoint((pygame.mouse.get_pos())):
                if player_rect.bottom == 340:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player_gravity = -11
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                obstacle_rect = obstacle_surface.get_rect(bottomleft=(800, 340))
                obstacle_x_pos = 800
                player_rect = player_surface.get_rect(bottomleft=(150, 340))
                player_gravity = 0
                start_time = int(pygame.time.get_ticks()/1000)
                game_active = True

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,340))
        screen.blit(grass_surface,(0,340))
        #pygame.draw.rect(screen, "#c0e8ec", text_rect)
        #screen.blit(text_surface,text_rect)
        display_score()

        player_gravity += 0.5
        player_rect.y += player_gravity
        if player_rect.bottom >= 340:
            player_rect.bottom = 340
        screen.blit(player_surface,player_rect)

        obstacle_rect.x -= 5
        if obstacle_rect.right <= 0:
            obstacle_rect.left = 800
        screen.blit(obstacle_surface,obstacle_rect)

        if obstacle_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

    pygame.display.update()
    clock.tick(60)