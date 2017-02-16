import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
KEY_ENTER = 13
KEY_Q = 113
play_again = True
level_counter = 1


def overlap(c1, c2):
    if (c2.x in xrange(c1.x,c1.x + c1.dimensions[2]) and c2.y in xrange(c1.y, c1.y + c1.dimensions[3])) or (c2.x + c2.dimensions[2] in xrange(c1.x,c1.x + c1.dimensions[2]) and c2.y + c2.dimensions[3] in xrange(c1.y, c1.y + c1.dimensions[3])):
        return True
    else:
        return False

class Character(object):
    def __init__(self,image,screen):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()

    def get_location(self):
        return (self.x,self.y)

class Enemy(Character):
    def __init__(self,image,screen,others):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others)
        self.direction_speed = 1
        self.change_direction()

    def change_direction(self):
        self.x_speed = random.randint(-1,1)
        self.y_speed = random.randint(-1,1)
        self.x_speed *= self.direction_speed
        self.y_speed *= self.direction_speed

    def set_location(self,others):
        self.x = random.randint(self.bounds[0],self.bounds[2] - self.dimensions[2])
        self.y = random.randint(self.bounds[1],self.bounds[3] - self.dimensions[3])
        resetFlag = False
        for i in others:
            if overlap(i,self):
                resetFlag = True
        if resetFlag:
            self.set_location(others)

    def move(self):
        if self.x <= self.bounds[2] and self.y <= self.bounds[3] and self.x >= self.bounds[0] - self.dimensions[2] and self.y >= self.bounds[1] - self.dimensions[3]:
            self.x += self.x_speed
            self.y += self.y_speed
        elif self.x > self.bounds[2]:
            self.x = self.bounds[0] - self.dimensions[2]
        elif self.y > self.bounds[3]:
            self.y = self.bounds[1] - self.dimensions[3]
        elif self.x < self.bounds[0] - self.dimensions[2]:
            self.x = self.bounds[2]
        elif self.y < self.bounds[3] - self.dimensions[3]:
            self.y = self.bounds[3]

class Goblin(Enemy):
    def __init__(self,image,screen,others):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others)
        self.direction_speed = 1
        self.change_direction()

class Hero(Character):
    def __init__(self,image,screen):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        for i in xrange(len(self.bounds)/2):
            self.bounds[i] += 32
            self.bounds[i+2] -= 32
        #self.bounds = list(self.bounds) + [32, 32, -32, -32]
        self.x = self.bounds[2]/2 - self.dimensions[2]/2
        self.y = self.bounds[3]/2 - self.dimensions[3]/2
        self.x_speed = 0
        self.y_speed = 0

    def set_speed(self, direction, speed):
        if direction == "x":
            self.x_speed = 2 * speed
        else:
            self.y_speed = 2 * speed

    def move(self):
        if self.x + self.dimensions[2] <= self.bounds[2] and self.y + self.dimensions[3] <= self.bounds[3] and self.x >= self.bounds[0] and self.y >= self.bounds[1]:
            self.x += self.x_speed
            self.y += self.y_speed
        elif self.x + self.dimensions[2] > self.bounds[2]:
            self.x = self.bounds[2] - self.dimensions[2]
        elif self.y + self.dimensions[3] > self.bounds[3]:
            self.y = self.bounds[3] - self.dimensions[3]
        elif self.x < self.bounds[0]:
            self.x = self.bounds[0]
        elif self.y < self.bounds[1]:
            self.y = self.bounds[1]

class Monster(Enemy):
    def __init__(self,image,screen,others):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others)
        self.direction_speed = 3
        self.change_direction()




def main():
    global play_again, level_counter
    play_again = False
    # declare the size of the canvas
    background_image = pygame.image.load('../images/background.png')

    x,y,width,height = background_image.get_rect()
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Simple Example')
    clock = pygame.time.Clock()
    tick = clock.tick()
    game_music = pygame.mixer.Sound('../sounds/music.wav')

    characters = []

    # Game initialization
    hero_image = pygame.image.load('../images/hero.png').convert_alpha()
    hero = Hero(hero_image,screen)
    characters.append(hero)

    monster_image = pygame.image.load('../images/monster.png').convert_alpha()
    monster = Monster(monster_image,screen,characters)
    characters.append(monster)

    num_goblins = 3 + level_counter - 1
    goblins = []
    goblin_image = pygame.image.load('../images/goblin.png').convert_alpha()
    for i in xrange(num_goblins):
        goblin = Goblin(goblin_image,screen,characters)
        characters.append(goblin)
        goblins.append(goblin)


    stop_game = False
    quit_game = False
    end_condition = ''
    game_music.play(-1)
    font = pygame.font.Font(None, 30)
    level_text = font.render('Level %d' % level_counter, True, (0, 0, 0), (255,255,255))

    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True
                quit_game = True
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.set_speed("y",1)
                elif event.key == KEY_UP:
                    hero.set_speed("y",-1)
                elif event.key == KEY_LEFT:
                    hero.set_speed("x",-1)
                elif event.key == KEY_RIGHT:
                    hero.set_speed("x",1)

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

        if overlap(hero, monster):
            stop_game = True
            sound = pygame.mixer.Sound('../sounds/win.wav')
            sound.play()
            end_condition = 'win'

        for i in goblins:
            if overlap(hero, i):
                stop_game = True
                sound = pygame.mixer.Sound('../sounds/lose.wav')
                sound.play()
                end_condition = 'lose'

        hero.move()
        monster.move()
        for i in goblins:
            i.move()

        if tick > 2000:
            monster.change_direction()
            for i in goblins:
                i.change_direction()
            tick = 0

        # Draw background
        screen.blit(background_image, (0,0))

        # Game display
        screen.blit(level_text,(32,32))
        screen.blit(hero.image, hero.get_location())
        screen.blit(monster.image, monster.get_location())
        for i in goblins:
            screen.blit(i.image, i.get_location())


        pygame.display.update()

        tick += clock.tick()


    game_music.stop()
    if end_condition == 'win':
        level_counter += 1
    else:
        level_counter = 1

    while not quit_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_ENTER:
                    play_again = True
                    quit_game = True
                if event.key == KEY_Q:
                    quit_game = True


        screen.blit(background_image, (0,0))
        screen.blit(hero.image, hero.get_location())
        font = pygame.font.Font(None, 50)
        text = font.render('press ENTER to play again', True, (0, 0, 0))
        text2 = font.render('press Q to quit ', True, (0, 0, 0))
        if end_condition == 'win':
            text3 = font.render('You win!', True, (0, 0, 0))
        else:
            text3 = font.render('You lose!', True, (0, 0, 0))
        screen.blit(text, (32, height/2))
        screen.blit(text2, (32, height/2 + 75))
        screen.blit(text3, (32, height/2 - 75))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    while play_again:
        main()
