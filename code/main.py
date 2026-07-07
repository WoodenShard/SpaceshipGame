import pygame

# general setup
pygame.init() # always to start pygame
WINDOW_WIDTH, WINDOW_HEIGHT= 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # needs a tuple so doudle (())
running : bool = True

while running:
    # event loop
    for event in pygame.event.get(): # checks for any event
        if event.type == pygame.QUIT: # if the even is equal to pygame.QUIT then we stop the loop and we close the window
            running : bool = False


    # draw game