import init
import re

data = init.read_data(isTest=False, )

def isGamePossible(observedDict, maximumsDict):
	for key, value in observedDict.items():
		# print('checking', key, value)
		if value > maximumsDict[key]:
			# print('found', maximumsDict[key])
			return False
	return True


def part1():
	maximums = {'red': 12, 'green': 13, 'blue': 14}
	possibleGames = []

	for line in data:
		line = line.replace(',', '')
		row = re.split(' |:|;|,', line)
		# print(row)
		gameNumber = int(row[1])
		largestObserved = {'red': 0, 'green': 0, 'blue': 0}
		for i in range(0, len(row)):
			if row[i] in maximums.keys():
				key, val = row[i], int(row[i-1])
				# print(key, val)
				if largestObserved[key] < val:
					largestObserved[key] = val
		print('GAME', gameNumber, largestObserved)
		isPossible = isGamePossible(largestObserved, maximums)
		if not isPossible:
			print('game', gameNumber, 'is not possible')
		else:
			possibleGames.append(gameNumber)
	return sum(possibleGames)


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
