import pygame
import time
import random


black = (0,0,0)
backgroundColor = (119, 179, 0)
white = (255,255,255)
headColor = (255, 26, 26)
snakeTailColor = (51, 102, 255)

fontName = 'Arial'

pygame.init()
gameDisplay = pygame.display.set_mode((1000,1000))
gameDisplay.fill(backgroundColor)

clock = pygame.time.Clock()

x = 100

while x<880:
    pygame.draw.line(gameDisplay,white,(x,40),(x,880),1)
    x+=20

y = 40

while y<880:
    pygame.draw.line(gameDisplay,white,(100,y),(880,y),1)
    y+=20

#draw the boundary

x = 100
y = 40
while x <= 880:
    pygame.draw.rect(gameDisplay,white,(x,y,20,20))
    x+=20
x = 100
y = 40
while y <= 880:
    pygame.draw.rect(gameDisplay,white,(x,y,20,20))
    y+=20
x = 880
y = 40
while y <= 880:
    pygame.draw.rect(gameDisplay,white,(x,y,20,20))
    y+=20
x = 100
y = 880
while x <= 880:
    pygame.draw.rect(gameDisplay,white,(x,y,20,20))
    x+=20 

#find all squre corners
squareCorners = []
x = 120
while x < 880:
    y = 60
    while y < 880:
        squareCorners.append([x,y])
        y+=20
    x+=20

#Draw the score card

fontobject = pygame.font.SysFont(fontName, 25)
textSurface = fontobject.render('Score: 0',True,black)
gameDisplay.blit(textSurface,(800,930))

fontobject = pygame.font.SysFont(fontName, 25)
textSurface = fontobject.render('Blocks Covered: 0',True,black)
gameDisplay.blit(textSurface,(100,930))

fontobject = pygame.font.SysFont(fontName, 25)
textSurface = fontobject.render('SOLID SNAKE',True,black)
gameDisplay.blit(textSurface,(425,10))

pygame.display.update()

