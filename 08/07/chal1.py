import numpy as np


def main():

	with open('input', 'r') as f:
		positions = np.array([int(timer.strip()) for timer in f.read().split(",")])
	
	lower = min(positions)
	upper = max(positions)+1
	
	least_fuel = 1000000000
	
	for i in range(lower,upper):
		iteration_fuel = abs(positions-i).sum()
		if iteration_fuel < least_fuel:
			least_fuel = iteration_fuel
		else:
			break

	print(least_fuel)
	
main()

