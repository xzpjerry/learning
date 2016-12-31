#!/usr/bin/env/ python

# 1 - Import library
import pygame
from pygame.locals import *
 
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
screen.blit(castle,(0,(height-420)/5))
screen.blit(castle,(0,2*(height-420)/5 + 105))
screen.blit(castle,(0,3*(height-420)/5 + 2*105))
screen.blit(castle,(0,4*(height-420)/5 + 3*105))
# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, (100,100))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)