import numpy as np

def update_timer(timer, reset = 6):
	if timer == 0:
		return reset
	return timer-1


def main():

	with open('input', 'r') as f:
		timers = np.array([int(timer.strip()) for timer in f.read().split(",")])

	print(timers)
	for i in range(0, 80):
		zero_count = len(timers) - np.count_nonzero(timers)
		timers = np.array([ update_timer(timer) for timer in timers ])
		timers = np.append(timers, (np.ones((zero_count),  dtype=np.int32)*8))
	
	print(len(timers))
	
main()

