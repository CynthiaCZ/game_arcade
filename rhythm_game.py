import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 625, 400 
bg = pygame.Color('grey')
FPS = 30 # might need to make this higher
screen = pygame.display.set_mode(SIZE)
note_img = pygame.image.load('note.png') # size of this image is 75*75
note_speed = 5
# create userevent add_note, a note will be added every 700 ms
add_note = pygame.USEREVENT + 1
pygame.time.set_timer(add_note, 700)

# there are three columns of notes (left, middle, and right)
# draw notes using screen.blit
def draw_screen(note_L_list, note_M_list, note_R_list):
    screen.fill(bg)
    for note_L in note_L_list:
        screen.blit(note_img, (note_L.x, note_L.y))
    for note_M in note_M_list:
        screen.blit(note_img, (note_M.x, note_M.y))
    for note_R in note_R_list:
        screen.blit(note_img, (note_R.x, note_R.y))
    pygame.display.update()

# move each note down according to note_speed
# remove note if it moves out of the screen
def make_notes(note_L_list, note_M_list, note_R_list):
    for note_L in note_L_list:
        note_L.y += note_speed
        if note_L.y > HEIGHT:
            note_L_list.remove(note_L)
    for note_M in note_M_list:
        note_M.y += note_speed
        if note_M.y > HEIGHT:
            note_M_list.remove(note_M)
    for note_R in note_R_list:
        note_R.y += note_speed
        if note_R.y > HEIGHT:
            note_R_list.remove(note_R)

# main loop
def main():
    clock = pygame.time.Clock()
    # create lists of notes
    note_L_list = []
    note_M_list = []
    note_R_list = []

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # the notes are randomly spaced
            # repeat this randomization for left, middle, and right note column
            if event.type == add_note and random.randint(1,3) == 1:
                note_L = pygame.Rect(100,0,75,75)
                note_L_list.append(note_L)
            if event.type == add_note and random.randint(1,3) == 1:
                note_M = pygame.Rect(275,0,75,75)
                note_M_list.append(note_M)
            if event.type == add_note and random.randint(1,3) == 1:
                note_R = pygame.Rect(450,0,75,75)
                note_R_list.append(note_R)

            # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LEFT:
                
        make_notes(note_L_list, note_M_list, note_R_list)
        draw_screen(note_L_list, note_M_list, note_R_list)

if __name__ == '__main__':
    main()

pygame.quit()
