import pygame
from rhythm_game import * # import rhythm game
from crossingroad import * #import crossing road
from snake import * #import snake

# sprite animation code is adapted from https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
# sprite movement code is adapted from https://opensource.com/article/17/12/game-python-moving-player

# basic setup
SIZE = WIDTH, HEIGHT = 750, 550 
BACKGROUND_COLOR = pygame.Color(130, 130, 130)
FPS = 10

# Create list of all sprites
fullspritelist = pygame.sprite.Group()

# create a player sprite class
class player_sprite(pygame.sprite.Sprite):
    def __init__(self):
        super(player_sprite, self).__init__()
        self.movex = 0
        self.movey = 0

        # load frames for animation
        # 66*66 is the image size of each frame
        img_list = ["D1", "D2", "D3", "D4"]
        self.images = []
        for item in img_list:
            self.images.append(pygame.image.load('sprite_sheet2/' + item + '.png'))

        self.index = 0 # start with the first frame
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

    # control movement of the sprite
    def control(self, x, y):
        self.movex += x
        self.movey += y

    # update frame index and position
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

# create sprite and add to list
my_sprite = player_sprite()
fullspritelist.add(my_sprite)

class gamesprite(pygame.sprite.Sprite):

    def __init__(self, color, x, y):
        super().__init__() #Calling parent class
        self.image = pygame.Surface([x, y])
        pygame.draw.rect(self.image, color, [0, 0, x, y])
        self.rect = self.image.get_rect()

#Creating 4 different sprites that, when collided with, will call the function of that specific game
game1 = gamesprite((100,149,237), 100, 60)
game1.rect.x = 100
game1.rect.y = 200
game1list = pygame.sprite.Group()
game1list.add(game1)
fullspritelist.add(game1)

game2 = gamesprite((72,61,139), 100, 60)
game2.rect.x = 200
game2.rect.y = 400
game2list = pygame.sprite.Group()
game2list.add(game2)
fullspritelist.add(game2)

game3 = gamesprite((72,209,204), 100, 60)
game3.rect.x = 400
game3.rect.y = 300
game3list = pygame.sprite.Group()
game3list.add(game3)
fullspritelist.add(game3)

game4 = gamesprite((255,127,80), 100, 60)
game4.rect.x = 600
game4.rect.y = 150
game4list = pygame.sprite.Group()
game4list.add(game4)
fullspritelist.add(game4)

# main loop
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    my_sprite.rect.x = 0
    my_sprite.rect.y = 330
    font = pygame.font.SysFont('Calibri', 26)

    while True:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:     
                if event.key == pygame.K_LEFT:
                    my_sprite.control(-10, 0)
                if event.key == pygame.K_RIGHT:
                    my_sprite.control(10, 0)
                if event.key == pygame.K_UP:
                    my_sprite.control(0 ,-10)
                if event.key == pygame.K_DOWN:
                    my_sprite.control(0 ,10)
    
            if event.type == pygame.KEYUP:     
                if event.key == pygame.K_LEFT:
                    my_sprite.control(10, 0)
                if event.key == pygame.K_RIGHT:
                    my_sprite.control(-10, 0)
                if event.key == pygame.K_UP:
                    my_sprite.control(0 ,10)
                if event.key == pygame.K_DOWN:
                    my_sprite.control(0 ,-10)

            # call game functions when player sprite collide with game sprite
            for gamesprite in pygame.sprite.spritecollide(my_sprite,game1list,False):
                crossingroad()
            for gamesprite in pygame.sprite.spritecollide(my_sprite,game2list,False):
                snake()
            for gamesprite in pygame.sprite.spritecollide(my_sprite,game3list,False):
                rhythm_game()
            # for gamesprite in pygame.sprite.spritecollide(my_sprite,game4list,False):
                # call function for tetris

        
        # write text
        text1 = font.render('Welcome to the CLPS0950 Arcade!', False, 'white')
        text2 = font.render('Use the arrow keys to move your sprite and pick a game', False, 'white')
        text3 = font.render('Crossing Road', False, 'white')
        text4 = font.render('Snake', False, 'white')
        text5 = font.render('Rhythm', False, 'white')
        text6 = font.render('Tetris', False, 'white')

        # display text
        screen.blit(text1, (10,0))
        screen.blit(text2, (10,40))
        screen.blit(text3, (80,175))
        screen.blit(text4, (210,375))
        screen.blit(text5, (410,275))
        screen.blit(text6, (610,125))

        fullspritelist.update()
        fullspritelist.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
