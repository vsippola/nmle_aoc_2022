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


#turn sacs into sets and find common elements (we now know part 1/2 both have 1 unique element)
def find_common_per_sac(sac_groups):
	
	common_per_sac = []

	for sacs in sac_groups:

		for sac_index, sac in enumerate(sacs):

			sac = set(sac)

			if sac_index == 0:
				sac_intersection = sac

			else:
				sac_intersection = sac_intersection.intersection(sac)
		
		common_per_sac.append(list(sac_intersection)[0])

	return common_per_sac


#Main
def main():
	full_input = load_input("input.txt")
	ruck_sacs = process_input(full_input)	

	#part 1
	priority_dict = create_priority_dict()

	#find common items in each pair of compartments per sac
	compartments_as_sac_groups = [[ ruck_sac[:len(ruck_sac)//2],  ruck_sac[len(ruck_sac)//2:]] for ruck_sac in ruck_sacs]
	common_per_sac_group = find_common_per_sac(compartments_as_sac_groups)

	#get and sum priorites of common itmes of compartments per sac
	priority_sum = sum([priority_dict[common] for common in common_per_sac_group])
	print(priority_sum)

	#part 2
	badge_groups = [ [ruck_sacs[3*i], ruck_sacs[3*i+1], ruck_sacs[3*i+2]] for i in range(len(ruck_sacs)//3) ]

	common_per_sac_group = find_common_per_sac(badge_groups)

	#get and sum priorites of common itmes per group
	priority_sum = sum([priority_dict[common] for common in common_per_sac_group])
	print(priority_sum)




	
	


	

if __name__ == "__main__":
    main()
