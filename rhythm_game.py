def rhythm_game():
    import pygame
    import random
    pygame.init()

    SIZE = WIDTH, HEIGHT = 750, 550 # define screen size

    # reshape start screen, background, and note image
    start_img = pygame.transform.scale(pygame.image.load('img_and_sound/start_screen.png'), (WIDTH, HEIGHT))
    bg_img = pygame.transform.scale(pygame.image.load('img_and_sound/background.png'), (WIDTH, HEIGHT))
    note_img = pygame.transform.scale(pygame.image.load('img_and_sound/note.png'), (90,90))
    line_img = pygame.transform.scale(pygame.image.load('img_and_sound/line.png'), (WIDTH,8))

    FPS = 50 # might need to make this higher
    screen = pygame.display.set_mode(SIZE)
    note_speed = 4
    font = pygame.font.SysFont('comicsans', 40)

    # import sound files
    click_sound = pygame.mixer.Sound('img_and_sound/click.mp3')
    music_sound = pygame.mixer.Sound('img_and_sound/music_100bpm.mp3')

    # create userevent add_note, a note will be added every 600 ms
    add_note = pygame.USEREVENT + 1
    pygame.time.set_timer(add_note, 600)

    # create user event for hits
    left_hit = pygame.USEREVENT + 2
    middle_hit = pygame.USEREVENT + 3
    right_hit = pygame.USEREVENT + 4

    # there are three columns of notes (left, middle, and right)
    # draw notes using screen.blit
    def draw_screen(note_L_list, note_M_list, note_R_list, score, line):
        screen.blit(bg_img, (0, 0)) # draw background
        screen.blit(line_img, (0,475)) # draw line

        # draw score text
        score_text = font.render("Score: " + str(score), 1, 'white')
        screen.blit(score_text, (10, 10))

        for note_L in note_L_list:
            screen.blit(note_img, (note_L.x, note_L.y))
        for note_M in note_M_list:
            screen.blit(note_img, (note_M.x, note_M.y))
        for note_R in note_R_list:
            screen.blit(note_img, (note_R.x, note_R.y))
        pygame.display.update()

    # move each note down the screen according to note_speed
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

    # draw result screen
    def draw_result(score):
        screen.blit(bg_img, (0, 0))
        result_text = font.render("You scored " + str(score) + " out of 50", 1, 'white')
        screen.blit(result_text, (WIDTH/2 - result_text.get_width() /
                            2, HEIGHT/2 - result_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(6000)

    # Draw start screen with how to play info
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(start_img, (0, 0))
        pygame.display.flip()
        pygame.time.delay(6000)
        break

    # start clock
    clock = pygame.time.Clock()
    music_sound.play()

    # create lists of notes
    note_L_list = []
    note_M_list = []
    note_R_list = []

    # Initialization
    score = 0
    note_count = 0
    left_note, middle_note, right_note = 0,0,0
    note_L, note_M, note_R = pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0)

    # draw line as rectangle 
    line = pygame.Rect(0,475,WIDTH,8)

    # main loop
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # the notes are randomly spaced
            # repeat this randomization for left, middle, and right note column
            if event.type == add_note and random.randint(1,3) == 1:
                note_L = pygame.Rect(120,0,75,75)
                note_L_list.append(note_L)
                note_count += 1
            if event.type == add_note and random.randint(1,3) == 1:
                note_M = pygame.Rect(330,0,75,75)
                note_M_list.append(note_M)
                note_count += 1
            if event.type == add_note and random.randint(1,3) == 1:
                note_R = pygame.Rect(540,0,75,75)
                note_R_list.append(note_R)
                note_count += 1

            # get position of the left note when it collide with the line
            if event.type == left_hit:
                left_note = note_L.y 
            # get position of the left note when user hit the left arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    click_sound.play()
                    left_key = note_L.y
                    # allow a range of error (maybe need to change this)
                    if (left_note - 10) < left_key < (left_note + 10):
                        score += 1

            # repeat for middle notes
            if event.type == middle_hit:
                middle_note = note_M.y 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    click_sound.play()
                    middle_key = note_M.y
                    if (middle_note - 5) < middle_key < (middle_note + 5):
                        score += 1
            
            # repeat for right notes
            if event.type == right_hit:
                right_note = note_R.y 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    click_sound.play()
                    right_key = note_R.y
                    if (right_note - 5) < right_key < (right_note + 5):
                        score += 1

        if note_count >= 50:
            draw_result(score) # draw result screen
            break
        
        make_notes(note_L_list, note_M_list, note_R_list, line)
        draw_screen(note_L_list, note_M_list, note_R_list, score, line)

    pygame.quit()