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

class gamesprite(pg.sprite.Sprite):

    def __init__(self, color, x, y):
        super().__init__() #Calling parent class
        self.image = pg.Surface([x, y])
        pg.draw.rect(self.image, color, [0, 0, x, y])
        self.rect = self.image.get_rect()

#Creating 4 different sprites that, when collided with, will call the function of that specific game
game1 = gamesprite(red, 100, 60)
game1.rect.x = 100
game1.rect.y = 200
game1list = pg.sprite.Group()
game1list.add(game1)
fullspritelist.add(game1)

game2 = gamesprite(red, 100, 60)
game2.rect.x = 200
game2.rect.y = 400
game2list = pg.sprite.Group()
game2list.add(game2)
fullspritelist.add(game2)

game3 = gamesprite(red, 100, 60)
game3.rect.x = 400
game3.rect.y = 300
game3list = pg.sprite.Group()
game3list.add(game3)
fullspritelist.add(game3)

game4 = gamesprite(red, 100, 60)
game4.rect.x = 600
game4.rect.y = 100
game4list = pg.sprite.Group()
game4list.add(game4)
fullspritelist.add(game4)

running = True
while running:
    for gamesprite in pg.sprite.spritecollide(mysprite,game1list,False):
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

        finishline = car(red, 10, 550)
        finishline.rect.x = 650
        finishline.rect.y = 0
        fullspritelist.add(finishline)

        #Making a list with all of the moving cars, list will be used to identify collision between sprite and any of the cars
        carlist = pg.sprite.Group()
        carlist.add(redcar)
        carlist.add(bluecar)
        carlist.add(greencar)
        carlist.add(yellowcar)

        #Only way to make collision loop work was to make a list, so made a list with only the finish line in it
        finishlinelist = pg.sprite.Group()
        finishlinelist.add(finishline)

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
                time.sleep(3) #Sleeps the program for 3 seconds so you can reset and read the text
                mysprite.rect.x = 0
                mysprite.rect.y = 250
                fullspritelist.add(mysprite)

            #Using spritecollide to detect a collision between the finish line and mysprite which would indicate that the player won
            crossfinishline = pg.sprite.spritecollide(mysprite,finishlinelist,False)
            for car in crossfinishline:
                pg.font.init()
                font = pg.font.SysFont('Calibri', 30) #Sets font
                fontsurface = font.render('Congrats! You made it out alive!', False, white) #Displays "try again" text
                screen.blit(fontsurface, (150,250)) #Positioning text
                pg.display.update()
                time.sleep(3) #Sleeps the program for 3 seconds so you can reset and read the text
                running = False #Exits the program once you won

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

    for gamesprite in pg.sprite.spritecollide(mysprite,game2list,False):
        import pygame
        import time
        import random

        pygame.init()

        ## sets the size of the game/initializes display
        dis_width = 600
        dis_height = 600
        
        display = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake - Amit Kundra')

        ## initializing the colors that will be used in the game
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        
        ## sets framerate for how game is going to run
        clock = pygame.time.Clock()
        ## sets values for speed that will be used later 
        snake_block = 10
        snake_speed = 15
        ## defines fonts and sizes to be called upon later (need different sizes in order to fit on screen)
        font_type = pygame.font.SysFont("franklingothicmedium", 23)

        ## draws the snake - checks how long the snake is and draws a rectangle for each point to make the snake longer
        ## this was the hardest thing to figure out - I ended up creating a different function to refer back to
        ## later in the code that iterates along a list that is created in the game loop
        ## and draws a rectangle of the same size in all the places that the snake has been
        def my_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(display, black, [x[0], x[1], 10, 10])
        
        ## the main game loop - where the meat of the game logic lives
        def game_loop():
            game_end = False
            game_close = False
            ##setting some basic parameters that will make the code easier to write 
            x1 = dis_width / 2
            y1 = dis_height / 2
        
            x1_change = 0
            y1_change = 0
        
            snake_List = []
            Length_of_snake = 1
            ##randomizes where the food will appear by randomixing x and y coordinates in the range of the screen
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            ## main while loop for when the game is running
            while not game_end:
        
                while game_close == True:
                    display.fill(white)
                    mesg = font_type.render("Game over. Press 'P' to Play Again or 'Q' to Quit the game", True, red)
                    display.blit(mesg, [dis_width / 5, dis_height / 2])

                    value = font_type.render("Score: " + str(Length_of_snake - 1), True, red)
                    display.blit(value, [0, 0])
                    pygame.display.update()
        
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_end = True
                                game_close = False
                            if event.key == pygame.K_p:
                                game_loop()
                        ## basically, this part of the code says that if q is pressed, the game should be quit
                        ## and if c is pressed, the game loop should be run again. It also calls on the message function previously defined
                        ## in order to actually display that text
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_end = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_end = True
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0
                    ## this part of the code takes the input from the keyboard arrow keys
                    ## and moves the snake one "snake unit" to the direction that was specified 

                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                    ## fixed a bug where the snake could go off the screen - now if the location
                    ## of the snake is ooutside of the bounds it will run the game close sequence
                x1 += x1_change
                y1 += y1_change
                ## updates the values so the snake actually moves continuously to a new location
                display.fill(white)
                pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
                ##draws rectangles for the "food"
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                ## creates a list that stores the location of where the snake has been
                ## so that it can be used to print the snake
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]
                ## deletes rectangles for where the snake has been thats longer than the length of
                ## the snake so it doesn't expand infinitely
                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True
        
                my_snake(snake_block, snake_List)
                ## calls on previously defined functions to draw snake
                ## displays the score using a string and "blit" command
                value = font_type.render("Score: " + str(Length_of_snake - 1), True, red)
                display.blit(value, [0, 0])
        
                pygame.display.update()
                ##simple collision detection - if the location of the snake head is the same as the
                ## location of the food, a new food is made the the length of the snake goes up 
                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1
        
                clock.tick(snake_speed)
        
            pygame.quit()
            quit()
        
        
        game_loop()
    
    #for gamesprite in pg.sprite.spritecollide(mysprite,game3list,False):
        #ADD CODE FOR GAME3

    #for gamesprite in pg.sprite.spritecollide(mysprite,game4list,False):
        #ADD CODE FOR GAME4
    

    keypress = pg.key.get_pressed()        
    if keypress[K_LEFT]:
        mysprite.rect.x -= 3
    if keypress[K_RIGHT]:
        mysprite.rect.x += 3
    if keypress[K_UP]:
        mysprite.rect.y -= 3
    if keypress[K_DOWN]:
        mysprite.rect.y += 3
    
    #Allows the user to quit the pygame window by exiting out or pressing the escape key
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pg.draw.rect(screen, black, [0,0,750,550])
    
    #Displays the instructions on the top of the screen and stays there for the duration of the game
    pg.font.init()
    font = pg.font.SysFont('Calibri', 23)
    font1 = pg.font.SysFont('Calibri', 23)
    fontsurface = font.render('Welcome to the CLPS0950 Arcade!', False, white)
    fontsurface1 = font1.render('Use the arrow keys to move your sprite and pick a game', False, white)
    screen.blit(fontsurface, (10,0))
    screen.blit(fontsurface1, (10,40))

    pg.font.init()
    font2 = pg.font.SysFont('Calibri', 23)
    fontsurface2 = font.render('Crossing Road', False, white)
    screen.blit(fontsurface2, (80,175))

    pg.font.init()
    font3 = pg.font.SysFont('Calibri', 23)
    fontsurface3 = font.render('Snake', False, white)
    screen.blit(fontsurface3, (210,375))

    fullspritelist.draw(screen) #Draws all of the sprites on the screen
    pg.display.update() #Updates drawing of sprites

pg.quit
