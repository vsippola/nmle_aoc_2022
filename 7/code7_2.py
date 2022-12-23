"""
Advent of Code day 1
Anemily Machina
"""

def load_input(filename):
	with open(filename) as f:
		return f.readlines()

def process_input(full_input):
	
	terminal_output = []

	for line in full_input:
		line = line.strip()
		terminal_output.append(line)
		
	return terminal_output


def change_dir(root, current_dir, terminal_line_tokens):

	target_dir = terminal_line_tokens[2]

	if target_dir == "/":
		return root

	if target_dir == "..":
		return current_dir['parent']

	if target_dir not in current_dir['files']:
		print("Folder not found?")

	return current_dir['files'][target_dir]


def populate_folder_from_ls(current_dir, terminal_output, current_line):

	output_classifications = {'$':'command', 'dir':'directory_name'}
	output_classification_default = 'file_size_and_name'	

	current_classification = ""

	while (current_classification != output_classifications['$']) and (current_line < len(terminal_output) - 1):

		current_line += 1

		terminal_line = terminal_output[current_line]
		terminal_line_tokens = terminal_line.split()

		current_classification = output_classifications.get(terminal_line_tokens[0], output_classification_default)

		#if there is a subfolder
		if current_classification == output_classifications['dir']:

			folder_name = terminal_line_tokens[1]

			current_dir['files'][folder_name] = {'type':'folder', 'files':{}, 'size':0, 'parent':current_dir}

		#else if this is a file
		elif current_classification == output_classification_default:

			file_size = int(terminal_line_tokens[0])
			file_name = terminal_line_tokens[1]

			current_dir['files'][file_name] = {'type':'file', 'size':file_size}

	return current_dir, current_line



def navigate_system(terminal_output):

	root = {'type':'folder', 'files':{}, 'size':0}

	current_dir = root
	current_line = 0

	while current_line < len(terminal_output) - 1:

		terminal_line = terminal_output[current_line]
		terminal_line_tokens = terminal_line.split()

		command_type = terminal_line_tokens[1]

		if command_type == "cd":

			current_dir = change_dir(root, current_dir, terminal_line_tokens)
			current_line += 1

		elif command_type == "ls":

			current_dir, current_line = populate_folder_from_ls(current_dir, terminal_output, current_line)
		

	return root


def print_filesystem_recursive(root, prefix):

	for file_key in  root['files']:

		file = root['files'][file_key]

		file_size = file['size']

		if file['type'] == 'file':

			print( f'{prefix} {file_key} (file, size={ file_size })' )

		else:
			print(f'{prefix} {file_key} (dir, size={ file_size })')
			print_filesystem(file, "  " + prefix)


#got errors, debugging
def print_filesystem(root, prefix):

	file_size = root['size']
	print(f'{prefix} / (dir, size={ file_size })')

	print_filesystem_recursive(root, "  " + prefix)



def calculate_folder_sizes(root):

	total_size = 0

	for file_key in root['files']:

		file = root['files'][file_key]

		#if it is a folder not a file, calculate size recursively
		if file['type'] == 'folder':
			calculate_folder_sizes(file)

		total_size += file['size']

	root['size'] = total_size


def  sum_folder_size(root, cutoff):

	total = 0

	if root['size'] <= cutoff:
		total+= root['size']

	for file_key in root['files']:

		file = root['files'][file_key]

		if file['type'] == 'folder':
			total += sum_folder_size(file, cutoff)


	return total


#only need to know the size of this directory, so discard names
def find_potential_directories_to_delete(root, max_space, current_space, potential_directories_to_delete):

	folder_size = root['size']

	if  (current_space - folder_size) <= max_space:		
		potential_directories_to_delete.append(folder_size)

	#recursion
	for file_key in root['files']:

		file = root['files'][file_key]

		if file['type'] == 'folder':
			find_potential_directories_to_delete(file, max_space, current_space, potential_directories_to_delete)



#Main
def main():
	full_input = load_input("input.txt")
	terminal_output = process_input(full_input)

	#part 1
	file_system_root = navigate_system(terminal_output)

	calculate_folder_sizes(file_system_root)

	cutoff = 100000

	total_sum_folder_size = sum_folder_size(file_system_root, cutoff)
	print(total_sum_folder_size)

	potential_directories_to_delete = []
	needed_space = 30000000
	total_space = 70000000

	find_potential_directories_to_delete(file_system_root, total_space - needed_space, file_system_root['size'], potential_directories_to_delete)

	potential_directories_to_delete.sort()

	print(potential_directories_to_delete[0])
	
	

	

if __name__ == "__main__":
    main()

