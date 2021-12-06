import numpy as np

def main():

	with open('input', 'r') as f:
		timers = np.array([int(timer.strip()) for timer in f.read().split(",")])

	init_counts = np.bincount(timers)
	counts = np.pad(init_counts, (0, 9-len(init_counts)))
	for i in range(0, 256):
		restart_count =  counts[0]
		counts = np.roll(counts, -1)
		counts[6] += restart_count
		
	print(counts.sum())
main()

