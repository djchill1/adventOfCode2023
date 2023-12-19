import init
import re

data = init.read_data(isTest=False, )

global workflows
workflows = {}
isWorkflows = True
parts = []
for line in data:
	render = re.split('\{|}', line)
	if line == '':
		isWorkflows = False
		pass
	elif isWorkflows:
		workflows[render[0]] = render[1]
	else:
		parts.append(render[1])

print(workflows)
print(parts)


def part_to_numbers(part):
	splits = init.ints(part)
	nums = {'x': splits[0], 'm': splits[1], 'a': splits[2], 's': splits[3]}
	return nums


def next_workflow_for_part(part, current_workflow):
	# x, m, a, s = part_to_numbers(part)
	nums = part_to_numbers(part)
	rules = workflows[current_workflow]
	rules = re.split(',', rules)
	# print(rules)

	for index, rule in enumerate(rules):

		if index == len(rules) - 1:
			# at the last rule so redirect
			return rule

		else:
			# still rules to check
			rule = re.split(':', rule)
			print(rule)
			category = rule[0][0]
			operator = rule[0][1]
			value = init.ints(rule[0])[0]
			ifSuccess = rule[1]

			actualValue = nums[category]

			if operator == '<':
				if actualValue < value:
					return ifSuccess
			elif operator == '>':
				if actualValue > value:
					return ifSuccess
			else:
				print('unsupported operator')


# print(next_workflow_for_part('x=787,m=2655,a=1222,s=2876', 'in'))


def part1():
	accepted_values = []
	for part in parts:
		current_workflow = 'in'
		print('checking part', part)
		print(current_workflow)
		while current_workflow not in ('R', 'A'):
			current_workflow = next_workflow_for_part(part, current_workflow)
			print(current_workflow)
		if current_workflow == 'A':
			# sum x,m,a,s
			accepted_values.append(sum(init.ints(part)))
	return sum(accepted_values)


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
