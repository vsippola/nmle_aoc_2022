"""
Advent of Code day 1
Anemily Machina
"""

def load_input(filename):
	with open(filename) as f:
		return f.readlines()

def split_input(full_input):

	stack_input = []
	move_input = []

	reading_stack_input = True

	for line in full_input:
		line = line[:-1]
		
		if line == "":
			reading_stack_input = False
		elif reading_stack_input:
			stack_input.append(line)
		else:
			move_input.append(line)

	return stack_input, move_input


def process_stack_input(stack_input):

	stack_dict = {}

	stack_numbers = stack_input.pop().split()
	for stack_number in stack_numbers:
		stack_dict[int(stack_number)] = []

	while len(stack_input) > 0:
		stack_contents = stack_input.pop()

		for stack_number in stack_dict:
			
			item_index = 1+4*(stack_number-1)			
			item = stack_contents[item_index]

			if item != " ":
				stack_dict[stack_number].append(item)

	return stack_dict

def process_move_input(move_input):
	
	moves = []

	for move in move_input:
		move = move.strip().split()
		moves.append( ( int(move[1]), int(move[3]), int(move[5]) ) )

	return moves
	
def do_moves(stack_dict, moves, serial_no = 9000):
	
	#moves = number of mover, from stack, to stack
	for move in moves:

		num_crates = move[0]
		s1 =move[1]
		s2 = move[2]

		#pick up the crates
		moving = stack_dict[s1][-num_crates:]
		stack_dict[s1] = stack_dict[s1][:-num_crates]

		#flip them if one at a time
		if serial_no == 9000:
			moving.reverse()

		stack_dict[s2].extend(moving)
		

def get_word(stack_dict):

	word = ""
	for key in stack_dict:
		word += stack_dict[key][-1]

	return word


#Main
def main():
	full_input = load_input("input.txt")
	stack_input, move_input = split_input(full_input)
	stack_dict = process_stack_input(stack_input)
	moves = process_move_input(move_input)

	#part1

	#inplace this is why we need copy
	stack_dict_copy = {key:[item for item in stack_dict[key]] for key in stack_dict}
	do_moves(stack_dict_copy, moves)
	word = get_word(stack_dict_copy)
	print(word)

	#part2
	stack_dict_copy = {key:[item for item in stack_dict[key]] for key in stack_dict}
	do_moves(stack_dict_copy, moves, 9001)
	word = get_word(stack_dict_copy)
	print(word)

	

	

if __name__ == "__main__":
    main()
