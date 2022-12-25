"""
Advent of Code day 1
Anemily Machina
"""

NOOP, ADDX = 0,1
NOOP_TIME, ADDX_TIME = 1,2
INITIAL_X_VALUE = 1
INITIAL_CYCLE_VALUE = 1
SIGNAL_STRENGTH_KEYS = [20,60,100,140,180,220]

def load_input(filename):
	with open(filename) as f:
		return f.readlines()
	
def parse_instructions(full_input):

	instructions = []

	for line in full_input:
		line = line.strip().split()

		instrction_type = NOOP if line[0] == 'noop' else ADDX
		instruction_data = 0 if instrction_type == NOOP else int(line[1])
		instruction_time = NOOP_TIME if instrction_type == NOOP else ADDX_TIME

		instruction = [instrction_type, instruction_data, instruction_time]

		instructions.append(instruction)

	return instructions

def do_part1_instructions(instructions):

	x = INITIAL_X_VALUE
	cycle = INITIAL_CYCLE_VALUE

	x_values = {}

	instructions = [instruction for instruction in instructions] #make copy

	instruction_queue = [] #trying to guess part 2

	while (len(instructions) > 0) or (len(instruction_queue) > 0):

		x_values[cycle] = x

		#if we aren't doing an instruction add the next one
		if len(instruction_queue) == 0:
			next_instruction = instructions[0]
			instructions = instructions[1:]

			instruction_queue.append(next_instruction)

		#do a cycle (ie lower cycle count)
		instruction_queue[0][2] -=1

		#if the instruction is done
		if instruction_queue[0][2] == 0:

			#do the operation if needed			
			if instruction_queue[0][0] == ADDX:
				x += instruction_queue[0][1]

			#remove the instruction from the queue
			instruction_queue = instruction_queue[1:]

		cycle += 1

	x_values[cycle] = x

	return x_values


def calc_signal_strength_sum(x_values):

	signal_strength_sum = 0

	for signal_strength_key in  SIGNAL_STRENGTH_KEYS:

		x_value = x_values[signal_strength_key]
		signal_strength = x_value*signal_strength_key

		signal_strength_sum +=signal_strength

	return signal_strength_sum



#Main
def main():
	full_input = load_input("input.txt")
	instructions = parse_instructions(full_input)

	#part 1
	x_values = do_part1_instructions(instructions)
	
	signal_strength_sum = calc_signal_strength_sum(x_values)
	print(signal_strength_sum)

if __name__ == "__main__":
    main()

