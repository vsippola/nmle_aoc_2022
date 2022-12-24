"""
Advent of Code day 1
Anemily Machina
"""

def load_input(filename):
	with open(filename) as f:
		return f.readlines()

def input2dict(full_input):

	tree_height_dict = {}

	forest_max_x = 0
	forest_max_y = 0
	

	for row_x, line in enumerate(full_input):
		line = line.strip()
		forest_max_y = len(line)
		forest_max_x += 1

		for col_y, height in enumerate(line):
			
			tree_height_dict[(row_x,col_y)] = int(height)

	return tree_height_dict, forest_max_x, forest_max_y


def get_next_tree(current_tree, forest_max_x, forest_max_y, line_type, line_direction):

	next_tree_x = -1
	next_tree_y = -1


	if line_type == 'col':
		next_tree_y = current_tree[1]

		if line_direction == 'forwards':
			next_tree_x = current_tree[0] + 1
		elif line_direction == 'backwards':
			next_tree_x = current_tree[0] -1

	elif line_type == 'row':
		next_tree_x = current_tree[0]

		if line_direction == 'forwards':
			next_tree_y = current_tree[1] + 1
		elif line_direction == 'backwards':
			next_tree_y = current_tree[1] -1

	#make sure we are in bounds
	if next_tree_x not in range(forest_max_x):
		return None

	if next_tree_y not in range(forest_max_y):
		return None

	return (next_tree_x,next_tree_y)



def mark_visible_trees_line(tree_height_dict, visible_trees, forest_max_x, forest_max_y, start_row_x, start_col_y, line_type, line_direction):
	
	max_height = -1
	current_tree = (start_row_x, start_col_y)

	while (current_tree is not None):

		current_tree_height = tree_height_dict[current_tree]
	
		if 	current_tree_height > max_height:
			max_height = current_tree_height
			visible_trees[current_tree] = None

		current_tree = get_next_tree(current_tree, forest_max_x, forest_max_y, line_type, line_direction)




def mark_visible_trees(tree_height_dict, forest_max_x, forest_max_y):

	visible_trees = {}

	for row_x in range(forest_max_x):

		mark_visible_trees_line(tree_height_dict, visible_trees, forest_max_x, forest_max_y, row_x, 0, 'row', 'forwards')
		mark_visible_trees_line(tree_height_dict, visible_trees, forest_max_x, forest_max_y, row_x, forest_max_y - 1, 'row', 'backwards')

	for col_y in range(forest_max_y):

		mark_visible_trees_line(tree_height_dict, visible_trees, forest_max_x, forest_max_y, 0, col_y, 'col', 'forwards')
		mark_visible_trees_line(tree_height_dict, visible_trees, forest_max_x, forest_max_y, forest_max_x - 1, col_y, 'col', 'backwards')

	return visible_trees


def calc_viewing_distance(tree_height_dict, forest_max_x, forest_max_y, start_row_x, start_col_y, view_type, view_direction):

	current_tree = (start_row_x, start_col_y)

	start_tree_height = tree_height_dict[current_tree]

	viewing_distance = 0

	current_tree = get_next_tree(current_tree, forest_max_x, forest_max_y, view_type, view_direction)

	while (current_tree is not None):

		current_tree_height = tree_height_dict[current_tree]

		#new tree is same or taller
		if current_tree_height >= start_tree_height:
			viewing_distance += 1
			return viewing_distance

		#new tree is smaller
		else:
			viewing_distance += 1

		current_tree = get_next_tree(current_tree, forest_max_x, forest_max_y, view_type, view_direction)

	#hit the edge of forest
	return viewing_distance




def calc_scenic_score(tree_height_dict, forest_max_x, forest_max_y, tree_row_x, tree_col_y):

	scenic_score = 1

	for view_type in ['row','col']:
		for view_direction in ['forwards', 'backwards']:

			viewing_distance = calc_viewing_distance(tree_height_dict, forest_max_x, forest_max_y, tree_row_x, tree_col_y, view_type, view_direction)

			scenic_score *= viewing_distance

	return scenic_score


def calc_max_scenic_score(tree_height_dict, forest_max_x, forest_max_y):

	max_scenic_score = -1

	#ignore boundry as they get a 0 and it makes logic easier later unlike part 1
	for row_x in range(1, forest_max_x-1):
		for col_y in range(1,forest_max_y-1):
			scenic_score = calc_scenic_score(tree_height_dict, forest_max_x, forest_max_y, row_x, col_y)

			if scenic_score > max_scenic_score:
				max_scenic_score = scenic_score

	return max_scenic_score 




#Main
def main():
	full_input = load_input("input.txt")
	tree_height_dict, forest_max_x, forest_max_y = input2dict(full_input)
	

	#part 1
	visible_trees = mark_visible_trees(tree_height_dict, forest_max_x, forest_max_y)

	print(len(visible_trees))

	#part 2 
	max_scenic_score = calc_max_scenic_score(tree_height_dict, forest_max_x, forest_max_y)
	print(max_scenic_score)


	

	

if __name__ == "__main__":
    main()

