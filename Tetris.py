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

# ---------------------------------------
#     Useful Dictionaries and Lists
# ---------------------------------------

pieceNames = ['I','J','L','O','S','T','Z']

# RGB values for each piece
colorPiece = {
    'I': (0, 255, 255),
    'J': (0, 0, 255),
    'L': (255, 127, 0),
    'O': (255, 255, 0),
    'S': (0, 255, 0),
    'T': (128, 0, 128),
    'Z': (255, 0, 0)
}

# Blueprint to build each piece object
# Instructions are block positions relative to top left block
buildPiece = {
    'I':[[0,1],[1,1],[2,1],[3,1]],
    'J':[[0,0],[0,1],[1,1],[2,1]],
    'L':[[0,1],[1,1],[2,1],[2,0]],
    'O':[[0,0],[0,1],[1,1],[1,0]],
    'S':[[0,1],[1,1],[1,0],[2,0]],
    'T':[[0,1],[1,1],[1,0],[2,1]],
    'Z':[[0,0],[1,0],[1,1],[2,1]],
}

# Instructions for rotating pieces clockwise
# Instructions must follow specific order (0,1,2,3)
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

# ---------------------------------------
#        Local Functions (for UI)
# ---------------------------------------

def drawGrid(gridWidth,gridHeight,blockSize,color,surface):
    for x in range(0, gridWidth, blockSize):
        for y in range(0, gridHeight, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, color, rect, 1)

def drawContainer(surface,color,x,y,w,h):
    pygame.draw.rect(surface,color,pygame.Rect(x*blockSize,y*blockSize,w*blockSize,h*blockSize))

# ---------------------------------------
#       Object Classes and Methods
# ---------------------------------------

# Basic building block, equals one square
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
            
    # Rounds block coordinates to be integer multiples of blockSize
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
    # Build piece as a group of 4 blocks, using build instructions
    def __init__(self,shape,x,y):
        super().__init__()
        self.shape = shape
        self.color = colorPiece[shape]
        self.rotation = 0
        for i in range(4):
            self.add(block(self.color,x+buildPiece[shape][i][0],y+buildPiece[shape][i][1],1,1))

    # Move each block in piece
    def move(self,direc,mag):
        for blk in self.sprites():
            blk.move(direc,mag)

    # Round each block coordinate in piece
    def smoothMove(self,direc):
        for blk in self.sprites():
            blk.smoothMove(direc)

    # Tries to move piece, undo if collision
    def movePiece(self,board,direc,mag):
        self.move(direc,mag)
        if self.checkBoundary(board):
            self.move(direc,-mag)
            self.smoothMove(direc)
            return True

    # Tries to rotate piece, undo if collision
    def rotatePiece(self,board,direc):
        self.rotate(direc)
        if self.checkBoundary(board):
            self.rotate(-direc)
            return True

    # Uses rotation instructions to rotate piece
    # Rotation instructions must follow specific order (0,1,2,3)
    def rotate(self,direc):
        mag = 1        
        # Handle CCW rotation
        if direc < 0:
            self.rotation += direc
            if self.rotation < 0:
                self.rotation = 3
            mag = -1
        self.rotation = self.rotation % 4

        # Reference rotation instructions
        mvmt = rotatePiece[self.shape][self.rotation]

        # Translate each block to appropriate new position
        # In total, this results in a rotation transformation
        i = 0
        for blk in self.sprites():
            blk.rect.move_ip(mag*mvmt[i][0]*blockSize,mag*mvmt[i][1]*blockSize)
            i += 1
        if direc > 0:
            self.rotation += direc

    # Returns true if new piece position has any collisions
    def checkBoundary(self,board):
        for sprite in self.sprites():
            if pygame.sprite.spritecollideany(sprite,board):
                return True
        return False

    # Drops piece as far as it can move vertically
    def fastFall(self,board):
        falling = 1
        while falling:
            if self.movePiece(board,'D',1):
                falling = 0
            
