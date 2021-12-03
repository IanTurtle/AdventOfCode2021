import numpy as np

with open('input') as f:
    readings = np.array([list(reading.strip()) for reading in f.readlines()], np.int32)

flipped = readings.transpose()
gamma = ''.join( [ str(np.argmax(np.bincount(row)))
                   for row in flipped] )
				 
epsilon = ''.join( [ '1' if i == '0' else '0' 
                     for i in gamma ] )
				 					 
print(int(gamma, 2) * int(epsilon, 2))