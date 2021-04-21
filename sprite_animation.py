import pygame
pygame.init()

# the following code is adapted from https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
# basic setup
SIZE = WIDTH, HEIGHT = 625, 400 
BACKGROUND_COLOR = pygame.Color('grey')
FPS = 10 # might need to make this higher

# create a sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        # load each frame
        # repeat this 4 times for 4 directions
        # change img_list to 4 lists of 4 for the different directions
        # and replace "self" with "down", left", right", or "up"
        #### this doesn't work ####
        img_list = ["D1", "D2", "D3", "D4", "L1", "L2", "L3", "L4", "R1", "R2", "R3", "R4", "U1", "U2", "U3", "U4"]
        self.images = []
        for item in img_list:
            self.images.append(pygame.image.load('sprite_sheet2/' + item + '.png'))

        self.index = 0 # start with the first frame
        self.image = self.images[self.index]
        # 100*100 is the position
        # 66*66 is the size of each frame
        self.rect = pygame.Rect(100, 100, 66, 66)

    def update(self):
        # do the same with this part
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

#Creating class that will be used to create sprites that mysprite can collide with to choose a specific game
class gamesprite(pygame.sprite.Sprite):

    def __init__(self, color, x, y):
        super().__init__() #Calling parent class
        self.image = pygame.Surface([x, y])
        pygame.draw.rect(self.image, color, [0, 0, x, y])
        self.rect = self.image.get_rect()

#Creating 4 different sprites that, when collided with, will call the function of that specific game
game1 = gamesprite(red, 60, 100)
game1.rect.x = 100
game1.rect.y = 200
game1list = pygame.sprite.Group()
game1list.add(game1)

game2 = gamesprite(red, 60, 100)
game2.rect.x = 200
game2.rect.y = 200
game2list = pygame.sprite.Group()
game2list.add(game2)

game3 = gamesprite(red, 60, 100)
game3.rect.x = 300
game3.rect.y = 200
game3list = pygame.sprite.Group()
game3list.add(game3)

game4 = gamesprite(red, 60, 100)
game4.rect.x = 300
game4.rect.y = 200
game4list = pygame.sprite.Group()
game4list.add(game4)

for gamesprite in pygame.sprite.spritecollide(Mysprite,game1list,False):
    #CALL GAME 1 FUNCTION

for gamesprite in pygame.sprite.spritecollide(Mysprite,game2list,False):
    #CALL GAME 2 FUNCTION

for gamesprite in pygame.sprite.spritecollide(Mysprite,game3list,False):
    #CALL GAME 3 FUNCTION

for gamesprite in pygame.sprite.spritecollide(Mysprite,game4list,False):
    #CALL GAME 4 FUNCTION

# main loop
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keypress = pygame.key.get_pressed()        
            if keypress[K_LEFT]:
                self.rect.x -= 2
            if keypress[K_RIGHT]:
                self.rect.x += 2
            if keypress[K_UP]:
                self.rect.y -= 2
            if keypress[K_DOWN]:
                self.rect.y += 2

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
