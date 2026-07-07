import pygame
from random import randint

pygame.init()

window_width, window_height = 1280, 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Shooters')
running : bool = True


playerSurface = pygame.image.load('images/player.png').convert_alpha()
playerRect = playerSurface.get_frect(center = (window_width/2, window_height/2+300))
playerDirection : int = 1

meteorSurface = pygame.image.load('images/meteor.png').convert_alpha()
meteorRect = meteorSurface.get_frect(center= (window_width/2, window_height/2))

starsSurf = pygame.image.load('images/star.png').convert_alpha()
stars = []
for i in range(20):
    stars.append((randint(0,1280),randint(0,720)))

laserSurface = pygame.image.load('images/laser.png').convert_alpha()
laserRect = laserSurface.get_frect(bottomleft = (20,window_height-20))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill('darkgray')

    for pos in stars:
        window.blit(starsSurf, pos)



    window.blit(meteorSurface, meteorRect)
    window.blit(laserSurface, laserRect)

    playerRect.x += playerDirection * 0.4
    if playerRect.right > window_width or playerRect.left < 0:
        playerDirection *= -1
    window.blit(playerSurface, playerRect)

    pygame.display.update()


pygame.quit()