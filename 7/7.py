import init
import re
import collections

data = init.read_data(isTest=True, )

strengthOrder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
strengthOrder.reverse()

# strength order of counts of unique cards in a hand.
# e.g. "5" means all 5 cards are the same.
handTypesInStrengthOrder = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]


def find_a_hands_type(hand):
	cards = re.split('', hand)
	cards = cards[1:len(cards) - 1]
	counts = collections.Counter(cards)
	c = tuple(sorted(counts.values()))
	return handTypesInStrengthOrder.index(c)

def order_strongest_hands():
	return False


def part1():
	handRanks = []
	hands = []
	bids = []
	for line in data:
		hand, bid = re.split(' ', line)
		hands.append(hand)
		bids.append(bid)
		print(hand, 'bid:', bid)
		handRanks.append(find_a_hands_type(hand))
	print(handRanks)

	# figure out best hands.
	finalRanks = handRanks
	maxRank = len(handRanks)
	current_rank = 1
	for handStrength in range(1, 6):
		print('resolving ties at strength', handStrength)
		resolveIndexes = []
		for index, value in enumerate(handRanks):
			if value == handStrength:
				resolveIndexes.append(index)

		print(resolveIndexes)
		if len(resolveIndexes) == 1:
			finalRanks[resolveIndexes[0]] = current_rank
			print('no clashes. Final rank of', hands[resolveIndexes[0]], 'is', current_rank, '\n')
			current_rank += 1

		elif len(resolveIndexes) == 0:
			# nothing to resolve
			print('nothing to resolve \n')
			continue

		# else check conflicts and figure out which is next
		else:
			# get all hands
			solveHands = []
			character = 0
			for index in resolveIndexes:
				solveHands.append(hands[index])
			while len(solveHands) > 0:
				chars = []
				# check each character of each hand
				for hand in solveHands:
					chars.append(hand[character])
				for index,



	return False


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
