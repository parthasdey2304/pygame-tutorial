# importing all the essential modules
import pygame, sys, os
from pygame.locals import *

# setting the colors using RGB values
red = [255, 0, 0]

# initializing pygame
pygame.init()

# setting up pygame window
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Hello this is pygame window")

# setting up a drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

while True:
    pass