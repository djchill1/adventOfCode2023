import init
import numpy as np
import re

data = init.read_data(isTest=False, )

symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# find all symbols
chars = []
for line in data:
	for element in line:
		if element not in chars:
			chars.append(element)

print('all characters present are', sorted(chars))

# make the individual matrix
matrix = []
maxi = -1
for line in data:
	maxi += 1
	matrix.append(re.split('', line))
maxj = len(matrix[0]) - 1
# matrix[i][j] i = row index, j = col index

print(maxi, maxj)


def constructNumberFromIndex(index, matrix, indexesChecked):
	# go as far left as long as still numeric.
	i, j = index
	print('checking', i, j)
	if (i, j) in indexesChecked:
		print('already checked', i, j)
		print('')
		return 0, indexesChecked

	indexesChecked.append((i, j))
	number = matrix[i][j]
	numberbuilder = []
	while number in numbers:
		print('adding number', number, 'at pos', i, j)
		numberbuilder[:0] = [number]
		j -= 1
		number = matrix[i][j]
		indexesChecked.append((i, j))
		print('next char', number, 'at pos', i, j)

	print('left done')
	# then as far right
	i, j = index
	j += 1
	number = matrix[i][j]
	while number in numbers:
		numberbuilder.append(number)
		indexesChecked.append((i, j))
		j += 1
		number = matrix[i][j]
		print('next char', number, 'at pos', i, j)

	print('right done')

	# stitch together
	# print('number is', numberbuilder)
	result = int(''.join(numberbuilder))
	print('number is', result)
	print(' ')
	return result, indexesChecked


def part1():
	indexesChecked = []
	adjacentIndexes = []
	for i in range(0, maxi + 1):
		for j in range(0, maxj + 1):
			if matrix[i][j] in numbers:
				print(i, j, matrix[i][j], 'is numeric')
				for dir in init.all_dirs:
					try:
						if matrix[i + dir[0]][j + dir[1]] in symbols:
							adjacentIndexes.append((i, j))
							print(i, j, matrix[i][j], 'is next to a symbol of value', matrix[i + dir[0]][j + dir[1]])
					except:
						continue
	print(adjacentIndexes)
	partNumbers = []
	for index in adjacentIndexes:
		result, indexesChecked = constructNumberFromIndex(index, matrix, indexesChecked)
		partNumbers.append(result)
	return sum(partNumbers)


def part2():
	indexesChecked = []
	gearIndexes = []
	adjacentIndexes = []
	gearRatios = []
	for i in range(0, maxi + 1):
		for j in range(0, maxj + 1):
			if matrix[i][j] == '*':
				print(i, j, matrix[i][j], 'is a gear!')
				gearIndexes.append((i,j))
				possibleAdjacentNumbers = 0
				tempAdjacentIndexes = []
				partNumbers = []
				for dir in init.all_dirs:
					try:
						if matrix[i + dir[0]][j + dir[1]] in numbers:
							possibleAdjacentNumbers += 1
							tempAdjacentIndexes.append((i + dir[0], j + dir[1]))
							print(i, j, matrix[i][j], 'is next to a number of value', matrix[i + dir[0]][j + dir[1]])
					except:
						continue
				if possibleAdjacentNumbers >= 2:
					print('sufficient close numbers to warrant further checking on', tempAdjacentIndexes)
					adjacentIndexes.append(tempAdjacentIndexes)
					for index in tempAdjacentIndexes:
						result, indexesChecked = constructNumberFromIndex(index, matrix, indexesChecked)
						if result != 0:
							partNumbers.append(result)
						print('partNumbers for this one are', partNumbers,'\n')
				if len(partNumbers) == 2:
					gearRatio = partNumbers[0]*partNumbers[1]
					gearRatios.append(gearRatio)
					print('new gear ratio found', gearRatio, 'from gear at', i, j, 'partNumbers', partNumbers , '\n')

	# print(gearIndexes)
	# print(adjacentIndexes)
	return sum(gearRatios)


print(f'Part 1: {part1()}, Part 2: {part2()}')
