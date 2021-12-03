import numpy as np

with open('input') as f:
    init_readings = np.array([list(reading.strip()) for reading in f.readlines()], np.int32)

def oxy_generator(readings, index):
    flipped = readings.transpose()
    row = flipped[index]
    counts = np.bincount(row)
    if counts[0] != counts[1]:
        row_max = np.argmax(counts)
    else:
        row_max = 1
    new_readings = np.array([ reading for reading in readings if reading[index] == row_max ])
    return new_readings

def co2_generator(readings, index):
    flipped = readings.transpose()
    row = flipped[index]
    counts = np.bincount(row)
    if counts[0] != counts[1]:
        row_max = np.argmin(counts)
    else:
        row_max = 0
    new_readings = np.array([ reading for reading in readings if reading[index] == row_max ])
    return new_readings

def calculate_rating(readings, generator):
    index = 0
    ratings = readings
    while(len(ratings) > 1):
        ratings = generator(ratings, index)
        index += 1
    rating = ''.join([str(bit) for bit in ratings.flatten()])
    return rating
	
oxygen_rating = calculate_rating(init_readings, oxy_generator)
co2_rating = calculate_rating(init_readings, co2_generator)

print(int(oxygen_rating, 2) * int(co2_rating, 2))
	