class board(pygame.sprite.Group):
    # Creates border of unmovable blocks around playable grid area
    def __init__(self,color,offsetX=0,offsetY=0):
        super().__init__()
        for i in range(gridWidth//blockSize):
            self.add(block(color,i,gridHeight//blockSize,1,1,False))
        for i in range(gridHeight//blockSize):
            self.add(block(color,gridWidth//blockSize,i,1,1,False))
            self.add(block(color,-1,i,1,1,False))
    
    # Add blocks from activePiece to gameBoard
    def addPiece(self,piece):
        yChecks = set()
        # Collect the nonrepeating y-values of each block
        for blk in piece.sprites():
            self.add(blk)
            yChecks.add(blk.rect.y)
        # Check if any of those y-values have full lines
        self.checkLine(yChecks)
    
    def checkLine(self,checkSet):
        # Target number of blocks to consider a row full
        numLineBlocks = gridBlockWidth+2
        
        # Check rows from top to bottom (hence sort)
        checkList = sorted(list(checkSet))

        while len(checkList) > 0:
            # Check one y-value then remove from queue
            y = checkList.pop(0)

            # Collect the block sprites in that specific row
            checkBlocks = set()
            for sprite in self.sprites():
                if sprite.rect.y == y:
                    checkBlocks.add(sprite)

            # Check if line is full (if it has enough blocks)
            if len(checkBlocks) >= numLineBlocks:
                # Remove any movable block sprites, keep unmovable border blocks
                for sprite in checkBlocks:
                    if sprite.movable:
                        self.remove(sprite)
                # Shift all blocks above that row down by 1 blockSize
                for sprite in self.sprites():
                    if sprite.movable and sprite.rect.y <= y:
                        sprite.move('D',blockSize)

# ---------------------------------------
#           Initialization
# ---------------------------------------

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
pygame.display.set_caption("Shaughn's Tetris Game")

gameBoard = board(GRAY)
nextPiece = piece(random.choice(pieceNames),gridBlockWidth+4,gridBlockHeight//2-1)

count = 0
countSpeed = 50
pieceCount = 0

pauseHold = 0

# Important game flags
running = True
createPiece = 1
heldPiece = pygame.sprite.Group()

# ---------------------------------------
#             Main Game Loop
# ---------------------------------------

# Beginning Game Loop
while running:
    count += 1
    # print(count)

    if createPiece:
        activePiece = piece(nextPiece.shape,3,0)
        nextPiece = piece(random.choice(pieceNames),gridBlockWidth+4,gridBlockHeight//2-1)
        # activePiece = piece(pieceNames[pieceCount % len(pieceNames)],3,0)
        pieceCount += 1
        createPiece = 0

    keys = pygame.key.get_pressed() # checking pressed keys

    if keys[K_DOWN]:
        countSpeed = 25
    else:
        countSpeed = 50
    
    if (count%countSpeed)==0:
        if activePiece.movePiece(gameBoard,'D',blockSize):
            gameBoard.addPiece(activePiece)
            pauseHold = 0
            createPiece = 1
   
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
            if event.key == K_RETURN and not pauseHold:
                print('HOLDING')
                pauseHold = 1
                nextHeld = activePiece.shape
                activePiece.empty()
                
                if len(heldPiece.sprites()) > 0:
                    activePiece = piece(heldPiece.shape,3,0)
                    count = 0
                else:
                    createPiece = 1

                heldPiece = piece(nextHeld,gridBlockWidth+4,gridBlockHeight//2+2)
                activePiece.draw(DISPLAYSURF)
                heldPiece.draw(DISPLAYSURF)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)
    drawContainer(DISPLAYSURF,GRAY,gridBlockWidth+3,gridBlockHeight//2+1,6,4)
    drawContainer(DISPLAYSURF,GRAY,gridBlockWidth+3,gridBlockHeight//2-3,6,4)
    drawGrid(gridWidth,gridHeight,blockSize,BLACK,DISPLAYSURF)
    activePiece.draw(DISPLAYSURF)
    nextPiece.draw(DISPLAYSURF)
    heldPiece.draw(DISPLAYSURF)
    gameBoard.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)