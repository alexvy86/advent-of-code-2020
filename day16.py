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
for ticket in nearby_tickets:
	for number in ticket:
		if all(number < spec[0] or number > spec[1] for rule_specs in rules.values() for spec in rule_specs):
			scanning_error_rate += number

print(scanning_error_rate)
