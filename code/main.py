import pygame
from random import randint

pygame.init()

window_width, window_height = 1280, 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Shooters')
running : bool = True
clock = pygame.time.Clock() # it can control the frame rate


playerSurface = pygame.image.load('images/player.png').convert_alpha()
playerRect = playerSurface.get_frect(center = (window_width/2, window_height/2+300))
playerDirection = pygame.math.Vector2(0,0) # we use Vector2 because we only need x,y if needed x,y,z we use Vector3 (make it as low as possible)
playerSpeed = 300

meteorSurface = pygame.image.load('images/meteor.png').convert_alpha()
meteorRect = meteorSurface.get_frect(center= (window_width/2, window_height/2))

starsSurf = pygame.image.load('images/star.png').convert_alpha()
stars = []
for i in range(20):
    stars.append((randint(0,1280),randint(0,720)))

laserSurface = pygame.image.load('images/laser.png').convert_alpha()
laserRect = laserSurface.get_frect(bottomleft = (20,window_height-20))

while running:
    dt = clock.tick() / 1000 # decides the framerate
    # checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            # pass
        # if event.type == pygame.MOUSEMOTION:
            # playerRect.center = event.pos

    # INPUT
    keys = pygame.key.get_pressed()
    playerDirection.x = int(keys[pygame.K_RIGHT] - int(keys[pygame.K_LEFT]))
    playerDirection.y = int(keys[pygame.K_DOWN] - int(keys[pygame.K_UP]))
    playerDirection = playerDirection.normalize() if playerDirection else playerDirection # utilized so while goine diagonally we go at the same speed
    playerRect.center += playerDirection * playerSpeed *dt

    recentKeys = pygame.key.get_just_pressed()
    if recentKeys[pygame.K_SPACE]:
        print('Si')
            
    # Drawing game
    window.fill('darkgray')
    for pos in stars:
        window.blit(starsSurf, pos)

    window.blit(meteorSurface, meteorRect)
    window.blit(laserSurface, laserRect)
    window.blit(playerSurface, playerRect)

    # updating the screen
    pygame.display.update()


pygame.quit()