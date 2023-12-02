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

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')