import pygame



def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    color_array = []
    '''
    CREATE ALL COLORS
    for i in xrange(0,256):
        for j in xrange(0,256):
            for k in xrange(0,256):
                color_array.append((i,j,k))
    color_pointer = 0
    print len(color_array)
    '''


    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Color Show')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background

        '''
        PRINT ALL COLORS, ONE EACH TIME THROUGH THE LOOP
        screen.fill(color_array[color_pointer])
        '''

        # Game display

        pygame.display.update()
        clock.tick(1)
        color_pointer += 1

    pygame.quit()

main()
