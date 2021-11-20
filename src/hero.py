import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
	def __init__(self, name, x, y, img_file):
		'''
    	creates the hero and gives it a name, speed and health
    	args: self(class), name(class), x, y, img_file
    	return: None
    		'''
		#initialize all the Sprite functionality
		pygame.sprite.Sprite.__init__(self)
		#The following two attributes must be called image and rect
		#pygame assumes you have intitialized these values
		#and uses them to update the screen

		#create surface object image
		self.image = pygame.image.load(img_file).convert_alpha()
        	#get the rectangle for positioning
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		#set other attributes
		self.name = name
		self.speed = 3
		self.health = 3

		#methods to make moving our hero easier
	def move_up(self):
		'''
	moves the hero up
	args: self(class)
	return: None
		'''
		self.rect.y -= self.speed

	def move_down(self):
		'''
    	moves the hero down
    	args: self(class)
    	return: None
    		'''
		self.rect.y += self.speed

	def move_left(self):
		'''
    	moves the hero left
   	args: self(class)
    	return: None
    		'''
		self.rect.x -= self.speed

	def move_right(self):
		'''
	moves the hero right
	args: self(class)
	return: None
		'''
		self.rect.x += self.speed

	def fight(self, opponent):
		'''
	makes the  hero and enemy fights and reduces the health fof the hero if the attacks fails
	args: self(class), opponent
	return: True(bool) and False(bool)
    		'''
		if(random.randrange(3)):
			self.health -= 1
			print("attack failed. Remaining Health: ", self.health)
			return False
		else:
			print("successful attack")
		return True
