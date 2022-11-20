import pygame,sys
import time
import random
pygame.init()

white = (255,255,255)
black = (100,0,0)
red = (255,0,0)
blue = (0,0,255)
window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('slither')

clock = pygame.time.Clock()
FPS = 5
blockSize = 20
noPixel = 0

def myquit():
    pygame.quit()
    sys.exit(0)

font = pygame.font.SysFont(None, 25, bold=True)
def drawGrid():
	sizeGrd = window_width // blockSize

def snake(blockSize, snakelist):

    for size in snakelist:
        pygame.draw.rect(gameDisplay, blue,[size[0]+5,size[1],blockSize,blockSize],2)

def message1(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/2, window_height/2])
def message2(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/3, window_height/3])

def gameLoop():
    gameExit = False
    gameOver = False

    leadX = window_width/2
    leadY = window_height/2

    changePixelsX = 0
    changePixelsY = 0

    snakelist = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0


    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message2("Game over",red)
            message1("press c to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN
                
                if leftArrow:
                    changePixelsX = -blockSize
                    changePixelsY = noPixel
                elif rightArrow:
                    changePixelsX = blockSize
                    changePixelsY = noPixel
                elif upArrow:
                    changePixelsY = -blockSize
                    changePixelsX = noPixel
                elif downArrow:
                    changePixelsY = blockSize
                    changePixelsX = noPixel
            if leadX >= window_width or leadX < 0 or leadY >= window_height or leadY < 0:
                gameOver = True
        leadX += changePixelsX
        leadY += changePixelsY
        
        gameDisplay.fill(white)
        AppleThickness = 20
        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.rect(gameDisplay, red, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        allspriteslist = []
        allspriteslist.append(leadX)
        allspriteslist.append(leadY)
        snakelist.append(allspriteslist)
        if len(snakelist) > snakeLength:
            del snakelist[0]
        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True
        snake(blockSize, snakelist)
        pygame.display.update()

        if leadX >= randomAppleX and leadX <= randomAppleX + AppleThickness:
            if leadY >= randomAppleY and leadY <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0
                snakeLength += 1
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()