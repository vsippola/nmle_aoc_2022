"""
Advent of Code day 1
Anemily Machina
"""

def load_input(filename):
	with open(filename) as f:
		return f.readlines()

def process_input(full_input):

	ruck_sacs = []
	

	for line in full_input:	
		
		line = line.strip()

		ruck_sac = []

		for letter in line:
			ruck_sac.append(letter)

		ruck_sacs.append(ruck_sac)

	return ruck_sacs
		

def create_priority_dict():

	all_items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

	priority_dict = {item:(item_index + 1) for item_index, item in enumerate(all_items)}
	
	return priority_dict


def find_common_per_sac(ruck_sacs):
	
	common_per_sac = []

	for ruck_sac in ruck_sacs:

		#split sac into compartments
		half_sac_size = len(ruck_sac)//2
		sac1 = ruck_sac[:half_sac_size]
		sac2 = ruck_sac[half_sac_size:]

		#turn sacs into sets
		sac1 = set(sac1)
		sac2 = set(sac2)

		#find intersections
		common = sac1.intersection(sac2)
		
		common_per_sac.append(list(common))

	return common_per_sac

#Main
def main():
	full_input = load_input("input.txt")
	ruck_sacs = process_input(full_input)	


	#part 1
	priority_dict = create_priority_dict()

	#find common items in each pair of compartments per sac
	common_per_sac = find_common_per_sac(ruck_sacs)

	#get and sum priorites of common itmes of compartments per sac
	priority_sum = sum([priority_dict[item] for sac_common in common_per_sac for item in sac_common])
	print(priority_sum)



	
	


	

if __name__ == "__main__":
    main()
