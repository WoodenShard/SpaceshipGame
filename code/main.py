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
playerDirection = pygame.math.Vector2(1,1) # we use Vector2 because we only need x,y if needed x,y,z we use Vector3 (make it as low as possible)
playerSpeed = 1000

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill('darkgray')

    for pos in stars:
        window.blit(starsSurf, pos)


    window.blit(meteorSurface, meteorRect)
    window.blit(laserSurface, laserRect)
    

    playerRect.center += playerDirection * playerSpeed * dt
    if playerRect.bottom >= window_height or playerRect.top <= 0:
        playerDirection.y *= -1
    if playerRect.right >= window_width or playerRect.left <= 0:
        playerDirection.x *= -1
    

    window.blit(playerSurface, playerRect)

    pygame.display.update()


pygame.quit()