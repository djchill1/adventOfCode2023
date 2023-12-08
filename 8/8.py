import init
import re
import math

isTest = False
data = init.read_data(isTest, )

instructions = re.split('', data[0])
instructions = instructions[1:len(instructions) - 1]

print(instructions)

# create dict of each node and connections
nodes = {}
for line in data[2:]:
	info = re.findall('[A-Za-z\d]+', line)
	nodes[info[0]] = (info[1], info[2])


def action_all_instructions(start_location):
	current_location = start_location
	for step in instructions:
		instruction = nodes[current_location]
		if step == 'L':
			# move to the first instruction position
			current_location = instruction[0]
		else:
			# move to the second instruction position
			current_location = instruction[1]
		# print(start_location, 'is now at', current_location)
	return current_location

def part1():
	steps = 0
	# current_location = 'AAA'
	# while current_location != 'ZZZ':
	# 	current_location = action_all_instructions(current_location)
	# 	steps += len(instructions)
	# 	print('now at', current_location, 'after', steps, 'steps')
	return steps


def part2():
	steps = 0
	if not isTest:
		current_locations = ['QVA', 'AAA', 'KLA', 'NDA', 'LBA', 'NNA']
	else:
		current_locations = ['11A', '22A']

	firstZat = []

	# find the first time each location gets to something ending in Z
	for current_location in current_locations:
		steps = 0
		while current_location[2] != 'Z':
			current_location = action_all_instructions(current_location)
			steps += len(instructions)
		firstZat.append(steps)

	print(firstZat)

	# find the LCM of these numbers.
	lcm = 1
	for n in firstZat:
		lcm = math.lcm(lcm, n)

	return lcm


print(f'Part 1: {part1()}, Part 2: {part2()}')