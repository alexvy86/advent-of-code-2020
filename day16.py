from math import prod

file_reader = open(f"input/day16.txt", "r")

rules = {}
line = file_reader.readline()
while line != "\n":
	rule_name, rule_specs = line.split(": ")
	rules[rule_name] = [(int(entry.split("-")[0]), int(entry.split("-")[1])) for entry in rule_specs.split(" or ")]
	line = file_reader.readline()

file_reader.readline() # "your ticket:" header
my_ticket = [int(n) for n in file_reader.readline().split(",")]
file_reader.readline() # empty line
file_reader.readline() # "nearby tickets:" header

nearby_tickets = []
line = file_reader.readline()
while line != "":
	nearby_tickets.append([int(n) for n in line.split(",")])
	line = file_reader.readline()

file_reader.close()

scanning_error_rate = 0
valid_tickets = []
for ticket in nearby_tickets:
	is_ticket_valid = True
	for number in ticket:
		if all(number < spec[0] or number > spec[1] for rule_specs in rules.values() for spec in rule_specs):
			scanning_error_rate += number
			is_ticket_valid = False
	if is_ticket_valid:
		valid_tickets.append(ticket)

print(scanning_error_rate)

# Start with all rules being possible for all numbers. Scan the numbers in each ticket and remove
# the rules that don't work for it from the list of its candidates.
possible_rules = [list(rules.keys()) for i in range(len(valid_tickets[0]))]
for ticket in valid_tickets:
	for i, number in enumerate(ticket):
		for rule_name, rule_specs in rules.items():
			if all(number < spec[0] or number > spec[1] for spec in rule_specs) and rule_name in possible_rules[i]:
				possible_rules[i].remove(rule_name)

# Some number end up with several possibilities for the rule that matches them. One only matches 1 rule,
# another matches 2, another 3... so propagate the constraints starting with the one that we know for sure.
for sure_rule in sorted(possible_rules, key=len):
	for in_progress_rule in possible_rules:
		if len(in_progress_rule) > 1 and sure_rule[0] in in_progress_rule:
			in_progress_rule.remove(sure_rule[0])

# Calculate product of required numbers from my ticket
print(prod(my_ticket[i] for i, rule_name in enumerate(possible_rules) if rule_name[0].startswith("departure")))
