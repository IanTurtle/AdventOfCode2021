import numpy as np

class Board:
    	
	def __init__(self, numbers):
		self.numbers = np.array(numbers)
		self.numbers_transpose = np.transpose(self.numbers)
		self.called = np.zeros_like(self.numbers)
		self.called_transpose = np.transpose(self.called)
	
	def call(self, number):
		self.called += (self.numbers == number)
		
	def is_winning(self):
		for row in self.called:
			if np.all(row):
				return True
		for col in self.called_transpose:
			if np.all(col):
				return True
		return False
	
	def get_sum_not_called(self):
		return np.sum(np.multiply(self.numbers, (1 - self.called)))
	
def main():
	with open('input', 'r') as f:
		lines = f.readlines()
	f.close()
	
	# Get calls
	calls = [ int(call) 
	          for call in lines[0].strip().split(",") ]
	
	boards = []
	
	matrix = []
	for line in lines[2:]:
		stripped = line.strip()
		if not stripped:
			boards.append(Board(matrix))
			matrix = []
		else:
			matrix.append([int(number) 
						  for number in line.strip().split()])
	
	for call in calls:
		for board in boards:
			board.call(call)
			if board.is_winning():
				print(call * board.get_sum_not_called())
				exit()
main()

