"""
Advent of Code day 1
Anemily Machina
"""

def load_input(filename):
	with open(filename) as f:
		return f.readlines()

def process_input(raw_input):
	elf_pockets = []
	elf_pocket = []

	for line in raw_input:	
		line = line.strip()
		if line == '':
			elf_pockets.append(elf_pocket)
			elf_pocket = []			
		else:
			elf_pocket.append(int(line))

	if len(elf_pocket) > 0:
		elf_pockets.append(elf_pocket) #make sure to get last one if needed

	return elf_pockets



#Main
def main():
	#part 1
	full_input = load_input("input.txt")

	elf_pockets = process_input(full_input)
	elf_pockets_sum = [sum(elf_pocket) for elf_pocket in elf_pockets]

	#part 1 solution
	print(max(elf_pockets_sum)) 

if __name__ == "__main__":
    main()
