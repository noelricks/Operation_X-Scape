import pygame
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((800,400)) ##Screen Size
pygame.display.set_caption('Operation_X-Scape') #Screen name
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)
game_active = True

space_surf = pygame.image.load('images/space.png').convert()
space_surf = pygame.transform.scale(space_surf, (800,400)).convert()

ground_surf = pygame.image.load('images/ground.png')
ground_surf = pygame.transform.scale(ground_surf, (800,100)).convert_alpha()

score_surf = test_font.render('Operation_X-Scape', False, 'White')
score_rect =score_surf.get_rect(center = (400,50))

alien_surf = pygame.image.load('images/alien.png').convert_alpha()
alien_surf = pygame.transform.scale(alien_surf, (100,100)).convert_alpha()
alien_rect = alien_surf.get_rect(bottomright = (750,360))

player_surf = pygame.image.load('images/player.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (150,150)).convert_alpha()
player_rect = player_surf.get_rect(midbottom = (100,345))
player_gravity = 0

##Keeps the windown open 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 325:
                player_gravity = -20

    if game_active:
        screen.blit(space_surf,(0,0))
        screen.blit(ground_surf,(0,325))
        pygame.draw.rect(screen,'Black', score_rect)
        pygame.draw.rect(screen,'Black', score_rect,10)
        screen.blit(score_surf,score_rect)

        alien_rect.x -= 4

        if alien_rect.right <= 0: alien_rect.left = 800
        screen.blit(alien_surf,alien_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 345: player_rect.bottom=345
        screen.blit(player_surf,player_rect)

        #Collision
        if alien_rect.colliderect(player_rect):
            game_active = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            

            if player_rect.colliderect(alien_rect) == 1:
                print('Collision')
            

        pygame.display.update()
        clock.tick(60) #fps control