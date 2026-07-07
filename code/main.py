import pygame
from random import randint

# general setup
pygame.init() # always to start pygame
WINDOW_WIDTH, WINDOW_HEIGHT= 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # needs a tuple so doudle (())
pygame.display.set_caption('Space shooter')
running : bool = True

# plain surface
surf = pygame.Surface((100,200)) # creates a surface once again using a tuple
surf.fill('orange') # fills the surface
x = 100

# surface by importing an img
player_surface = pygame.image.load('images/player.png').convert_alpha()
player_rect = player_surface.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
start_surf = pygame.image.load('images/star.png').convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20)]

while running:
    # event loop
    for event in pygame.event.get(): # checks for any event
        if event.type == pygame.QUIT: # if the even is equal to pygame.QUIT then we stop the loop and we close the window
            running : bool = False


    # draw game
    display_surface.fill('darkgray')
    #x += 0.1 on every loop since we are not breaking we will continue to go right
    # display_surface.blit(surf, (x,150))  to display our surface we use this which takes 2 params 1) what to display 2) x,y of where to
    #display_surface.blit(player_surface, (x, 150)) 
    for pos in star_positions:
        display_surface.blit(start_surf, pos)
    
    if player_rect.right < WINDOW_WIDTH:
        player_rect.left += 0.1
    
    display_surface.blit(player_surface, player_rect)
    
    pygame.display.update() # updates all the screen

    # the order in which you fill your screen in is REALLY IMPORTANT

pygame.quit() # making sure it closes correctly since u used pygame.init() 