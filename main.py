import pygame
from board import findPath,board,pathCol,pathRow,arrows,pixels
from pieces import Dice,Blue,Green
from game import Game
from network import Network

import time
import random

pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)

dices = [pygame.image.load('./Sprites/d1.png'),pygame.image.load('./Sprites/d2.png'),pygame.image.load('./Sprites/d3.png'),pygame.image.load('./Sprites/d4.png'),pygame.image.load('./Sprites/d5.png'),pygame.image.load('./Sprites/d6.png')]	

n = Network()
game = n.send({},"GET")

def giveSurface(count):
	return myfont.render(str(count), False, (0, 0, 0))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((772,772))

bg = pygame.image.load('./Sprites/bg.jpg')	

def drawRect(screen,color):
	if color == "Blue":
		pygame.draw.rect(screen, (0, 0, 255), (2, 465, 300, 300), 6)
	else:
		pygame.draw.rect(screen, (0, 255, 0), (464, 10, 300, 300), 6)

def drawScreen(game):
	Bluepieces = [game.Bpiece1,game.Bpiece2,game.Bpiece3,game.Bpiece4]
	Greenpieces = [game.Gpiece1,game.Gpiece2,game.Gpiece3,game.Gpiece4]
	global dices
	screen.blit(bg,(0,0))	
	game.dice.draw(dices,screen) 
	if game.isBlue:
		drawRect(screen,"Blue")
	else:
		drawRect(screen,"Green")	

	screen.blit(giveSurface(game.BlueWinCount),(148,589))
	screen.blit(giveSurface(game.GreenWinCount),(609,129))

	for bluep in Bluepieces:
		if not bluep.dontInclude:
			bluep.draw(screen)

	for greenp in Greenpieces:
		if not greenp.dontInclude:
			greenp.draw(screen)		

	pygame.display.update()


run = True
i = 0
modified = False

def isBlueingame():
	if game.Bpiece1.inGame or game.Bpiece2.inGame or game.Bpiece3.inGame or game.Bpiece4.inGame:
		return True
	else:
		return False


def isGreeningame():
	if game.Gpiece1.inGame or game.Gpiece2.inGame or game.Gpiece3.inGame or game.Gpiece4.inGame:
		return True
	else:
		return False			

def isDicePressed(event):
	if not game.diceWent:
		pos = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN and 352 < pos[0] < 352+68 and 352 < pos[1] < 352+68:
			game.dice.idx = random.randint(0,5)
			print("diceeeeee......",game.dice.idx)
			game.diceWent = True

def piecePressed(pos):
	posx,posy = pos
	if game.isBlue:
		if game.Bpiece1.x < posx < game.Bpiece1.x + 38 and game.Bpiece1.y < posy < game.Bpiece1.y + 38 and (game.dice.idx == 5 or game.Bpiece1.inGame):
			return game.Bpiece1
		elif game.Bpiece2.x < posx < game.Bpiece2.x + 38 and game.Bpiece2.y < posy < game.Bpiece2.y + 38 and (game.dice.idx == 5 or game.Bpiece2.inGame): 	
			return game.Bpiece2
		elif game.Bpiece3.x < posx < game.Bpiece3.x + 38 and game.Bpiece3.y < posy < game.Bpiece3.y + 38 and (game.dice.idx == 5 or game.Bpiece3.inGame):	
			return game.Bpiece3
		elif game.Bpiece4.x < posx < game.Bpiece4.x + 38 and game.Bpiece4.y < posy < game.Bpiece4.y + 38 and (game.dice.idx == 5 or game.Bpiece4.inGame):
			return game.Bpiece4
		else:
			return -1	
	elif not game.isBlue:
		if game.Gpiece1.x < posx < game.Gpiece1.x + 38 and game.Gpiece1.y < posy < game.Gpiece1.y + 38 and (game.dice.idx == 5 or game.Gpiece1.inGame):
			return game.Gpiece1
		elif game.Gpiece2.x < posx < game.Gpiece2.x + 38 and game.Gpiece2.y < posy < game.Gpiece2.y + 38 and (game.dice.idx == 5 or game.Gpiece2.inGame): 	
			return game.Gpiece2
		elif game.Gpiece3.x < posx < game.Gpiece3.x + 38 and game.Gpiece3.y < posy < game.Gpiece3.y + 38 and (game.dice.idx == 5 or game.Gpiece3.inGame):	
			return game.Gpiece3
		elif game.Gpiece4.x < posx < game.Gpiece4.x + 38 and game.Gpiece4.y < posy < game.Gpiece4.y + 38 and (game.dice.idx == 5 or game.Gpiece4.inGame):
			return game.Gpiece4
		else:
			return -1
				

