import init
import re

data = init.read_data(isTest=True, )


def completeMap(rangesList):
	map = {}
	for row in rangesList:
		row = init.ints(row)
		destinationStart, sourceStart, length = row
		for i in range(0, length):
			map[sourceStart + i] = destinationStart + i
	return map

def remapSeed(seeds, partialMap):
	output = []
	for seed in seeds:
		try:
			output.append(partialMap[seed])
			# print('remapped')
		except:
			output.append(seed)

	return output

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
		partialMap = completeMap(data[mapRange[0]:mapRange[1]])

		# run every seed through the index
		seeds = remapSeed(seeds, partialMap)
		print(seeds)

	return min(seeds)


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
