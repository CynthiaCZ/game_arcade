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

class block(pygame.sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        super().__init__() #Calling parent class
        self.image = pygame.Surface([w*blockSize, h*blockSize])
        self.image.fill(color)
        pygame.draw.rect(self.image, BLACK, (0,0,w*blockSize,h*blockSize),2)
        self.rect = self.image.get_rect()
        self.rect.x = x*blockSize
        self.rect.y = y*blockSize
            
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


# Beginning Game Loop
count = 0
while True:
    count += 1
    print(count) # to make sure not frozen

    # Necessary board updates, from pygame tutorial
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)

