import pygame
import random
import sys
from pygments.styles.rainbow_dash import WHITE

import gameSettings as eV


# player class
class Player:
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self.playerSpeed=eV.playerSpeed
        self.playerHeight=eV.playerHeight
        self.playerWidth=eV.playerDepthPercent/100*eV.screenWidth
        self.rect=pygame.FRect(self.x,self.y,self.playerWidth,self.playerHeight)


    def move(self, direction=0):
        if direction==0:
            self.rect.y-=self.playerSpeed
        else:
            self.rect.y+=self.playerSpeed

        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>eV.screenHeight:
            self.rect.bottom=eV.screenHeight


    def draw(self,screen):
        pygame.draw.rect(screen,WHITE, self.rect)



class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.radius=eV.ballRadius
        self.speedX=eV.ballSpeed * random.choice([1,-1])
        self.speedY=eV.ballSpeed * random.choice([1,-1])
        self.rect=pygame.FRect(x-self.radius,y-self.radius,self.radius*2,self.radius*2)

    def draw(self,screen):
        pygame.draw.circle(screen,WHITE, self.rect.center,self.radius)

    def move(self):
        self.rect.x+=self.speedX
        self.rect.y+=self.speedY

    def bounce(self,axis):
        if axis=='y':
            self.speedY*=-1

        if axis=='x':
            self.speedX*=-1


    def reset(self):
        self.rect.center=eV.screenCenter

        self.speedX*=random.choice([1,-1])
        self.speedY*=random.choice([1,-1])


class PongGame:

    def __init__(self):
        pygame.init()

        self.screen=pygame.display.set_mode((eV.screenWidth,eV.screenHeight))
        pygame.display.set_caption('Pong')
        self.clock=pygame.time.Clock()

        self.player1=Player(eV.playerDepthPercent/100*eV.screenWidth,eV.screenHeight/2-eV.playerHeight/2)
        self.computer=Player(eV.screenWidth-(eV.playerDepthPercent/100*eV.screenWidth)*2,eV.screenHeight/2-eV.playerHeight/2)
        self.ball=Ball(eV.screenWidth/2,eV.screenHeight/2)

        self.playerScore=0
        self.computerScore=0
        self.font=pygame.font.SysFont('comicsans',30)

    def playerInput(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player1.move(0)
        if keys[pygame.K_s]:
            self.player1.move(1)

    def computerMovement(self):

        chance = random.randint(1, 100)
        if chance <= eV.difficulty:
            if self.computer.rect.center[1] < self.ball.rect.center[1]:
                self.computer.move(1)
            elif self.computer.rect.center[1] > self.ball.rect.center[1]:
                self.computer.move(0)
        else:
            random_move = random.choice([-1, 0, 1])
            if random_move == -1:
                self.computer.move(1)
            elif random_move == 1:
                self.computer.move(0)







    def collision(self):

        if self.ball.rect.top<0 or self.ball.rect.bottom>eV.screenHeight:
            self.ball.bounce('y')

        if self.ball.rect.colliderect(self.player1.rect) or self.ball.rect.colliderect(self.computer.rect):
            self.ball.bounce('x')


        if self.ball.rect.left < 0:
            self.computerScore+=1
            self.ball.reset()
        if self.ball.rect.right > eV.screenWidth:
            self.playerScore+=1
            self.ball.reset()

    def draw(self):
        self.screen.fill('black')
        pygame.draw.aaline(self.screen,WHITE,(eV.screenWidth/2,0),(eV.screenWidth/2,eV.screenHeight))

        self.player1.draw(self.screen)
        self.computer.draw(self.screen)
        self.ball.draw(self.screen)


        self.screen.blit(self.font.render(str(self.playerScore),True,WHITE),(eV.screenWidth/4,20))
        self.screen.blit(self.font.render(str(self.computerScore), True, WHITE), (eV.screenWidth * 3 / 4, 20))


        pygame.display.flip()

    def runGame(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.playerInput()
            self.computerMovement()
            self.ball.move()
            self.collision()
            self.draw()

if __name__ == "__main__":
    pongGame = PongGame()
    pongGame.runGame()