#import the pygame library
import pygame
pygame.init()

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#windows

width = 500
height = 700
size = ((height, width))
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")
background = pygame.image.load('back.jpg')
screen.blit(background, (0, 0))

#show score

def show_score():
	score = font.render("Score: " )
	screen.blit(score)


#define space 

class Ship:
	def __init__(self, x, y, health = 100):
		self.x = width / 2
		self.y = height / 2
		self.health = health

	def move_left(self):
		self.x -= 10

	def move_right(self):
		self.x += 10

	def draw(self, screen):
		pygame.draw.rect(screen, WHITE, pygame.Rect(self.x, self.y, 60, 60))

class Enemies: 
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def draw(self, screen):
		pygame.draw.rect(screen, RED, pygame.Rect(self.x, self.y, 20, 20))
#main loop

Running = True
clock = pygame.time.Clock()

while Running:
	#main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Running = False

	# logic of the game
	ship = Ship(300, 300)
	enemies1 = Enemies(203,200)
	enemies2 = Enemies(242,220)
	enemies3 = Enemies(254,230)
	enemies4 = Enemies(222,240)
	enemies5 = Enemies(254,230)
	enemies6 = Enemies(222,240)
	keys_pressed = pygame.key.get_pressed()
	if keys_pressed[pygame.K_a]:#left
		ship.move_left()

	if keys_pressed[pygame.K_d]:#right
		ship.move_right()

	#drawing the elements

	ship.draw(screen)
	enemies1.draw(screen)
	enemies2.draw(screen)
	enemies3.draw(screen)
	enemies4.draw(screen)
	enemies5.draw(screen)
	enemies6.draw(screen)
	show_score()
  #update the screen
	pygame.display.flip()

	#70 frames per second
	clock.tick(70)

pygame.quit()
