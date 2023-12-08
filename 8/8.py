import init
import re

data = init.read_data(isTest=False, )

instructions = re.split('', data[0])
instructions = instructions[1:len(instructions) - 1]

print(instructions)

# create dict of each node and connections
nodes = {}
for line in data[2:]:
	info = re.findall('[A-Za-z]+', line)
	nodes[info[0]] = (info[1], info[2])


def part1():
	steps = 0
	current_location = 'AAA'
	while current_location != 'ZZZ':
		for step in instructions:
			steps += 1
			instruction = nodes[current_location]
			if step == 'L':
				# move to the first instruction position
				current_location = instruction[0]
			else:
				# move to the second instruction position
				current_location = instruction[1]
			print('now at', current_location, 'after', steps, 'steps')
	return steps


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')