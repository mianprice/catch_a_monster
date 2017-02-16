import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

def main():
   # declare the size of the canvas
   background_image = pygame.image.load('../images/background.png')
   x,y,width,height = background_image.get_rect()
   blue_color = (97, 159, 182)

   pygame.init()
   screen = pygame.display.set_mode((width, height))
   pygame.display.set_caption('Simple Example')
   clock = pygame.time.Clock()

   # Game initialization
   hero_image = pygame.image.load('../images/hero.png').convert_alpha()
   hero_size = hero_image.get_rect()

   hero_x = 100
   hero_y = 300
   hero_speed_x = 0
   hero_speed_y = 0

   stop_game = False
   while not stop_game:
       for event in pygame.event.get():
           # Event handling
           if event.type == pygame.QUIT:
               stop_game = True
           if event.type == pygame.KEYDOWN:
               # activate the cooresponding speeds
               # when an arrow key is pressed down
               if event.key == KEY_DOWN:
                   hero_speed_y = 5
               elif event.key == KEY_UP:
                   hero_speed_y = -5
               elif event.key == KEY_LEFT:
                   hero_speed_x = -5
               elif event.key == KEY_RIGHT:
                   hero_speed_x = 5
           if event.type == pygame.KEYUP:
               # deactivate the cooresponding speeds
               # when an arrow key is released
               if event.key == KEY_DOWN:
                   hero_speed_y = 0
               elif event.key == KEY_UP:
                   hero_speed_y = 0
               elif event.key == KEY_LEFT:
                   hero_speed_x = 0
               elif event.key == KEY_RIGHT:
                   hero_speed_x = 0



       if hero_x + 32 < width and hero_y + 32 < height and hero_x > 0 and hero_y > 0:
           hero_x += hero_speed_x
           hero_y += hero_speed_y
       elif hero_x + 32 >= width:
           print "out of bound"
           print str(hero_x) + "," + str(hero_y)
           hero_x = width - 33
       elif hero_y + 32 >= height:
           print "out of bound"
           print str(hero_x) + "," + str(hero_y)
           hero_y = height - 33
       elif hero_x <= 0:
           print "out of bound"
           print str(hero_x) + "," + str(hero_y)
           hero_x = 1
       elif hero_y <= 0:
           print "out of bound"
           print str(hero_x) + "," + str(hero_y)
           hero_y = 1

       # Game logic

       # Draw background
       screen.blit(background_image, (0,0))

       # Game display

       screen.blit(hero_image, (hero_x, hero_y))

       pygame.display.update()



   pygame.quit()

if __name__ == '__main__':
   main()
