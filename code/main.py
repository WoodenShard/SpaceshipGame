import pygame

# general setup
pygame.init() # always to start pygame
WINDOW_WIDTH, WINDOW_HEIGHT= 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # needs a tuple so doudle (())
pygame.display.set_caption('Space shooter')
running : bool = True

# surface

surf = pygame.Surface((100,200)) # creates a surface once again using a tuple

while running:
    # event loop
    for event in pygame.event.get(): # checks for any event
        if event.type == pygame.QUIT: # if the even is equal to pygame.QUIT then we stop the loop and we close the window
            running : bool = False


    # draw game
    display_surface.fill('darkgray')
    display_surface.blit(surf, (100,150)) # to display our surface we use this which takes 2 params 1) what to display 2) x,y of where to
    pygame.display.update() # updates all the screen

pygame.quit() # making sure it closes correctly since u used pygame.init() 