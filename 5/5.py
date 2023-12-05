import init
import re

data = init.read_data(isTest=False, )


def math_remap_seed(seeds, rangesList):
	for index, seed in enumerate(seeds):
		for row in rangesList:
			row = init.ints(row)
			if seed in range(row[1], row[1]+row[2]):
				# can update
				newSeed = (seed - row[1]) + row[0]
				seeds[index] = newSeed
				print('can update!', seed, newSeed)
	return seeds


def part1():
	seeds = init.ints(data[0])
	indexes = []
	mapIndexes = []
	for index, line in enumerate(data):
		if 'map' in line:
			indexes.append(index)
	indexes.append(len(data))
	# print(indexes)
	for index, entry in enumerate(indexes):
		try:
			mapIndexes.append((entry + 1, indexes[index + 1] - 1))
		except:
			continue
	print(mapIndexes)

	# loop through each map group for every seed
	for mapRange in mapIndexes:
		seeds = math_remap_seed(seeds, data[mapRange[0]:mapRange[1]])

		print(seeds)

	return min(seeds)


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
