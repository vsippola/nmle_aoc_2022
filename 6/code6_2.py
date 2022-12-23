"""
Advent of Code day 1
Anemily Machina
"""

def load_input(filename):
	with open(filename) as f:
		return f.readlines()


def find_marker_end_position(buffered_message, marker_size):

	for i in range(len(buffered_message)-(marker_size-1)):
		
		four_letter_code = buffered_message[i:i+marker_size]
		if len(list(set(four_letter_code))) == marker_size:
			return i+marker_size

def find_marker_end_positions(buffered_messages, marker_size):

	marker_end_positions = []

	for buffered_message in buffered_messages:
		marker_end_positions.append(find_marker_end_position(buffered_message, marker_size))

	return marker_end_positions


#Main
def main():
	full_input = load_input("input.txt")
	buffered_messages = [input_line.strip() for input_line in full_input]

	#part 1
	marker_end_positions = find_marker_end_positions(buffered_messages, 4)
	print(marker_end_positions)

	#part 2
	marker_end_positions = find_marker_end_positions(buffered_messages, 14)
	print(marker_end_positions)



	

if __name__ == "__main__":
    main()

