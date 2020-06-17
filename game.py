from pieces import Dice,Blue,Green
from board import movingBoard

class Game:
	def __init__(self,Id):
		self.diceWent = False
		self.isBlue = False
		self.pieceWent = False
		self.inMovementPiece = 0
		self.BlueWinCount = 0
		self.GreenWinCount = 0
		self.gameId = Id
		self.playersRd = [0,1] 
		self.Bpiece1 = Blue(200,500,1)
		self.Bpiece2 = Blue(50,500,2)
		self.Bpiece3 = Blue(200,650,3)
		self.Bpiece4 = Blue(50,650,4)
		self.Gpiece1 = Green(520,70,1)
		self.Gpiece2 = Green(520,220,2)
		self.Gpiece3 = Green(670,70,3)
		self.Gpiece4 = Green(670,220,4)
		self.ready = False
		self.dice = Dice()
		self.movingBoard = movingBoard
		print(movingBoard[1][8])

	def update(self,game):
		self.diceWent = game.diceWent
		self.isBlue = game.isBlue
		self.pieceWent = game.pieceWent
		self.BlueWinCount = game.BlueWinCount
		self.GreenWinCount = game.GreenWinCount
		self.inMovementPiece = game.inMovementPiece
		self.playersRd = game.playersRd
		self.dice = game.dice
		self.Bpiece1 = game.Bpiece1
		self.Bpiece2 = game.Bpiece2
		self.Bpiece3 = game.Bpiece3
		self.Bpiece4 = game.Bpiece4
		self.Gpiece1 = game.Gpiece1
		self.Gpiece2 = game.Gpiece2
		self.Gpiece3 = game.Gpiece3
		self.Gpiece4 = game.Gpiece4
		self.movingBoard = game.movingBoard