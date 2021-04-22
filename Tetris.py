import pygame, sys, random

#Importing key inputs that will be used for sprite navigation
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT,
)

pieceNames = ['I','J','L','O','S','T','Z']

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
    'I':[[0,1],[1,1],[2,1],[3,1]],
    'J':[[0,0],[0,1],[1,1],[2,1]],
    'L':[[0,1],[1,1],[2,1],[2,0]],
    'O':[[0,0],[0,1],[1,1],[1,0]],
    'S':[[0,1],[1,1],[1,0],[2,0]],
    'T':[[0,1],[1,1],[1,0],[2,1]],
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

def drawGrid(gridWidth,gridHeight,blockSize,color,surface):
    for x in range(0, gridWidth, blockSize):
        for y in range(0, gridHeight, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, color, rect, 1)

# def drawContainer(surface,color,x,y):
#     pygame.draw.rect


# def holdPiece(activePiece,heldPiece):
#     if len(heldPiece.sprites()) == 0:
#         heldPiece = piece(activePiece.shape,gridWidth+100,gridHeight/2+100)

class block(pygame.sprite.Sprite):
    def __init__(self, color, x, y, w, h, movable = True):
        super().__init__() #Calling parent class
        self.image = pygame.Surface([w*blockSize, h*blockSize])
        self.image.fill(color)
        pygame.draw.rect(self.image, BLACK, (0,0,w*blockSize-1,h*blockSize-1),2)
        self.rect = self.image.get_rect()
        self.rect.x = x*blockSize
        self.rect.y = y*blockSize
        self.movable = movable

    def move(self,direc,mag):
        if self.movable:
            if (direc == 'L'):
                self.rect.move_ip(-mag,0)
            elif (direc =='R'):
                self.rect.move_ip(mag,0)
            elif (direc == 'D'):
                self.rect.move_ip(0,mag)
            elif (direc == 'U'):
                self.rect.move_ip(0,-mag)
            
    def smoothMove(self,direc):
        if direc == 'L' or direc == 'R':
            if self.rect.x % blockSize != 0:
                self.rect.x = int(round(self.rect.x/blockSize)*blockSize)
                print(self.rect.x)
        if direc == 'D' or direc == 'U':
            if self.rect.y % blockSize != 0:
                self.rect.y = int(round(self.rect.y/blockSize)*blockSize)

    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class piece(pygame.sprite.Group):
    def __init__(self,shape,x,y):
        super().__init__()
        self.shape = shape
        self.color = colorPiece[shape]
        self.rotation = 0
        # yNeg = 0
        for i in range(4):
            self.add(block(self.color,x+buildPiece[shape][i][0],y+buildPiece[shape][i][1],1,1))
        #     if y+buildPiece[shape][i][1]:
        #         yNeg = 1
        # while yNeg:
        #     self.move('D',blockSize)
        #     yNeg = 0
        #     for sprite in self.sprites():
        #         if sprite.rect.y < 0:
        #             yNeg = 1
        

    def move(self,direc,mag):
        for blk in self.sprites():
            blk.move(direc,mag)

    def smoothMove(self,direc):
        for blk in self.sprites():
            blk.smoothMove(direc)

    def movePiece(self,board,direc,mag):
        self.move(direc,mag)
        if self.checkBoundary(board):
            self.move(direc,-mag)
            self.smoothMove(direc)
            return True

    def rotatePiece(self,board,direc):
        self.rotate(direc)
        if self.checkBoundary(board):
            self.rotate(-direc)
            return True

    def rotate(self,direc):
        mag = 1        
        if direc < 0:
            self.rotation += direc
            if self.rotation < 0:
                self.rotation = 3
            mag = -1
        self.rotation = self.rotation % 4
        print(self.rotation)
        mvmt = rotatePiece[self.shape][self.rotation]
        i = 0
        for blk in self.sprites():
            blk.rect.move_ip(mag*mvmt[i][0]*blockSize,mag*mvmt[i][1]*blockSize)
            i += 1
        if direc > 0:
            self.rotation += direc

    def checkBoundary(self,board):
        for sprite in self.sprites():
            if pygame.sprite.spritecollideany(sprite,board):
                return True
        return False

    def fastFall(self,board):
        falling = 1
        while falling:
            if self.movePiece(board,'D',1):
                falling = 0
            
