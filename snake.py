import pygame
import time
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

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
