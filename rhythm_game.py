import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 625, 400 
bg = pygame.Color('grey')
FPS = 30 # might need to make this higher
screen = pygame.display.set_mode(SIZE)
note_img = pygame.image.load('img_files/note.png') # size of this image is 75*75
note_speed = 5
font = pygame.font.SysFont('comicsans', 30)


# create userevent add_note, a note will be added every 700 ms
add_note = pygame.USEREVENT + 1
pygame.time.set_timer(add_note, 700)

# create user event for hits
left_hit = pygame.USEREVENT + 2
middle_hit = pygame.USEREVENT + 3
right_hit = pygame.USEREVENT + 4

# there are three columns of notes (left, middle, and right)
# draw notes using screen.blit
def draw_screen(note_L_list, note_M_list, note_R_list, combo, score, line):
    screen.fill(bg) # draw background

    # draw combo and score text
    combo_text = font.render("Combo: " + str(combo), 1, 'black')
    score_text = font.render("Score: " + str(score), 1, 'black')
    screen.blit(combo_text, (10, 10))
    screen.blit(score_text, (10, 40))

    # draw line
    pygame.draw.rect(screen, 'cyan', line)

    for note_L in note_L_list:
        screen.blit(note_img, (note_L.x, note_L.y))
    for note_M in note_M_list:
        screen.blit(note_img, (note_M.x, note_M.y))
    for note_R in note_R_list:
        screen.blit(note_img, (note_R.x, note_R.y))
    pygame.display.update()

# move each note down according to note_speed
# remove note if it moves out of the screen
def make_notes(note_L_list, note_M_list, note_R_list, line):
    for note_L in note_L_list:
        note_L.y += note_speed
        if line.colliderect(note_L): # if the note collide with the line
            pygame.event.post(pygame.event.Event(left_hit))
        if note_L.y > HEIGHT:
            note_L_list.remove(note_L)

    for note_M in note_M_list:
        note_M.y += note_speed
        if line.colliderect(note_M):
            pygame.event.post(pygame.event.Event(middle_hit))
        if note_M.y > HEIGHT:
            note_M_list.remove(note_M)

    for note_R in note_R_list:
        note_R.y += note_speed
        if line.colliderect(note_R):
            pygame.event.post(pygame.event.Event(right_hit))
        if note_R.y > HEIGHT:
            note_R_list.remove(note_R)

# main loop
def main():
    clock = pygame.time.Clock()

    # create lists of notes
    note_L_list = []
    note_M_list = []
    note_R_list = []

    # combo and score
    combo = 0
    score = 0

    # line
    line = pygame.Rect(0,350,625,8)

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

            # get position of the left note when it collide with the line
            if event.type == left_hit:
                left_note = note_L.y 
            # get position of the left note when user hit the left arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_key = note_L.y
                    # allow a range of error (maybe need to change this)
                    if (left_note - 5) < left_key < (left_note + 5):
                        score += 1

            # repeat for middle notes
            if event.type == middle_hit:
                middle_note = note_M.y 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    middle_key = note_M.y
                    if (middle_note - 5) < middle_key < (middle_note + 5):
                        score += 1
            
            # repeat for right notes
            if event.type == right_hit:
                right_note = note_R.y 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right_key = note_R.y
                    if (right_note - 5) < right_key < (right_note + 5):
                        score += 1

        make_notes(note_L_list, note_M_list, note_R_list, line)
        draw_screen(note_L_list, note_M_list, note_R_list, combo, score, line)

if __name__ == '__main__':
    main()

pygame.quit()
