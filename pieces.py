import pygame

pieceBlue = pygame.image.load('./Sprites/chipBlueWhite.png')
pieceGreen = pygame.image.load('./Sprites/green.png')

class Blue:
	def __init__(self,x,y,nth):
		self.initX = [13,x]
		self.initY = [6,y]
		self.x = x
		self.y = y
		self.nth = nth
		self.inGame = False
		self.xInMat = 13
		self.yInMat = 6
		self.color = 'Blue'
		self.dontInclude = False

	def draw(self,window):
		window.blit(pieceBlue,(self.x,self.y))

class Green:
	def __init__(self,x,y,nth):
		self.initX = [1,x]
		self.initY = [8,y]
		self.x = x
		self.y = y
		self.nth = nth
		self.inGame = False
		self.xInMat = 1
		self.yInMat = 8
		self.color = 'Green'
		self.dontInclude = False

	def draw(self,window):
		window.blit(pieceGreen,(self.x,self.y))		

class Dice:
	def __init__(self):
		self.x = 772//2-34
		self.y = 772//2-34	
		self.idx = 2

	def draw(self,surface,screen):
		screen.blit(surface[self.idx],(self.x,self.y))	
