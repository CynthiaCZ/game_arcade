import pygame as pg
import time

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

#Initializing imported modules
pg.init()

#Defining colors to be used to create background and sprites
black = (0,0,0)
yellow = (255,255,0)
white = (255,255,255)
green = (0,255,0)
darkgreen = (0,128,0)
grey = (128,128,128)
red = (255,0,0)
blue = (0,0,255)

#Defining dimensions of the screen
screen = pg.display.set_mode((750,550))

#Creating list of all sprites in the game (cars, player sprite, and finish line)
fullspritelist = pg.sprite.Group()

#Creating a class "mysprite" and then using __init__ to create an object from this class and initializing its attributes
#Making a circular object that will be called later when making the player's sprite
class mysprite(pg.sprite.Sprite):
    def __init__(self, color, x, y, radius):
        super().__init__() #Calling parent class
        self.image = pg.Surface([x, y])
        self.image.fill(white)
        self.image.set_colorkey(white) #Used to make the rectangle behind the circle transparent
        pg.draw.circle(self.image, color, (x/2, y/2), radius) #Actually drawing the circle
        self.rect = self.image.get_rect() #Getting rectangular object

#Making the sprite using the previously made mysprite class and positioning its starting position
mysprite = mysprite(yellow, 50, 50, 20)
mysprite.rect.x = 0
mysprite.rect.y = 250
fullspritelist.add(mysprite)

#Creating a class "car" and then using __init__ to create an object from this class and initializing its attributes
#Making a rectangular object that will be used to make the moving cars and the finish line
class car(pg.sprite.Sprite):

    def __init__(self, color, x, y):
        super().__init__() #Calling parent class
        self.image = pg.Surface([x, y])
        pg.draw.rect(self.image, color, [0, 0, x, y])
        self.rect = self.image.get_rect()

#Making and positioning the different colors of car, adding them to the full sprite list
redcar = car(red, 60, 100)
redcar.rect.x = 350
redcar.rect.y = 0
fullspritelist.add(redcar)

bluecar = car(blue, 60, 100)
bluecar.rect.x = 200
bluecar.rect.y = 0
fullspritelist.add(bluecar)

greencar = car(green, 60, 100)
greencar.rect.x = 275
greencar.rect.y = 0
fullspritelist.add(greencar)

yellowcar = car(yellow, 60, 100)
yellowcar.rect.x = 350
yellowcar.rect.y = 0
fullspritelist.add(yellowcar)

#Main program while loop
running = True

while running:
    
    #Uses series of if statements to detect keyboard input on the arrow keys or the space bar to reset position if the sprite goes off of the screen
    #get_pressed() is used to store the keyboard input and if statements check which key is pressed
    keypress = pg.key.get_pressed()        
    if keypress[K_LEFT]:
        mysprite.rect.x -= 3
    if keypress[K_RIGHT]:
        mysprite.rect.x += 3
    if keypress[K_UP]:
        mysprite.rect.y -= 3
    if keypress[K_DOWN]:
        mysprite.rect.y += 3
    if keypress[K_SPACE]:
        mysprite.rect.x = 0
        mysprite.rect.y = 250
        fullspritelist.add(mysprite)
    
    #Allows the user to quit the pygame window by exiting out or pressing the escape key
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
