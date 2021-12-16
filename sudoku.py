import sys
sys.setrecursionlimit(387420489)
finalcount = 1
Condition = True
VerticalNums = []
SquareNums = []	
Con = True

class SudokuLine:
	def __init__(self, name, square, LineCount):
		self.name = name
		self.RuleBreak = True
		self.Row = []
		self.square = square

		self.Combinations = []#this represents all possible combinations for a row
		self.CurrentCombination = []#this represents the current combination to test.
		self.BaseRow = []#Use this as a blueprint to represent each original line
		
		self.Con = False
		
		self.Highest = 0
		self.CombinationCount = 0 #tracks the combinations in the self.combinations based on an integer value
		self.LineCount = LineCount

	def LineInput(self):
		FinalBoard[self.LineCount] = self.Combinations[self.CombinationCount]
		self.CombinationCount += 1
	def RowNums(self):#finds all the missing numbers in each line
		self.SetBaseRow()
		nums = [1,2,3,4,5,6,7,8,9]
		for num in self.Row:
			for num2 in nums:
				if num == num2:
					nums.remove(num)
		self.Recursive(nums, len(nums), [], len(nums))
	
	def SetBaseRow(self):
		copy = self.Row.copy()
		for i in range(0,len(copy)):
			self.BaseRow.append(copy[i])
	
	def Recursive(self, unused_nums, length, number, constant):#finds all possible combinations
		for num in unused_nums:
			number.append(num)
			NewNumList = unused_nums.copy()
			NewNumList.remove(num)
			if length > 0:
				self.Recursive(NewNumList, length - 1, number, constant)
			if len(number) == constant:
				NewNumber = number.copy()
				BaseRow = self.BaseRow.copy()
				
				x = 0
				for i in range(0, len(BaseRow)):
					if BaseRow[i] == 0:
							BaseRow[i] = NewNumber[x]
							
							x += 1
				
				self.Combinations.append(BaseRow)
			number.remove(num)
	
	def SquareCombination(self, count):
		x = 0
		for i in range(0,9):
			self.AllSquares[x].append(self.Combinations[count][i])  
			if i % 3 == 0:
				x += 1

	def RowNumInput(self):#inputs one combination list into a row.
		count = 0
		for i in range(0, len(self.Row)):
			if self.Row[i] == 0:
				self.Row[i] = self.CurrentCombination[count]
				count += 1
			else:
				pass

def SetRowNums():
	for i in range(0,9):
		AllLines[i].RowNums()

def Vertical():
	for i in range(0,9):
		tempList = []
		for x in range(0,9):
			if AllLines2[x][i] != 0:
				tempList.append(AllLines2[x][i])
		VerticalNums.append(tempList)

def CombinationRemoveVertical():
	for VertCount in range(0,9):
		VertNums = set(VerticalNums[VertCount])
		for LineCount in range(0,9):
			RemoveList = []
			Poggers = []
			Line = AllLines[LineCount].Combinations
			for Combination in Line:
				Number = set([Combination[VertCount]])
				if AllLines[LineCount].BaseRow[VertCount] == 0:
					intersection = VertNums.intersection(Number)

					if len(intersection) > 0:
						RemoveList.append(Combination)
						
					else:
						pass
			for Num1 in RemoveList:
				Line.remove(Num1)
	

def Square():
	for a in range(0,3):
		for b in range(0,3):
			y1 = 3 * a
			x1 = 3 * b
			List1 = []
			for y in range(0,3):
				for x in range(0,3):
					List1.append(AllLines2[y + y1][x + x1])
			SquareNums.append(List1)

	for Square in SquareNums:
		for i in range(8,-1,-1):
			if Square[i] == 0:
				Square.remove(Square[i])
			
def Square2():
	a = -1
	for i in range(0,9):
		if i % 3 == 0:
			a += 1
		Line = AllLines[i]
		BaseRow = AllLines[i].BaseRow
		Squares = [SquareNums[3 * a], SquareNums[3 * a + 1], SquareNums[3 * a + 2]]
		for j in range(len(Line.Combinations) - 1, -1, -1):
			Combination = Line.Combinations[j].copy()
			for num in BaseRow:
				for i in range(0,9):	
					if Combination[i] == num:
						Combination[i] = 0
			for x in range(0,3):
				LineHor = [Combination[3 * x], Combination[3 * x + 1], Combination[3 * x + 2]]
				intersect2 = set(Squares[x]).intersection(set(LineHor))
				if len(intersect2) > 0:

					Line.Combinations.remove(Line.Combinations[j])
					break

def LineSwap(LineCount):
	Line = AllLines[LineCount]
	Line.LineInput()
	if Line.CombinationCount > Line.Highest:
		Line.CombinationCount = 0
		LineSwap(LineCount - 1)


def BoardTest():
	count = 0
	nums = {1,2,3,4,5,6,7,8,9}
	for x in range(0,9):
		hor = []
		for y in range(0,9):
			hor.append(FinalBoard[y][x])
		if len(hor) != 9:
			pass
		else:
			intersect = set(hor).intersection(nums)
			if len(intersect) < 9:
				count += 1
	Squares = []
	for a in range(0,3):
		for b in range(0,3):
			y1 = 3 * a
			x1 = 3 * b
			List1 = []
			for y in range(0,3):
				for x in range(0,3):
					List1.append(FinalBoard[y + y1][x + x1])
			Squares.append(List1)
	for square in Squares:
		intersect = set(square).intersection(nums)
		if len(intersect) < 9:
			count += 1
	if count > 0:
		pass
	else:
		for i in range(0,9):
			print(FinalBoard[i])
		global finalcount
		finalcount = -1

FinalBoard = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
]

Line1 = SudokuLine("1", 1, 0)
Line2 = SudokuLine("2", 1, 1)
Line3 = SudokuLine("3", 1, 2)
Line4 = SudokuLine("4", 2, 3)
Line5 = SudokuLine("5", 2, 4)
Line6 = SudokuLine("6", 2, 5)
Line7 = SudokuLine("7", 3, 6)
Line8 = SudokuLine("8", 3, 7)
Line9 = SudokuLine("9", 3, 8)

AllLines = [Line1, Line2, Line3, Line4, Line5, Line6, Line7, Line8, Line9]
AllLines2 = [Line1.BaseRow, Line2.BaseRow, Line3.BaseRow, Line4.BaseRow, Line5.BaseRow, Line6.BaseRow, Line7.BaseRow, Line8.BaseRow, Line9.BaseRow]
for line in AllLines:
	i = input("Line" + str(line.name))
	line.Row = i

SetRowNums()
Vertical()
CombinationRemoveVertical()
Square()
Square2()

for i in range(0,9):
	AllLines[i].Highest = len(AllLines[i].Combinations) - 1

while finalcount > 0:
	LineSwap(8)
	BoardTest()

