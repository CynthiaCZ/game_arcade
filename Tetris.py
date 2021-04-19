import pygame, sys
#Importing key inputs that will be used for sprite navigation
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def drawGrid(gridWidth,gridHeight,blockSize,color,surface):
    for x in range(0, gridWidth, blockSize):
        for y in range(0, gridHeight, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, color, rect, 1)

class block(pygame.sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        super().__init__() #Calling parent class
        self.image = pygame.Surface([w*blockSize, h*blockSize])
        self.image.fill(color)
        pygame.draw.rect(self.image, BLACK, (0,0,w*blockSize,h*blockSize),2)
        self.rect = self.image.get_rect()
        self.rect.x = x*blockSize
        self.rect.y = y*blockSize

    def move(self,direc,mag):
        if (direc == 'L'):
            self.rect.move_ip(-mag,0)
        elif (direc =='R'):
            self.rect.move_ip(mag,0)
        elif (direc == 'D'):
            self.rect.move_ip(0,mag)

    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class piece(pygame.sprite.Group):
    def __init__(self,color,x,y,shape):
        super().__init__()
        self.shape = shape
        self.color = color
        for i in range(4):
            self.add(block(color,x+i,y,1,1)) #drawing I piece

    def move(self,direc):
        for blk in self.sprites():
            mag = 1
            blk.move(direc,mag)
            
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initializing useful variables
blockSize = 40
gridWidth = 10*blockSize
gridHeight = 20*blockSize
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((gridWidth,gridHeight))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")

# Testing out block class
testBlock = block(RED,5,10,1,1)
fullspritelist = pygame.sprite.Group()
fullspritelist.add(testBlock)
fullspritelist.draw(DISPLAYSURF)

# testing out piece class
testPiece = piece(BLUE,3,3,'I')
testPiece.draw(DISPLAYSURF)


# Beginning Game Loop
count = 0
while True:
    count += 1
    print(count) # to make sure not frozen

    if count%5 == 0:
        testBlock.move('D',1)
        testPiece.move('D')
        DISPLAYSURF.fill(WHITE)
        drawGrid(gridWidth,gridHeight,blockSize,BLACK,DISPLAYSURF)
        testPiece.draw(DISPLAYSURF)
        testBlock.draw(DISPLAYSURF)

    # Necessary board updates, from pygame tutorial
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                print('LEFT')
                testBlock.move('L',1*blockSize)
            if event.key == K_RIGHT:
                print('RIGHT')
                testBlock.move('R',1*blockSize)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)