def moveDice(event):
	global game
	if game.diceWent and not game.pieceWent:
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			game.inMovementPiece = piecePressed(pos)
			if game.isBlue:
				if isBlueingame() or game.dice.idx == 5:
					if game.inMovementPiece != -1:
						game.pieceWent = True
						#print("above",game.inMovementPiece.color,game.inMovementPiece.xInMat-(dice.idx+1),game.inMovementPiece.xInMat,game.inMovementPiece.yInMat)
						if game.inMovementPiece.color == 'Blue' and game.inMovementPiece.xInMat-(game.dice.idx+1) < 8  and game.inMovementPiece.xInMat >= 7 and game.inMovementPiece.yInMat == 7:
							#print(game.inMovementPiece.color,game.inMovementPiece.xInMat-dice.idx,game.inMovementPiece.xInMat,game.inMovementPiece.yInMat)
							game.pieceWent = False
							game.diceWent = False
							game.playersRd = [not game.playersRd[0],not game.playersRd[1]]	
							game.isBlue = not game.isBlue

				else:
					print("hittingg....")
					game.diceWent = False		
					game.playersRd = [not game.playersRd[0],not game.playersRd[1]]
					game.isBlue = not game.isBlue
		
			else:
				if isGreeningame() or game.dice.idx == 5:
					if game.inMovementPiece != -1:
						game.pieceWent = True
						if game.inMovementPiece.color == 'Green' and game.inMovementPiece.xInMat+(game.dice.idx+1) > 6 and game.inMovementPiece.xInMat <= 7 and game.inMovementPiece.yInMat == 7:
							game.pieceWent = False
							game.diceWent = False	
							game.playersRd = [not game.playersRd[0],not game.playersRd[1]]
							game.isBlue = not game.isBlue
							

				else:
					print(game.isBlue,"hitting")
					game.diceWent = False
					game.playersRd = [not game.playersRd[0],not game.playersRd[1]]
					game.isBlue = not game.isBlue
				


def movePiece():
	global i
	global game
	continu = True
	if type([]) == type(game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat]):
		if len(game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat]) == 1:
			game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat] = -1
		else:	
			j = 0
			length = len(game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat])
			while len(game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat]) != length-1 and j < length:
				if game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat][j] == game.inMovementPiece:
					game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat].pop(i)
				j += 1	
	else:
		if game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat] == -1: 
			game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat] = -1
		else:
			game.movingBoard[game.inMovementPiece.xInMat][game.inMovementPiece.yInMat] = -2	
	print("piece moving.....")
	while continu:
		i += 1		
		x,y = findPath(game.inMovementPiece.xInMat,game.inMovementPiece.yInMat,game.inMovementPiece,game.dice.idx+1)	
		if x == 13 and y == 6 and game.inMovementPiece.color == "Blue":
			i = 6
		if x == 1 and y == 8 and game.inMovementPiece.color == "Green":
			i = 6	
		if x == -1 and y == -1:
			game.diceWent = False
			game.pieceWent = False
			game.playersRd = [not game.playersRd[0],not game.playersRd[1]]
			game.isBlue = not game.isBlue
		game.inMovementPiece.xInMat = x
		game.inMovementPiece.yInMat = y
		game.inMovementPiece.x = pixels[x][y][0]
		game.inMovementPiece.y = pixels[x][y][1]
		if i == game.dice.idx+1:
			print(game.movingBoard[x][y],x,y)
			if game.movingBoard[x][y] != -1 and game.movingBoard[x][y] != -2:
				print("Came here....")
				same = False
				if type([]) == type(game.movingBoard[x][y]):
					print(game.movingBoard[x][y])
					for idx,i in enumerate(game.movingBoard[x][y]):
						print(idx,i)
						if i.color != game.inMovementPiece.color:
							print("game.pieceWentgg.....")
							i.xInMat = i.initX[0]
							i.yInMat = i.initY[0]
							i.x = i.initX[1]
							i.y = i.initY[1]
							i.inGame = False
						else:
							same = True	
						if idx == len(game.movingBoard[x][y]) - 1:
							game.movingBoard[x][y] = [game.inMovementPiece] 				
				if same:
					print("same")
					game.movingBoard[x][y].append(game.inMovementPiece)
			elif game.movingBoard[x][y] == -1:
				game.movingBoard[x][y] = [game.inMovementPiece]	
				print("puting stufff....")					
						
			if game.inMovementPiece.xInMat == 8 and game.inMovementPiece.yInMat == 7 and game.inMovementPiece.color == "Blue":
				game.BlueWinCount += 1
				game.inMovementPiece.dontInclude = True
				game.inMovementPiece.inGame = False
			if game.inMovementPiece.xInMat == 6 and game.inMovementPiece.yInMat == 7 and game.inMovementPiece.color == "Green":
				game.GreenWinCount += 1	
				game.inMovementPiece.dontInclude = True
				game.inMovementPiece.inGame = False
			game.pieceWent = False
			game.diceWent = False
			game.playersRd = [not game.playersRd[0],not game.playersRd[1]]
			game.isBlue = not game.isBlue
			# print(game.inMovementPiece.color,game.inMovementPiece.nth,game.inMovementPiece.xInMat,game.inMovementPiece.yInMat)
			# print(game.Gpiece1.xInMat,game.Gpiece1.yInMat)
			game = n.send(game,"POST")
			continu = False
			i = 0

while run:
	clock.tick(20)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			n.send({},"CLOSE")
	# print(game.ready)
	# print(game.playersRd,game.playersRd[int(n.p)])			


	if game.ready and game.playersRd[int(n.p)]:		
		isDicePressed(event)	
		moveDice(event)

		if game.BlueWinCount == 4 or game.GreenWinCount == 4:
			run = False

		
		if game.pieceWent:
			movePiece()	
		game = n.send(game,"POST")
	else:	
		
		game = n.send({},"SEND_ME")	
	drawScreen(game)

			