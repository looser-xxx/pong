import pygame
import evnironmentData as enV

# Create and color the divider surface
dividerSurface = pygame.Surface((10, enV.screenSize[1]))
dividerSurface.fill('white') # Fills the divider with blue

# Get the rect for the divider. Its position is set in the main file.
dividerRect = dividerSurface.get_rect()




playerSurface = pygame.Surface((20,100))
playerSurface.fill('red')
playerRect = playerSurface.get_rect()