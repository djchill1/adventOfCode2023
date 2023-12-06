import init
import math

data = init.read_data(isTest=False, )

# parse data
times = init.ints(data[0])
distanceRecords = init.ints(data[1])


def part1():
	allWaysToWin = []
	for index, maxTime in enumerate(times):
		distanceRecord = distanceRecords[index]
		waysToWin = 0
		for holdTime in range(1, maxTime):
			travelTime = maxTime - holdTime
			distance = travelTime * holdTime
			print(maxTime, 'holding for', holdTime, 'travels', distance)
			if distance > distanceRecord:
				waysToWin += 1
		allWaysToWin.append(waysToWin)
		print('total ways to win are', waysToWin)

	result = 1
	for value in allWaysToWin:
		result *= value
	return result


def part2():
	isTest = False
	if isTest:
		distanceRecord = 940200
		maxTime = 71530
	else:
		maxTime = 56977875
		distanceRecord = 546192711311139

	# solve quadratic x^2 - maxTime*x + distanceRecord = 0
	a = 1
	b = -maxTime
	c = distanceRecord
	d = b**2 - 4*a*c

	# solutions
	sols = [(-b + d**0.5) / 2*a, (-b - d**0.5) / 2*a]
	sols = sorted(sols)
	print('solution range between', sols)
	print(math.floor(sols[1]), math.ceil(sols[0]))

	return math.floor(sols[1])-math.ceil(sols[0]) + 1



	# print('total ways to win are', waysToWin)
	# return waysToWin


print(f'Part 1: {part1()}, Part 2: {part2()}')
