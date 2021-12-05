import numpy as np

class Board:
        
    def __init__(self, numbers):
        self.iteration = 0
        self.numbers = np.array(numbers)
        self.shape = self.numbers.shape
        self.called = np.zeros_like(self.numbers)
    
    def call(self, number):
        self.called += (self.numbers == number)
        self.most_recent_call = number
        self.iteration += 1
        
    def is_winning(self):
        row_sums = np.sum(self.called, 1)
        col_sums = np.sum(self.called, 0)
		
        return self.shape[0] in row_sums or  self.shape[1] in col_sums
    
    def get_sum_not_called(self):
        return np.sum(np.multiply(self.numbers, (1 - self.called)))
    
def main():
    with open('input', 'r') as f:
        lines = f.readlines()
    f.close()
    
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
    for board in boards:
        for call in calls:
            board.call(call)
            if board.is_winning():
                break
                
    boards.sort(key = lambda x: x.iteration, reverse=True)
    last_board = boards[0]

    print(last_board.most_recent_call * last_board.get_sum_not_called())

main()

