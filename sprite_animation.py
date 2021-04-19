import pygame

# from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

# the following code is adapted from https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
# basic setup
SIZE = WIDTH, HEIGHT = 600, 400 
BACKGROUND_COLOR = pygame.Color('grey')
FPS = 10 # might need to make this higher

# create a sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        # load each frame
        img_list = ["D1", "D2", "D3", "D4", "L1", "L2", "L3", "L4", "R1", "R2", "R3", "R4", "U1", "U2", "U3", "U4"]
        self.images = []
        for item in img_list:
            self.images.append(pygame.image.load('sprite_sheet2/' + item + '.png'))

        self.index = 0
        self.image = self.images[self.index]
        # 100*100 is the position
        # 66*66 is the size of each frame
        self.rect = pygame.Rect(100, 100, 66, 66)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

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

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()