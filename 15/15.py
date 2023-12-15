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
	boxes = {}

	for i in range(0,256):
		boxes[i] = {}

	for step in steps:
		commands = re.split('', step)
		commands = commands[1:len(commands)-1]
		current_value = 0
		left = ''
		# current value is box to check.
		for value in commands:
			if value.isalpha():
				left = left+value
				current_value = hash(value, current_value)
			elif value in ('=', '-'):
				rule = value
			elif value.isnumeric():
				lens = value

		# print('after', step)
		if rule == '=':

			# add lens to box number current_value
			current_box = boxes[current_value]
			# print(current_box)

			# if already a lens with same label, replace value in situ.
			try:
				boxes[current_value][left] = lens

			# else add to end of box.
			except:
				boxes[current_value][left] = lens
		else:
			# try to remove lens if present & bunch every other lens forward
			try:
				boxes[current_value].pop(left)
			except:
				pass
		# print(boxes)

	# calculate power
	total_focusing_power = 0

	for box_number in boxes:
		print(box_number, boxes[box_number])

		lens_slot_within_box = 1
		for lens in boxes[box_number]:
			lens_value = boxes[box_number][lens]

			focusing_power = (1 + int(box_number)) * lens_slot_within_box * int(lens_value)
			print('lens at', lens, 'has power', focusing_power)
			total_focusing_power += focusing_power

			lens_slot_within_box += 1

	return total_focusing_power


print(f'Part 1: {part1()}, Part 2: {part2()}')


#I had this problem as well — turns out I assumed all label strings were of length 2, which isn't the case in the actual input.