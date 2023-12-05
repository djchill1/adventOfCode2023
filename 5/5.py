import init
import re

data = init.read_data(isTest=False, )


def math_remap_seeds(seeds, rangesList):
	for index, seed in enumerate(seeds):
		for row in rangesList:
			row = init.ints(row)
			if seed in range(row[1], row[1]+row[2]):
				# can update
				newSeed = (seed - row[1]) + row[0]
				seeds[index] = newSeed
				print('can update!', seed, newSeed)
	return seeds


def math_remap_seed(seed, rangesList):
	for row in rangesList:
		row = init.ints(row)
		# print('checking', row)
		if seed in range(row[1], row[1]+row[2]):
			# can update
			newSeed = (seed - row[1]) + row[0]
			# print('can update!', seed, newSeed)
			seed = newSeed
			return seed
		else:
			# print('cannot update', seed)
			continue
	return seed


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
		seeds = math_remap_seeds(seeds, data[mapRange[0]:mapRange[1]])

		print(seeds)

	return min(seeds)


def part2():
	print('part 2')
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
	minLocation = 1000000000000000000
	# loop through each map group for every seed
	seed_starts = [(seeds[0], seeds[1]), (seeds[2], seeds[3])]
	for info in seed_starts:
		for seed in range(info[0], info[0]+info[1]):
			# print(seed)
			for mapRange in mapIndexes:
				seed = math_remap_seed(seed, data[mapRange[0]:mapRange[1]])
			if seed < minLocation:
				minLocation = seed

	return minLocation


print(f'Part 1: {part1()}, Part 2: {part2()}')
