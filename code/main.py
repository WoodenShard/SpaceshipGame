from typing import Any

import pygame
from random import randint

class Player(pygame.sprite.Sprite):
    

    def __init__(self, groups):
        super().__init__(groups)
        self.image= pygame.image.load('images/player.png').convert_alpha()
        self.rect: pygame.FRect= self.image.get_frect(center=(window_width / 2, window_height / 2 + 300))
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
        playerDirection = self.direction.normalize() if self.direction else self.direction # utilized so while goine diagonally we go at the same speed
        self.rect.center += playerDirection * self.speed * dt

        recentKeys = pygame.key.get_just_pressed()
        if recentKeys[pygame.K_SPACE]:
            print('fire')
 
class Star(pygame.sprite.Sprite):
    
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/star.png').convert_alpha()
        self.rect = self.image.get_frect(center =(randint(0,window_width),randint(0,window_height)))


pygame.init()

window_width, window_height = 1280, 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Shooters')
running : bool = True
clock = pygame.time.Clock() # it can control the frame rate

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)
for i in range(20):
    Star(all_sprites)


meteorSurface = pygame.image.load('images/meteor.png').convert_alpha()
meteorRect = meteorSurface.get_frect(center= (window_width/2, window_height/2))



laserSurface = pygame.image.load('images/laser.png').convert_alpha()
laserRect = laserSurface.get_frect(bottomleft = (20,window_height-20))

while running:
    dt = clock.tick() / 1000 # decides the framerate
    # checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    all_sprites.update(dt)
            
    # Drawing game
    window.fill('darkgray')


    window.blit(meteorSurface, meteorRect)
    window.blit(laserSurface, laserRect)
    all_sprites.draw(window)

    # updating the screen
    pygame.display.update()


pygame.quit()