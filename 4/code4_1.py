"""
Advent of Code day 1
Anemily Machina
"""

def load_input(filename):
	with open(filename) as f:
		return f.readlines()

def process_input(full_input):

	pairs_of_ranges = []

	for line in full_input:
		line = line.strip()
		split_line = line.split(",")

		pair_of_ranges = []
		for range_values in split_line:
			pair_of_ranges.append([int(value) for value in range_values.split('-')])

		pairs_of_ranges.append(pair_of_ranges)

	return pairs_of_ranges


#returns true if range 1 is inside range 2, otherwise false
def is_inside(range1, range2):

	if range1[0] < range2[0]:
		return False

	if range1[1] > range2[1]:
		return False

	return True

def count_overlap(pairs_of_ranges):

	number_overlap = 0

	for pair_of_ranges in pairs_of_ranges:		

		if is_inside(pair_of_ranges[0], pair_of_ranges[1]) or is_inside(pair_of_ranges[1], pair_of_ranges[0]):
			number_overlap += 1

	return number_overlap


	
#Main
def main():
	full_input = load_input("input.txt")

	pairs_of_ranges = process_input(full_input)	

	#part 1
	number_overlap = count_overlap(pairs_of_ranges)
	print(number_overlap)






	
	


	

if __name__ == "__main__":
    main()
