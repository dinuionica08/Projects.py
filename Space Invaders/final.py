import pygame
import random

#Defining Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)

level = 1

#---Defining the Space Invaders
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super(Block, self).__init__()
        self.image = pygame.image.load("enemies.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()


    def update(self):
        #This makes the 'invaders' advance every so often.
        #The exact time should be 20 times 2^(-level), so that
        #the wait time can never be negative and so that it decreases
        #with each level up.
        waittime = (1000.00 * (20.00*(2.00**(-1.00 * level))))//1
        if level == 0:
            self.rect.y = self.rect.y
        else:
            pygame.time.wait(waittime)
            self.rect.y = self.rect.y - 40



#---Defining the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("ship.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = (pos[0] - 50)
        self.rect.y = 650

#---Defining the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.image = pygame.Surface([4, 15])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 12

#function used later to increment the level by one
def Levelup():
    level+=1

#function used later to regenerate the invaders without running through
#the entire while loop
def BlockGenerator():
    for i in range(25):
        block = Block()
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(500)
        block_list.add(block)
        all_sprites_list.add(block)

#--Initializing the game
pygame.init()

pygame.mouse.set_visible(1)

#Setting the width and height of the screen [width, height]
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Spaceship")

all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

for i in range(25):
    block = Block()
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(500)
    block_list.add(block)
    all_sprites_list.add(block)

player = Player()
all_sprites_list.add(player)

#Loop until user clicks the close button
done = False

#Score
score = 0

#formatting, to make the entire spaceship visible
player.rect.y = 370

#Manages how fast the screen updates
clock = pygame.time.Clock()

#-----Main Program Loop------
while not done:
    #---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #---Processing other user actions

        #This handles the "Game Over" instance    
        elif event.type == pygame.MOUSEBUTTONDOWN and level == 0:
            done = True

        #This handles all other instances
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x + 47
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    all_sprites_list.update()

    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1


        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


    #---Drawing the screen

    #Screen clear & fill        
    screen.fill(WHITE)

    #drawing the sprites
    all_sprites_list.draw(screen)

    #Outputting the score and level onto the game
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render("Score: %s" % (score), True, BLUE)
    screen.blit(text, [312, 30])
    text3 = font.render("Level %s" % (level), True, BLUE)
    screen.blit(text3, [450, 30])

    #Once the player kills all 25 invaders, this is executed
    if score == 25:
        font1 = pygame.font.SysFont('Calibri', 40, True, False)
        text2 = font1.render("You Win!", True, GREEN)
        screen.blit(text2, [285, 150])

        #The "You Win!" message shows for roughly 5 seconds,
        #then the player advances to the next level.
        pygame.time.wait(5000)
        Levelup()

    #"Game Over" instance
    #Once a block advances to the same y coordinate as the player,
    #The game ends
    for block in block_list:
        if block.rect.y > 600:
            level = 0
            font2 = pygame.font.SysFont('Calibri', 40, True, False)
            text4 = font.render["You Lose!", 40, True, RED]
            screen.blit(text4, [285, 150])
            #After this, the game loop runs through again, but this time
            #Level is set to 0, making the invaders stationary
            #The "You Lose" message should show
            #Once the player clicks, the game terminates


    pygame.display.flip()

    clock.tick(40)

pygame.quit()