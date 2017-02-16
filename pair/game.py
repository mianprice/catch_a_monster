import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

def overlap(c1, c2):
    if c2.x in xrange(c1.x,c1.x + c1.dimensions[2]) or c2.y in xrange(c1.y, c1.y + c1.dimensions[3]):
        return True



class Hero(object):
    def __init__(self,image,screen):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.x = self.bounds[2]/2 - self.dimensions[2]/2
        self.y = self.bounds[3]/2 - self.dimensions[3]/2
        self.x_speed = 0
        self.y_speed = 0

    def get_location(self):
        return (self.x,self.y)

    def set_speed(self, direction, speed):
        if direction == "x":
            self.x_speed = speed
        else:
            self.y_speed = speed

    def move(self):
        if self.x + self.dimensions[2] <= self.bounds[2] and self.y + self.dimensions[3] <= self.bounds[3] and self.x >= self.bounds[0] and self.y >= self.bounds[1]:
                self.x += self.x_speed
                self.y += self.y_speed
        elif self.x + self.dimensions[2] > self.bounds[2]:
            print "out of bound"
            print str(self.x) + "," + str(self.y)
            self.x = self.bounds[2] - self.dimensions[2]
        elif self.y + self.dimensions[3] > self.bounds[3]:
            print "out of bound"
            print str(self.x) + "," + str(self.y)
            self.y = self.bounds[3] - self.dimensions[3]
        elif self.x < self.bounds[0]:
            print "out of bound"
            print str(self.x) + "," + str(self.y)
            self.x = self.bounds[0]
        elif self.y < self.bounds[1]:
            print "out of bound"
            print str(self.x) + "," + str(self.y)
            self.y = self.bounds[1]

class Monster(object):
    def __init__(self,image,screen):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.x = random.randint(self.bounds[2] - self.dimensions[2])
        self.y = random.randint(self.bounds[3] - self.dimensions[3])
        self.x_speed = 1
        self.y_speed = 0






def main():
   # declare the size of the canvas
   background_image = pygame.image.load('../images/background.png')
   x,y,width,height = background_image.get_rect()
   blue_color = (97, 159, 182)

   pygame.init()
   screen = pygame.display.set_mode((width, height))
   pygame.display.set_caption('Simple Example')
   clock = pygame.time.Clock()

   print screen.get_rect()

   # Game initialization
   hero_image = pygame.image.load('../images/hero.png').convert_alpha()
   hero = Hero(hero_image,screen)

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
                   hero.set_speed("y",-5)
               elif event.key == KEY_UP:
                   hero.set_speed("y",5)
               elif event.key == KEY_LEFT:
                   hero.set_speed("x",-5)
               elif event.key == KEY_RIGHT:
                   hero.set_speed("x",5)
           if event.type == pygame.KEYUP:
               # deactivate the cooresponding speeds
               # when an arrow key is released
               if event.key == KEY_DOWN:
                   hero.set_speed("y",0)
               elif event.key == KEY_UP:
                   hero.set_speed("y",0)
               elif event.key == KEY_LEFT:
                   hero.set_speed("x",0)
               elif event.key == KEY_RIGHT:
                   hero.set_speed("x",0)



       hero.move()

       # Game logic

       # Draw background
       screen.blit(background_image, (0,0))

       # Game display

       screen.blit(hero.image, hero.get_location())

       pygame.display.update()



   pygame.quit()

if __name__ == '__main__':
   main()
