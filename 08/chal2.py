import numpy as np
from collections import Counter
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

def get_patterns_by_length(patterns):
	patterns_by_length = {"2": [], "3": [], "4": [], "5": [], "6": [], "7": []}
	for pattern in patterns:
		patterns_by_length[str(len(pattern))].append(pattern)
	return patterns_by_length

def calculate_number(row):

	number_mappings = {
		"abcefg": "0",
		"cf": "1",
		"acdeg": "2",
		"acdfg": "3",
		"bcdf": "4",
		"abdfg": "5",
		"abdefg": "6",
		"acf": "7",
		"abcdefg": "8",
		"abcdfg": "9"
	}


	# map jumbled letter to actual letter
	letter_mappings = {}

	patterns = row[0].split()
	digits = row[1].split()
	
	patterns_by_length = get_patterns_by_length(patterns)	
	
	# There is only one word of length 3 and one word of length 2, so find the missing letter and map it to "a"
	missing_letter = list(set(patterns_by_length["3"][0]) - set(patterns_by_length["2"][0]))[0]
	letter_mappings[missing_letter] = "a"
	
	# We now know what the letter a maps to, so remove that letter from all words
	patterns = [letter.replace(missing_letter, '') for letter in patterns]
	
	# Do a character count analysis on the 4 letter words
	patterns_by_length = get_patterns_by_length(patterns)	
	letter_counts = Counter("".join(patterns_by_length["4"]))
	for mapped_letter, count in letter_counts.most_common():
		if count == 4:
			letter_mappings[mapped_letter] = "d"
			patterns = [letter.replace(mapped_letter, '') for letter in patterns]
		elif count == 2:
			letter_mappings[mapped_letter] = "b"
			patterns = [letter.replace(mapped_letter, '') for letter in patterns]
		elif count == 1:
			letter_mappings[mapped_letter] = "e"
			patterns = [letter.replace(mapped_letter, '') for letter in patterns]
	
	# Do a character count analysis on the 2 letter words
	patterns_by_length = get_patterns_by_length(patterns)
	letter_counts = Counter("".join(patterns_by_length["2"]))
	for mapped_letter, count in letter_counts.most_common():
		if count == 4:
			letter_mappings[mapped_letter] = "c"
		elif count == 5:
			letter_mappings[mapped_letter] = "f"
		elif count == 3:
			letter_mappings[mapped_letter] = "g"
		

	new_digits = []
	for digit in digits:
		letters = list(digit)
		new_letters = []
		for letter in letters:
			new_letters.append(letter_mappings[letter])
		new_digits.append(number_mappings["".join(sorted(new_letters))])
	number = int("".join(new_digits))
	return number
	
def main():
	
	
	with open('input', 'r') as f:
		lines = f.readlines()
		rows = np.array([x.strip().split(" | ")for x in lines])
	
	# Get initial patterns
	total = 0
	for row in rows:
		total += calculate_number(row)
	print(total)
		
main()

