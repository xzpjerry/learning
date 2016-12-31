#!/usr/bin/env/ python

# 1 - Import library
import pygame
from pygame.locals import *
 
# 2 - Initialize the game
pygame.init()
width, height = 1280, 720
screen=pygame.display.set_mode((width, height))

# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,(height-castle.get_height()*4)/5))
    screen.blit(castle,(0,2*(height-castle.get_height()*4)/5 + castle.get_height()))
    screen.blit(castle,(0,3*(height-castle.get_height()*4)/5 + castle.get_height()*2))
    screen.blit(castle,(0,4*(height-castle.get_height()*4)/5 + castle.get_height()*3))
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