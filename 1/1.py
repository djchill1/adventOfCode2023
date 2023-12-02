import init
import typing
import re

data = init.read_data(isTest=False, )


def part1():
	solution = 0
	for line in data:
		ints = init.ints(line)
		x, y = ints[0], ints[-1]
		result = int(str(x)[0] + str(y)[-1])
		print(result, x, y, ints)
		solution += result
	return solution


def lmap(func, *iterables):
	return list(map(func, *iterables))


def intsAndWords(s: str) -> typing.List[int]:
	return lmap(int, re.findall(r"-?\d+", s))


words = [['one', '1'], ['two', '2'], ['three', '3'], ['four', '4'], ['five', '5'], ['six', '6'], ['seven', '7'],
		 ['eight', '8'], ['nine', '9']]


def part2():
	results = []
	for line in data:
		print('orig', line)
		compstring = ''
		for i in range(0, len(line)):
			compstring = compstring + line[i]
			compOld = compstring
			for x, y in words:
				compstring = compstring.replace(x, y)
			if compOld != compstring:
				# change has happened so stop!
				break
			print(compstring)

		# now iterate backwards to avoid missing the wrong number
		revCompstring = ''
		for i in reversed(range(0, len(line))):
			revCompstring = line[i] + revCompstring
			compOld = revCompstring
			for x, y in words:
				revCompstring = revCompstring.replace(x, y)
			if compOld != revCompstring:
				# change has happened so stop!
				compstring = compstring + revCompstring
				break
			print(revCompstring)

		ints = init.ints(compstring)
		x, y = ints[0], ints[-1]
		result = int(str(x)[0] + str(y)[-1])
		print('RESULT', result)
		results.append(result)
	return sum(results)



print(f'Part 1: {part1()}, Part 2: {part2()}')
