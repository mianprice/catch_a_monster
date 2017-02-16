import pygame

width = 500
height = 500

class Circle(object):
    def __init__(self,screen,radius,position,color,direction):
        self.screen = screen
        self.radius = radius
        self.position = position
        self.color = color
        self.direction = direction

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

    def updateDirection(self):
        for i,v in enumerate(self.direction):
            if self.position[i] + self.radius > width or self.position[i] + self.radius > height or self.position[i] - self.radius < 0:
                v = -v

    def updatePosition(self):
        for i,v in enumerate(self.position):
            v += self.direction[i]



def main():
    blue_color = (97, 159, 182)
    white_color = (0,0,0)

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

    # Game initialization
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Warmup')
    clock = pygame.time.Clock()

    # Create circle to move
    circle = Circle(screen,25,(250,250),blue_color,(5,5))


    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        circle.updatePosition()
        circle.updateDirection()

        # Draw background
        screen.fill(white_color)
        circle.draw()
        '''
        PRINT ALL COLORS, ONE EACH TIME THROUGH THE LOOP
        screen.fill(color_array[color_pointer])
        color_pointer += 1
        '''

        # Game display

        pygame.display.update()
        clock.tick(1)



    pygame.quit()

main()