def mainGameLoop():
    snakeHead = [500,440]
    snakeTail = []
    snakeSquareLength = 18
    direction = 'None'
    gameExit = False
    ychange = 0
    xchange = -20
    speedSetting = 1.0
    speedChange = 1.0
    score = 0
    blocksCovered = 0
    scoreText = "Score: {}".format(score)
    #draw first food
    food = random.choice(squareCorners)
    pygame.draw.rect(gameDisplay,black,(food[0]+1,food[1]+1,snakeSquareLength,snakeSquareLength))

    while gameExit is False:
        GameEvents = pygame.event.get()

        for event in GameEvents:
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                
                if event.key == 97 and direction is not 'right':
                    ychange = 0
                    xchange = -20
                    direction = 'left'
                if event.key == 115 and direction is not 'up':
                    ychange = 20
                    xchange = 0
                    direction = 'down'
                if event.key == 100 and direction is not 'left':
                    ychange = 0
                    xchange = 20
                    direction = 'right'
                if event.key == 119 and direction is not 'down':
                    ychange = -20
                    xchange = 0
                    direction = 'up'

        if speedSetting >= 15.0:
            speedSetting = 1.0
            #draw over snake head, then tail
            pygame.draw.rect(gameDisplay,backgroundColor,(snakeHead[0]+1,snakeHead[1]+1,snakeSquareLength,snakeSquareLength))

            for square in snakeTail:
                pygame.draw.rect(gameDisplay,backgroundColor,(square[0]+1,square[1]+1,snakeSquareLength,snakeSquareLength))
            
            if direction is not 'None':
                
                blocksCovered+=1
                blockText = 'Blocks Covered: {}'.format(blocksCovered)
                fontobject = pygame.font.SysFont(fontName, 25)
                textSurface = fontobject.render(blockText,True,black)
                textSurface.fill(backgroundColor)
                gameDisplay.blit(textSurface,(100,930))
                textSurface = fontobject.render(blockText,True,black)
                gameDisplay.blit(textSurface,(100,930))
                
                
                
                #change snake coordinates according to direction
                #change tail
                snakeTail.insert(0,list(snakeHead))
                snakeTail.pop()
                #change head
                snakeHead[0] += xchange
                snakeHead[1] += ychange
                #draw all the snake squares
            pygame.draw.rect(gameDisplay,headColor,(snakeHead[0]+1,snakeHead[1]+1,snakeSquareLength,snakeSquareLength))
            for square in snakeTail:
                pygame.draw.rect(gameDisplay,snakeTailColor,(square[0]+1,square[1]+1,snakeSquareLength,snakeSquareLength))
            #food handling
            if snakeHead[0] == food[0] and snakeHead[1] == food[1] :
                speedChange += 0.1
                #add tail
                if len(snakeTail) != 0:
                    snakeTail.append([snakeTail[-1][0]-xchange, snakeTail[-1][1] - ychange])
                else:
                    snakeTail.append([snakeHead[0] - xchange, snakeHead[1] - ychange])

                #draw food somewhere else

                food = random.choice(squareCorners)
                while food in snakeTail or food is snakeHead:
                    food = random.choice(squareCorners)
                pygame.draw.rect(gameDisplay,black,(food[0]+1,food[1]+1,snakeSquareLength,snakeSquareLength))

                #update score
                score += 10
                scoreText = "Score: {}".format(score)

                fontobject = pygame.font.SysFont(fontName, 25)
                textSurface = fontobject.render(scoreText,True,black)
                textSurface.fill(backgroundColor)
                gameDisplay.blit(textSurface,(800,930))
                fontobject = pygame.font.SysFont(fontName, 25)
                textSurface = fontobject.render(scoreText,True,black)
                gameDisplay.blit(textSurface,(800,930))
            

            if snakeHead in snakeTail:
                pygame.time.wait(1000)
                print('Tail Crash')
                pygame.draw.rect(gameDisplay,backgroundColor,(100,40,800,860))
                
                fontobject = pygame.font.SysFont(fontName, 50)
                textSurface = fontobject.render('GAME OVER!',True,black)
                gameDisplay.blit(textSurface,(350,400))

                fontobject = pygame.font.SysFont(fontName, 40)
                textSurface = fontobject.render('Wall Crash',True,black)
                gameDisplay.blit(textSurface,(410,480))
                
                fontobject = pygame.font.SysFont(fontName, 30)
                textSurface = fontobject.render(blockText,True,black)
                gameDisplay.blit(textSurface,(390,530))

                fontobject = pygame.font.SysFont(fontName, 30)
                textSurface = fontobject.render(scoreText,True,black)
                gameDisplay.blit(textSurface,(390,560))
                gameExit = True

            if snakeHead[0] < 120 or snakeHead[0] > 860 or snakeHead[1] < 60 or snakeHead[1] > 860:
                pygame.time.wait(1000)
                print('Wall Crash')
                pygame.draw.rect(gameDisplay,backgroundColor,(100,40,800,860))
                
                fontobject = pygame.font.SysFont(fontName, 50)
                textSurface = fontobject.render('GAME OVER!',True,black)
                gameDisplay.blit(textSurface,(350,400))

                fontobject = pygame.font.SysFont(fontName, 40)
                textSurface = fontobject.render('Wall Crash',True,black)
                gameDisplay.blit(textSurface,(410,480))
                
                fontobject = pygame.font.SysFont(fontName, 30)
                textSurface = fontobject.render(blockText,True,black)
                gameDisplay.blit(textSurface,(390,530))

                fontobject = pygame.font.SysFont(fontName, 30)
                textSurface = fontobject.render(scoreText,True,black)
                gameDisplay.blit(textSurface,(390,560))
                gameExit = True



        speedSetting += speedChange
        # print(speedSetting)
        pygame.display.update()    
        clock.tick(120)


mainGameLoop()
pygame.time.wait(2000)
pygame.quit()
quit()