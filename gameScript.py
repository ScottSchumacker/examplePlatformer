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

# Inserting the background and player
background_img = pygame.image.load('/Users/scottschumacker/Desktop/platformer/testbg.jpeg')
character = pygame.image.load('/Users/scottschumacker/Desktop/platformer/character_img.png')
player_x = 300 


# Creating the platforms
platforms = [
pygame.Rect(100,600,300,50),
pygame.Rect(500,600,50,50),
pygame.Rect(700,600, 200, 50),
pygame.Rect(850,400, 200, 50)
]


# Defining run statement for the game to run
run = True
while run:
    screen.blit(background_img, (0,0))
    screen.blit(character, (player_x,300))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= 2
    if keys[pygame.K_d]:
        player_x += 2
    
    # Insert the platform
    for p in platforms:
        pygame.draw.rect(screen, blueColor, p)
    
    pygame.display.update()
            
pygame.quit()