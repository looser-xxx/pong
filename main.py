import pygame
import sys
import evnironmentData as enV
import assets
from assets import playerRect

# Position the divider rect here, after it has been imported
assets.dividerRect.centerx = enV.screenSize[0] / 2
assets.dividerRect.y = 0

playerRect.centery = enV.screenSize[1] / 2
rightPlayerRect = playerRect.copy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the entire screen with a background color (e.g., black)
    enV.screen.fill((0, 0, 0))

    # Blit the divider onto the main screen using its rect
    enV.screen.blit(assets.dividerSurface, assets.dividerRect)


    keys = pygame.key.get_pressed()


    if keys[pygame.K_w]:
        playerRect.y -= 5
    if keys[pygame.K_s]:
        playerRect.y += 5
    if playerRect.bottom > enV.screenSize[1]:
        playerRect.bottom = enV.screenSize[1]
    if playerRect.top < 0:
        playerRect.top = 0

    enV.screen.blit(assets.playerSurface, assets.playerRect)


    if keys[pygame.K_UP]:
        rightPlayerRect.y -= 5
    if keys[pygame.K_DOWN]:
        rightPlayerRect.y += 5

    if rightPlayerRect.top < 0:
        rightPlayerRect.top = 0
    if rightPlayerRect.bottom > enV.screenSize[1]:
        rightPlayerRect.bottom = enV.screenSize[1]



    rightPlayerSurface=assets.playerSurface
    rightPlayerRect.right=enV.screenSize[0]
    enV.screen.blit(rightPlayerSurface, rightPlayerRect)

    # Update the display to show the changes
    pygame.display.flip()

    # Cap the frame rate
    enV.clock.tick(60)

pygame.quit()
sys.exit()

