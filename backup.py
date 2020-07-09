import pygame
from board import findPath,board,pathCol,pathRow,arrows,pixels,movingBoard
from pieces import Dice,Blue,Green
from actions import Action

import time
import random


actions = Action()
pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)


def giveSurface(count):
	return myfont.render(str(count), False, (0, 0, 0))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((772,772))

bg = pygame.image.load('bg.jpg')

Bpiece1 = Blue(200,500,1)
Bpiece2 = Blue(50,500,2)
Bpiece3 = Blue(200,650,3)
Bpiece4 = Blue(50,650,4)
Gpiece1 = Green(520,70,1)
Gpiece2 = Green(520,220,2)
Gpiece3 = Green(670,70,3)
Gpiece4 = Green(670,220,4)
dice = Dice() 	

Bluepieces = [Bpiece1,Bpiece2,Bpiece3,Bpiece4]
Greenpieces = [Gpiece1,Gpiece2,Gpiece3,Gpiece4]

def drawRect(screen,color):
	if color == "Blue":
		pygame.draw.rect(screen, (0, 0, 255), (2, 465, 300, 300), 6)
	else:
		pygame.draw.rect(screen, (0, 255, 0), (464, 10, 300, 300), 6)

def drawScreen():
	screen.blit(bg,(0,0))	
	dice.draw(screen) 
	if actions.isBlue:
		drawRect(screen,"Blue")
	else:
		drawRect(screen,"Green")	

	screen.blit(giveSurface(actions.BlueWinCount),(148,589))
	screen.blit(giveSurface(actions.GreenWinCount),(609,129))

	for bluep in Bluepieces:
		if not bluep.dontInclude:
			bluep.draw(screen)

	for greenp in Greenpieces:
		if not greenp.dontInclude:
			greenp.draw(screen)		

	pygame.display.update()


run = True

inMovementPiece = 0

def isBlueingame():
	if Bpiece1.inGame or Bpiece2.inGame or Bpiece3.inGame or Bpiece4.inGame:
		return True
	else:
		return False


def isGreeningame():
	if Gpiece1.inGame or Gpiece2.inGame or Gpiece3.inGame or Gpiece4.inGame:
		return True
	else:
		return False			

def isDicePressed(event):
	if not actions.movings:
		pos = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN and 352 < pos[0] < 352+68 and 352 < pos[1] < 352+68:
			if actions.isBlue:
				actions.isBlue = 0
			else:
				actions.isBlue = 1	
			dice.idx = random.randint(0,5)
			actions.movings = True

def piecePressed(pos):
	posx,posy = pos
	if actions.isBlue:
		if Bpiece1.x < posx < Bpiece1.x + 38 and Bpiece1.y < posy < Bpiece1.y + 38 and (dice.idx == 5 or Bpiece1.inGame):
			return Bpiece1
		elif Bpiece2.x < posx < Bpiece2.x + 38 and Bpiece2.y < posy < Bpiece2.y + 38 and (dice.idx == 5 or Bpiece2.inGame): 	
			return Bpiece2
		elif Bpiece3.x < posx < Bpiece3.x + 38 and Bpiece3.y < posy < Bpiece3.y + 38 and (dice.idx == 5 or Bpiece3.inGame):	
			return Bpiece3
		elif Bpiece4.x < posx < Bpiece4.x + 38 and Bpiece4.y < posy < Bpiece4.y + 38 and (dice.idx == 5 or Bpiece4.inGame):
			return Bpiece4
		else:
			return -1	
	else:
		if Gpiece1.x < posx < Gpiece1.x + 38 and Gpiece1.y < posy < Gpiece1.y + 38 and (dice.idx == 5 or Gpiece1.inGame):
			return Gpiece1
		elif Gpiece2.x < posx < Gpiece2.x + 38 and Gpiece2.y < posy < Gpiece2.y + 38 and (dice.idx == 5 or Gpiece2.inGame): 	
			return Gpiece2
		elif Gpiece3.x < posx < Gpiece3.x + 38 and Gpiece3.y < posy < Gpiece3.y + 38 and (dice.idx == 5 or Gpiece3.inGame):	
			return Gpiece3
		elif Gpiece4.x < posx < Gpiece4.x + 38 and Gpiece4.y < posy < Gpiece4.y + 38 and (dice.idx == 5 or Gpiece4.inGame):
			return Gpiece4
		else:
			return -1


while run:
	clock.tick(20)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		isDicePressed(event)	
		inMovementPiece = actions.moves_wrt_dice(event,piecePressed,pygame.mouse.get_pos(),isBlueingame,isGreeningame,inMovementPiece,pygame.MOUSEBUTTONDOWN,dice)

	if actions.BlueWinCount == 4 or actions.GreenWinCount == 4:
		run = False

	
	if actions.moving:
		actions.movePiece(inMovementPiece,dice)

	drawScreen()
			
