import numpy as np

def calculate_fuel(n):
	return np.arange(0,n+1).sum()


def main():

	with open('input', 'r') as f:
		positions = np.array([int(timer.strip()) for timer in f.read().split(",")])
	
	lower = min(positions)
	upper = max(positions)+1
	
	least_fuel = 1000000000
	
	for i in range(lower,upper):
		num_moves = abs(positions-i)
		iteration_fuel = np.array(list(map(calculate_fuel, num_moves))).sum()
		if iteration_fuel < least_fuel:
			least_fuel = iteration_fuel
		else:
			break

	print(least_fuel)
	
main()

