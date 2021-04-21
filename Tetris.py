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

colorPiece = {
    'I': (0, 255, 255),
    'J': (0, 0, 255),
    'L': (255, 127, 0),
    'O': (255, 255, 0),
    'S': (0, 255, 0),
    'T': (128, 0, 128),
    'Z': (255, 0, 0)
}

buildPiece = {
    'I':[[0,0],[1,0],[2,0],[3,0]],
    'J':[[0,0],[0,1],[1,1],[2,1]],
    'L':[[0,0],[1,0],[2,0],[2,-1]],
    'O':[[0,0],[0,1],[1,1],[1,0]],
    'S':[[0,0],[1,0],[1,-1],[2,-1]],
    'T':[[0,0],[1,0],[1,-1],[2,0]],
    'Z':[[0,0],[1,0],[1,1],[2,1]],
}

rotatePiece = {
    'I':[[[2,-1],[1,0],[0,1],[-1,2]],
        [[1,2],[0,1],[-1,0],[-2,-1]],
        [[-2,1],[-1,0],[0,-1],[1,-2]],
        [[-1,-2],[0,-1],[1,0],[2,1]]],
        # -------------------------
    'J':[[[2,0],[1,-1],[0,0],[-1,1]],
        [[0,2],[1,1],[0,0],[-1,-1]],
        [[-2,0],[-1,1],[0,0],[1,-1]],
        [[0,-2],[-1,-1],[0,0],[1,1]]],
        # -------------------------
    'L':[[[1,-1],[0,0],[-1,1],[0,2]],
        [[1,1],[0,0],[-1,-1],[-2,0]],
        [[-1,1],[0,0],[1,-1],[0,-2]],
        [[-1,-1],[0,0],[1,1],[2,0]]],
        # -------------------------
    'O':[[[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[0,0],[0,0],[0,0]]],
        # -------------------------
    'S':[[[1,-1],[0,0],[1,1],[0,2]],
        [[1,1],[0,0],[-1,1],[-2,0]],
        [[-1,1],[0,0],[-1,-1],[0,-2]],
        [[-1,-1],[0,0],[1,-1],[2,0]]],
        # -------------------------
    'T':[[[1,-1],[0,0],[1,1],[-1,1]],
        [[1,1],[0,0],[-1,1],[-1,-1]],
        [[-1,1],[0,0],[-1,-1],[1,-1]],
        [[-1,-1],[0,0],[1,-1],[1,1]]],
        # -------------------------
    'Z':[[[2,0],[1,1],[0,0],[-1,1]],
        [[0,2],[-1,1],[0,0],[-1,-1]],
        [[-2,0],[-1,-1],[0,0],[1,-1]],
        [[0,-2],[1,-1],[0,0],[1,1]]]
}

oppDirec = {
    'L':'R',
    'R':'L',
    'U':'D',
    'D':'U'
}

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
        elif (direc == 'U'):
            self.rect.move_ip(0,-mag)

    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class piece(pygame.sprite.Group):
    def __init__(self,shape,x,y):
        super().__init__()
        self.shape = shape
        self.color = colorPiece[shape]
        self.rotation = 0
        for i in range(4):
            self.add(block(self.color,x+buildPiece[shape][i][0],y+buildPiece[shape][i][1],1,1))

    def move(self,direc,mag):
        for blk in self.sprites():
            blk.move(direc,mag)

    def rotate(self,rotation):
        mvmt = rotatePiece[self.shape][rotation]
        i = 0
        for blk in self.sprites():
            blk.rect.move_ip(mvmt[i][0]*blockSize,mvmt[i][1]*blockSize)
            i += 1

    def checkBoundary(self,board,direc,mag):
        self.move(direc,mag)
        for sprite in self.sprites():
            if pygame.sprite.spritecollideany(sprite,board):
                self.move(oppDirec[direc],-mag)
                return True
        return False
            
class board(pygame.sprite.Group):
    def __init__(self,color):
        super().__init__()
        for i in range(gridWidth//blockSize):
            self.add(block(color,i,gridHeight//blockSize-1/blockSize,1,1))
    
    def addPiece(self,piece):
        for blk in piece.sprites():
            self.add(blk)

# Initialize program
pygame.init()
pygame.key.set_repeat(300,150)
 
# Assign FPS a value
FPS = 60
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
gridHeight = (20-1)*blockSize
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((gridWidth,gridHeight))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")

gameBoard = board(BLUE)

count = 0

running = True
for key in buildPiece.keys():
    print(key)
    testPiece = piece(key,3,3)
    running = True

    # Beginning Game Loop
    while running:
        count += 1
        # print(count)

        keys = pygame.key.get_pressed() # checking pressed keys
        if keys[pygame.K_SPACE]:
            running = False
        
        if (count%2)==0:
            if testPiece.checkBoundary(gameBoard,'D',1):
                gameBoard.addPiece(testPiece)
                running = False

        DISPLAYSURF.fill(WHITE)
        drawGrid(gridWidth,gridHeight,blockSize,BLACK,DISPLAYSURF)
        testPiece.draw(DISPLAYSURF)
        gameBoard.draw(DISPLAYSURF)
            
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    testPiece.checkBoundary(gameBoard,'L',blockSize)
                if event.key == K_RIGHT:
                    testPiece.checkBoundary(gameBoard,'R',blockSize)
                if event.key == K_DOWN:
                    testPiece.checkBoundary(gameBoard,'D',3)
                if event.key == K_UP:
                    testPiece.rotate(testPiece.rotation)
                    testPiece.rotation += 1
                    testPiece.rotation = testPiece.rotation % 4
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FramePerSec.tick(FPS)