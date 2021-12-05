import numpy as np

class Board:
        
    def __init__(self, numbers):
        self.numbers = np.array(numbers)
        self.shape = self.numbers.shape
        self.called = np.zeros_like(self.numbers)
    
    def call(self, number):
        self.called += (self.numbers == number)
        
    def is_winning(self):
        row_sums = np.sum(self.called, 1)
        col_sums = np.sum(self.called, 0)
		
        return self.shape[0] in row_sums or  self.shape[0] in col_sums
            
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
    board = boards[0]
    for call in calls:
        for board in boards:
            board.call(call)
            if board.is_winning():
                print(call * board.get_sum_not_called())
                exit()
main()

