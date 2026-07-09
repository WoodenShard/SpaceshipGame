from typing import Any

import pygame
from random import randint,uniform

class Player(pygame.sprite.Sprite):
    

    def __init__(self, groups):
        super().__init__(groups)
        self.image= pygame.image.load('images/player.png').convert_alpha()
        self.rect: pygame.FRect= self.image.get_frect(center=(window_width / 2, window_height / 2 + 300))
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 600

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
    def __init__(self,surf,pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect: pygame.FRect = self.image.get_frect(center = pos)
        self.direction = pygame.math.Vector2(uniform(-0.5,0.5),1)
        self.speed: int = randint(400,500)
    def update(self,dt):
        self.rect.center += 400 * dt * self.direction
        if self.rect.top > window_height:
            self.kill()
        

class Laser(pygame.sprite.Sprite):
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        self.image = surf
        self.rect: pygame.FRect = self.image.get_frect(midbottom = pos)
        self.direction = pygame.math.Vector2()


    def update(self,dt):
        self.rect.centery -= 200 * dt
        if self.rect.bottom <0:
            self.kill()



pygame.init()

window_width, window_height = 1280, 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Shooters')
running : bool = True
clock = pygame.time.Clock() # it can control the frame rate


laser_surf = pygame.image.load('images/laser.png').convert_alpha()
meteor_surf = pygame.image.load('images/meteor.png').convert_alpha()


all_sprites = pygame.sprite.Group() # groups can draw update and organize the stripes
player = Player(all_sprites)
for i in range(20):
    Star(all_sprites)


# meteor event

meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 200)



while running:
    dt = clock.tick() / 1000 # decides the framerate
    position_meteor = pygame.math.Vector2((randint(0,1280),randint(-200,-100)))
    # checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            meteor = Meteor(meteor_surf,position_meteor,all_sprites)
            pass
  
    all_sprites.update(dt)
            
    # Drawing game
    window.fill('darkgray')

    all_sprites.draw(window)

    # updating the screen
    pygame.display.update()


pygame.quit()