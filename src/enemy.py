import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
	def __init__(self, name, x, y, img_file):
		'''
	creates our enemies, sets their position and speen and gives them name
	args: self(class), name(self) ,x ,y, img_file
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
		self.name = name + str(id(self))
		self.speed = 2
      

	def update(self):
		'''
	makes the enemies randomly move on the screen
	args: self(class)
	return: None
		'''
		self.rect.x += random.randrange (-1,2)
		self.rect.y += random.randrange (-1,2)
     
