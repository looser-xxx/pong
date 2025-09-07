import pygame
import sys
import random
import evnironmentData as enV
import assets
import ballMovement as bm



pygame.init()
pygame.mixer.init()
file=['1.wav','2.wav','3.wav']

padHitSfx=pygame.mixer.Sound('audio/hit/padHit.wav')
bounceHitSfx=pygame.mixer.Sound('audio/hit/bounceHit.wav')
bounceHitSfx.set_volume(0.1)
endFrameSfx=pygame.mixer.Sound('audio/fart/endFart.wav')

# Position the divider rect here, after it has been imported
assets.dividerRect.centerx = enV.screenSize[0] / 2
assets.dividerRect.y = 0

assets.playerRect.centery = enV.screenSize[1] / 2
rightPlayerRect = assets.playerRect.copy()

leftPlayerScore=0
rightPlayerScore=0

toMultiply = bm.d
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    path = 'audio/fart/' + random.choice(file)
    scoreSfx = pygame.mixer.Sound(path)




    # Fill the entire screen with a background color (e.g., black)
    enV.screen.fill((0, 0, 0))

    # Blit the divider onto the main screen using its rect
    enV.screen.blit(assets.dividerSurface, assets.dividerRect)


    keys = pygame.key.get_pressed()


    if keys[pygame.K_w]:
        assets.playerRect.y -= bm.playerSpeed
    if keys[pygame.K_s]:
        assets.playerRect.y += bm.playerSpeed
    if assets.playerRect.bottom > enV.screenSize[1]:
        assets.playerRect.bottom = enV.screenSize[1]
    if assets.playerRect.top < 0:
        assets.playerRect.top = 0

    enV.screen.blit(assets.playerSurface, assets.playerRect)


    if keys[pygame.K_UP]:
        rightPlayerRect.y -= bm.playerSpeed
    if keys[pygame.K_DOWN]:
        rightPlayerRect.y += bm.playerSpeed

    if rightPlayerRect.top < 0:
        rightPlayerRect.top = 0
    if rightPlayerRect.bottom > enV.screenSize[1]:
        rightPlayerRect.bottom = enV.screenSize[1]



    rightPlayerSurface=assets.playerSurface
    rightPlayerRect.right=enV.screenSize[0]
    enV.screen.blit(rightPlayerSurface, rightPlayerRect)



    assets.ballRect.right+=toMultiply[0]
    assets.ballRect.bottom+=toMultiply[1]

    if assets.ballRect.bottom >= enV.screenSize[1] and toMultiply==bm.a:
        print("bottom ",toMultiply)
        bounceHitSfx.play()
        toMultiply=bm.d



    if assets.ballRect.bottom >= enV.screenSize[1] and toMultiply==bm.b:
        print("bottom ",toMultiply)
        bounceHitSfx.play()
        toMultiply=bm.c


    if assets.ballRect.top <= 0 and toMultiply==bm.c:
        print("top ",toMultiply)
        bounceHitSfx.play()
        toMultiply=bm.b

    if assets.ballRect.top <= 0 and toMultiply==bm.d:
        print("top ",toMultiply)
        bounceHitSfx.play()
        toMultiply=bm.a


    if assets.ballRect.left < 20 :
        if assets.playerRect.top<assets.ballRect.midleft[1]<assets.playerRect.bottom:
            padHitSfx.play()
            if toMultiply==bm.b:
                toMultiply = bm.a
            else:
                toMultiply = bm.d
        elif assets.ballRect.right < 0:
            rightPlayerScore+=1
            scoreSfx.play()
            assets.ballRect.center=enV.screenCenter
            toMultiply = bm.d



    if assets.ballRect.right > enV.screenSize[0]-20:
        if rightPlayerRect.top<assets.ballRect.midright[1]<rightPlayerRect.bottom :
            padHitSfx.play()
            if toMultiply==bm.d:
                toMultiply = bm.c
            else:
                toMultiply = bm.b
        elif assets.ballRect.left > enV.screenSize[0]:
            leftPlayerScore+=1
            scoreSfx.play()
            assets.ballRect.center=enV.screenCenter
            toMultiply = bm.c



    enV.screen.blit(assets.ballSurface, assets.ballRect)

    # Render the scores as text surfaces
    leftScoreText = enV.font.render(str(leftPlayerScore), True, (255, 255, 255)) # The color is white
    rightScoreText = enV.font.render(str(rightPlayerScore), True, (255, 255, 255))

    # Blit the scores onto the screen
    enV.screen.blit(leftScoreText, (enV.screenSize[0] / 4, 10))
    enV.screen.blit(rightScoreText, (enV.screenSize[0] * 3 / 4, 10))


    if leftPlayerScore ==bm.toScore or rightPlayerScore ==bm.toScore:
        endFrame=True

        while endFrame:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endFrame = False
            enV.screen.fill((0, 0, 0))
            pygame.display.flip()
            enV.screen.blit(leftScoreText, (enV.screenSize[0] / 4,(enV.screenSize[1] / 2-45)))
            enV.screen.blit(rightScoreText, (enV.screenSize[0] * 3 / 4, (enV.screenSize[1] / 2-45)))
            endFrameSfx.play()




            pygame.display.flip()
            enV.clock.tick(60)

        running=False

    # Update the display to show the changes
    pygame.display.flip()

    # Cap the frame rate
    enV.clock.tick(60)

pygame.quit()

print(leftPlayerScore)
print(rightPlayerScore)

sys.exit()
