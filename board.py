pixels = [[[0,0] for x in range(15)] for y in range(15)]

pixels[0][0] = [16,20]

for i in range(1,15):
	pixels[i][0] = [pixels[i-1][0][0],pixels[i-1][0][1] + 50]

for j in range(1,15):
	pixels[0][j] = [pixels[0][j-1][0] + 50,pixels[0][j-1][1]]		

for i in range(1,15):
	for j in range(1,15):
		pixels[i][j] = [pixels[i][j-1][0]+50,pixels[i-1][j][1]+50]


board = [[0 for x in range(15)] for y in range(15)]



board[10-1][7-1] = 300
board[7-1][6-1] = 301
board[6-1][9-1] = 302
board[9-1][10-1] = 303
board[7][0] = 2
board[0][7] = 4
board[7][14] = 6
board[14][7] = 8

pathCol = {6:"decRow",8:"incRow"}
pathRow = {6:"incCol",8:"decCol"}
decideUrselfCol = {7:1}
arrows = {300:[8,5],301:[5,6],302:[6,9],303:[9,8]}
twoWays = {2:[6,0],4:[0,8],6:[8,14],8:[14,6]}

def findPath(x,y,obj,thrown):
	if not obj.inGame and thrown == 6:
		obj.inGame = True		
		return [obj.xInMat,obj.yInMat]
	if obj.inGame:
		if board[x][y] in arrows:
			b = arrows[board[x][y]]
			x = b[0]
			y = b[1]
		elif y in decideUrselfCol or board[x][y] in twoWays:
			if x <= 14 and x >= 8 and obj.color == 'Blue':
				x -= 1
			elif x >= 0 and x <= 6 and obj.color == 'Green':
				x += 1	
			else:	
				print(board[x][y])
				b = twoWays[board[x][y]]
				x = b[0]
				y = b[1]
		elif y in pathCol:
			if pathCol[y] == "decRow":
				if x-1 < 0:
					y += 1
				else:	 
					x -= 1	
			else:
				if x+1 > 14:
					y -= 1
				else:
					x += 1	 		
		elif x in pathRow:
			if pathRow[x] == "decCol":
				if y-1 < 0:
					x = x-1
				else:
					y = y-1
			else:
				if y+1 > 14:
					x = x + 1
				else:
					y += 1
	else:
		return [-1,-1]

	return [x,y]
	

movingBoard = [[-1 for x in range(15)] for y in range(15)]
movingBoard[13][6] = -2
movingBoard[12][8] = -2
movingBoard[8][13] = -2
movingBoard[6][12] = -2
movingBoard[8][2] = -2
movingBoard[6][1] = -2
movingBoard[2][6] = -2
movingBoard[1][8] = -2