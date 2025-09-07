import pygame

# Initialize Pygame
pygame.init()

# Define screen parameters
screenSize = (800, 600)
screenCenter = (screenSize[0] / 2, screenSize[1] / 2)

# Create the main display surface
screen = pygame.display.set_mode(screenSize)

# Create the clock
clock = pygame.time.Clock()


font = pygame.font.Font(None, 74) # None for the default font, 74 is the font size