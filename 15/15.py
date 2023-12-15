import init
import re

data = init.read_data(isTest=False, )

steps = re.split(',',data[0])

def hash(character, current_value):
	current_value += ord(character)
	current_value = current_value*17
	current_value = current_value % 256
	return current_value



def part1():
	current_values = []
	for step in steps:
		current_value = 0
		for character in step:
			current_value = hash(character, current_value)
		print('step', step, 'results in current value', current_value)
		current_values.append(current_value)
	return sum(current_values)


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')