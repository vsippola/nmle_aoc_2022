"""
Advent of Code day 1
Anemily Machina
"""

def load_input(filename):
	with open(filename) as f:
		return f.readlines()

def process_input(full_input):

	opponent_moves = []
	my_moves = []

	for line in full_input:	
		line = line.strip()
		split_line = line.split()
		opponent_moves.append(split_line[0].strip()) 
		my_moves.append(split_line[1].strip()) 

	return opponent_moves, my_moves		

#makes a table showing if your move is right and their move is left
def calculate_move2result():
	choices = ['rock', 'paper', 'scissors']
	result = ['draw','lose','win']

	move2result = {}
	for choice1_index in range(len(choices)):
		for choice2_offset in range(0,3):

			choice1 = choices[choice1_index]
			choice2 = choices[(choice1_index+choice2_offset)%len(choices)]

			move2result[f'{choice1}_{choice2}'] = result[choice2_offset]

	return move2result
		



def run_tournament(opponent_moves, my_moves, opponent_move_dict, my_move_dict, move_score, result_score, move2result):
	
	score = 0
	
	for opponent_move, my_move in zip(opponent_moves, my_moves):
		
		#get RPS moves
		opponent_move = opponent_move_dict[opponent_move]
		my_move = my_move_dict[my_move]

		#get match result
		result = move2result[f'{my_move}_{opponent_move}']

		#update score
		score += move_score[my_move]
		score += result_score[result]

	return score





#Main
def main():
	move2result = calculate_move2result()

	#part 1
	full_input = load_input("input.txt")
	opponent_moves, my_moves = process_input(full_input)

	opponent_move_dict = {'A':'rock', 'B':'paper', 'C':'scissors'}
	my_move_dict = {'X':'rock', 'Y':'paper', 'Z':'scissors'}

	move_score = {'rock':1, 'paper':2, 'scissors':3}
	result_score = {'lose':0, 'draw':3, 'win':6}

	score = run_tournament(opponent_moves, my_moves, opponent_move_dict, my_move_dict, move_score, result_score, move2result)

	print(score)


	

if __name__ == "__main__":
    main()
