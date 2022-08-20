# Importing libraries
import pygame
from pygame.locals import *
pygame.init()

# Defining screen size
screen_width = 1920
screen_height = 1080

# Defining screen object
screen = pygame.display.set_mode((screen_width, screen_height))
blueColor = (66, 93, 245)

# Game title
pygame.display.set_caption('Scotts First Game')

# Setting the background image
background_img = pygame.image.load('/Users/scottschumacker/Desktop/platformer/testbg.jpeg')

# Creating the platforms
platform = pygame.Rect(100,600,300,50)


# Defining run statement for the game to run
run = True
while run:
    screen.blit(background_img, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Insert the platform
    pygame.draw.rect(screen, blueColor, platform)
    
    pygame.display.update()
            
pygame.quit()