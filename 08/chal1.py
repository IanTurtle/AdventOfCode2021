import numpy as np

"""
0 - abcefg (6)
1 - cf (2)
2 - acdeg (5)
3 - acdfg (5)
4 - bcdf (4)
5 - abdfg (5)
6 - abdefg (6) 
7 - acf (3)
8 - abcdefg (7)
9 - abcdfg (6)
"""

def main():

	sizes = [2, 4, 3, 7]

	with open('input', 'r') as f:
		lines = f.readlines()
		output_values = np.array([x.strip().split(" | ")[1].split() for x in lines]).flatten()
	
	output_sizes = np.array([len(value) for value in output_values])

	print(np.isin(output_sizes, sizes).sum())
	
main()

