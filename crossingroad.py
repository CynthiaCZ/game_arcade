#DYLAN INES' GAME

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

#Making a list with all of the moving cars, list will be used to identify collision between sprite and any of the cars
carlist = pg.sprite.Group()
carlist.add(redcar)
carlist.add(bluecar)
carlist.add(greencar)
carlist.add(yellowcar)

#Main program while loop
running = True

counter = 2 #Counter used to enter different if statements so that the different color cars start at different places of the screen

while running:
    redcar.rect.y += 2 #Gives the red car a downward speed of 2
    #Identifies when the car goes off of the bottom of the screen and resets the position to the top of the screen
    if redcar.rect.y > 550:
        redcar.rect.x = 425
        redcar.rect.y = 0
        fullspritelist.add(redcar)
        
    bluecar.rect.y += 2 #Gives the blue car a downward speed of 2
    #Identifies when the car goes off of the bottom of the screen and resets the position to the top of the screen, only enters this statement every
    #other time so the car swithes the lane it is driving in every time
    if bluecar.rect.y > 550 and counter%2 == 0:
        bluecar.rect.x = 425
        bluecar.rect.y = 0
        fullspritelist.add(bluecar)
        counter += 1

    #Identifies when the car goes off of the bottom of the screen and resets the position to the top of the screen, only enters this statement every
    #other time so the car swithes the lane it is driving in every time
    if bluecar.rect.y > 550 and counter%2 != 0:
        bluecar.rect.x = 200
        bluecar.rect.y = 0
        fullspritelist.add(bluecar)
        counter += 1

    greencar.rect.y += 3 #Gives the green car a downward speed of 3
    #Identifies when the car goes off of the bottom of the screen and resets the position to the top of the screen
    if greencar.rect.y > 550:
        greencar.rect.x = 275
        greencar.rect.y = 0
        fullspritelist.add(greencar)

    yellowcar.rect.y += 4 #Gives the green car a downward speed of 4
    #Identifies when the car goes off of the bottom of the screen and resets the position to the top of the screen
    if yellowcar.rect.y > 550:
        yellowcar.rect.x = 350
        yellowcar.rect.y = 0
        fullspritelist.add(yellowcar)
        
    #Using spritecollide to detect collision between mysprite and any of the cars by looping through any collisions between the sprite and cars in the carlist
    for car in pg.sprite.spritecollide(mysprite,carlist,False):
        pg.font.init()
        font = pg.font.SysFont('Calibri', 30) #Sets font
        fontsurface = font.render('You have been hit! Try again', False, white) #Displays "try again" text
        screen.blit(fontsurface, (150,250)) #Positioning text
        pg.display.update() #Updating display to show text
        time.sleep(3) #Sleeps the program for 3 seconds so player can reset and read the text
        mysprite.rect.x = 0
        mysprite.rect.y = 250
        fullspritelist.add(mysprite)
        
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
                
    #Draws the background of the grass and road
    pg.draw.rect(screen, black, [200,0,400,550])
    pg.draw.line(screen, yellow, [350,0], [350,50], 5)
    pg.draw.line(screen, yellow, [350,125], [350,200], 5)
    pg.draw.line(screen, yellow, [350,275], [350,350], 5)
    pg.draw.line(screen, yellow, [350,425], [350,500], 5)
    pg.draw.rect(screen, darkgreen, [0,0,200,550])
    pg.draw.rect(screen, darkgreen, [500,0,250,550])
    
    #Displays the instructions on the top of the screen and stays there for the duration of the game
    pg.font.init()
    font = pg.font.SysFont('Calibri', 23)
    font1 = pg.font.SysFont('Calibri', 23)
    fontsurface = font.render('Make it to the finish line without getting close to a car!', False, white)
    fontsurface1 = font1.render('Use the arrow keys to move, press the space key to reset your position', False, white)
    screen.blit(fontsurface, (10,0))
    screen.blit(fontsurface1, (10,40))

    fullspritelist.draw(screen) #Draws all of the sprites on the screen
    pg.display.update() #Updates drawing of sprites

pg.quit()
