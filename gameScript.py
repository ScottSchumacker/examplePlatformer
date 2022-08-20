# Importing libraries
import pygame
from pygame.locals import *
pygame.init()

# Defining screen size
screen_width = 1920
screen_height = 1080

# Defining screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption('Scotts First Game')

# Load images
background_img = pygame.image.load('/Users/scottschumacker/Desktop/platformer/testbg.jpeg')

# Defining run statement for the game to run
run = True
while run:
    screen.blit(background_img, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
            
pygame.quit()