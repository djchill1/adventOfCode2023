import init
import re

data = init.read_data(isTest=False, )

def splitCard(row):
	card, winners, actualNumbers = re.split(':|\|',row)
	card = init.ints(card)[0]
	winners = init.ints(winners)
	actualNumbers = init.ints(actualNumbers)
	return card, winners, actualNumbers

global totalWinnersPerCard, copies
totalWinnersPerCard = []
copies = []

def part1():
	scores = []
	for line in data:
		winningNumbers = 0
		card, winners, actualNumbers = splitCard(line)
		for number in actualNumbers:
			if number in winners:
				winningNumbers += 1
		if winningNumbers > 0:
			score = pow(2,winningNumbers-1)
		else:
			score = 0
		scores.append(score)
		totalWinnersPerCard.append(winningNumbers)
		copies.append(1)
		print('card #', card, 'winning numbers:', winningNumbers, 'score:', score)
	return sum(scores)


def part2():
	for index, value in enumerate(totalWinnersPerCard):
		card = index + 1
		print('card #', card, value)
		# play per card
		toplay = copies[index]
		for time in range(0, toplay):
			# print('playing a game for card', card, 'total to play', toplay)
			# results of each card
			for i in range(index, index+value):
				copies[i+1] += 1
				# print(copies)
	return sum(copies)


print(f'Part 1: {part1()}, Part 2: {part2()}')