class board(pygame.sprite.Group):
    def __init__(self,color,offsetX=0,offsetY=0):
        super().__init__()
        for i in range(gridWidth//blockSize):
            self.add(block(color,i,gridHeight//blockSize,1,1,False))
        for i in range(gridHeight//blockSize):
            self.add(block(color,gridWidth//blockSize,i,1,1,False))
            self.add(block(color,-1,i,1,1,False))
    
    def addPiece(self,piece):
        yChecks = set()
        for blk in piece.sprites():
            self.add(blk)
            yChecks.add(blk.rect.y)
        print(yChecks)
        self.checkLine(yChecks)
    
    def checkLine(self,checkSet):
        # print('checking line')
        numLineBlocks = gridBlockWidth+2
        
        checkList = sorted(list(checkSet))

        while len(checkList) > 0:
            y = checkList.pop(0)
            checkBlocks = set()
            for sprite in self.sprites():
                if sprite.rect.y == y: # and 0 < sprite.rect.x < gridWidth:
                    checkBlocks.add(sprite)
            if len(checkBlocks) >= numLineBlocks:
                # self.clearLine(checkBlocks)
                for sprite in checkBlocks:
                    if sprite.movable:
                        self.remove(sprite)
                for sprite in self.sprites():
                    if sprite.movable and sprite.rect.y <= y:
                        sprite.move('D',blockSize)

    def clearLine(self,clearSet):
        # print('clearing line')
        for sprite in clearSet:
            self.remove(sprite)
        for sprite in self.sprites():
            if sprite.movable:
                sprite.move('D',blockSize)

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
GRAY = (127,127,127)

# Initializing useful variables
blockSize = 40
gridBlockWidth = 10
gridBlockHeight = 20-1
gridWidth = gridBlockWidth*blockSize
gridHeight = gridBlockHeight*blockSize
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((2*gridWidth,gridHeight))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")

gameBoard = board(GRAY)

count = 0
countSpeed = 50
pieceCount = 0
nextActive = ''
nextHeld = ''

# Important game flags
running = True
createPiece = 1
heldPiece = pygame.sprite.Group()

# Beginning Game Loop
while running:
    count += 1
    # print(count)

    if createPiece:
        # if len(nextActive) > 0:
        #     activePiece = piece(nextActive,3,0)
        # else:
        activePiece = piece(random.choice(pieceNames),3,0)
        # activePiece = piece(pieceNames[pieceCount % len(pieceNames)],3,0)
        pieceCount += 1
        # count = 49
        createPiece = 0

    keys = pygame.key.get_pressed() # checking pressed keys

    if keys[K_DOWN]:
        countSpeed = 25
    else:
        countSpeed = 50
    
    if (count%countSpeed)==0:
        if activePiece.movePiece(gameBoard,'D',blockSize):
            gameBoard.addPiece(activePiece)
            createPiece = 1

    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF,GRAY,pygame.Rect((gridBlockWidth+3)*blockSize,(gridBlockHeight//2+1)*blockSize,6*blockSize,4*blockSize))
    drawGrid(gridWidth,gridHeight,blockSize,BLACK,DISPLAYSURF)
    activePiece.draw(DISPLAYSURF)
    heldPiece.draw(DISPLAYSURF)
    gameBoard.draw(DISPLAYSURF)
    
        
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                activePiece.movePiece(gameBoard,'L',blockSize)
            if event.key == K_RIGHT:
                activePiece.movePiece(gameBoard,'R',blockSize)
            # if event.key == K_DOWN:
            #     activePiece.movePiece(gameBoard,'D',3+5)
            if event.key == K_UP:
                activePiece.rotatePiece(gameBoard,1)
                # activePiece.rotation += 1
                # activePiece.rotation = activePiece.rotation % 4
            if event.key == K_ESCAPE:
                activePiece.rotatePiece(gameBoard,-1)
            if event.key == K_SPACE:
                activePiece.fastFall(gameBoard)
            if event.key == K_RETURN:
                print('HOLDING')
                nextHeld = activePiece.shape
                # if len(heldPiece.sprites()) > 0:
                #     nextActive = heldPiece.shape
                #     createPiece = 1
                heldPiece = piece(nextHeld,gridBlockWidth+4,gridBlockHeight//2+2)
                heldPiece.draw(DISPLAYSURF)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    FramePerSec.tick(FPS)