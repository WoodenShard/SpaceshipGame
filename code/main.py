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

        # cooldown

        self.can_shoot: bool = True
        self.laser_shoot_time: int = 0
        self.cooldown_duration: int= 1000

    def laser_timer(self):
        if not self.can_shoot:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot: bool = True
            

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
        playerDirection = self.direction.normalize() if self.direction else self.direction # utilized so while going diagonally we go at the same speed
        self.rect.center += playerDirection * self.speed * dt

        recentKeys = pygame.key.get_just_pressed()
        if recentKeys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf,self.rect.midtop,all_sprites)
            self.can_shoot: bool = False
            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()
 
class Star(pygame.sprite.Sprite):
    
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/star.png').convert_alpha()
        self.rect = self.image.get_frect(center =(randint(0,window_width),randint(0,window_height)))

class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/meteor.png').convert_alpha()
        self.rect = self.image.get_frect(center= (window_width/2, window_height/2))

class Laser(pygame.sprite.Sprite):
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        self.image = surf
        self.rect: pygame.FRect = self.image.get_frect(midbottom = pos)

    def update(self,dt):
        self.rect.centery -= 400 * dt  

laser_surf = pygame.image.load('images/laser.png')

pygame.init()

window_width, window_height = 1280, 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Shooters')
running : bool = True
clock = pygame.time.Clock() # it can control the frame rate

all_sprites = pygame.sprite.Group() # groups can draw update and organize the stripes
player = Player(all_sprites)
for i in range(20):
    Star(all_sprites)
meteor = Meteor(all_sprites)

# meteor event

meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 2000)



while running:
    dt = clock.tick() / 1000 # decides the framerate
    # checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            pass
  
    all_sprites.update(dt)
            
    # Drawing game
    window.fill('darkgray')

    all_sprites.draw(window)

    # updating the screen
    pygame.display.update()


pygame.quit()