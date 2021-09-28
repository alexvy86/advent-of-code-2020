import re

rules = {}

with open(f"input/day19.txt", "r") as file_reader:
	line = file_reader.readline()
	while line != "\n":
		rule_num, rule_description = line.split(": ")
		rules[rule_num] = rule_description.replace("\n","")
		line = file_reader.readline()

	messages = []
	while line != "":
		messages.append(line.replace("\n", ""))
		line = file_reader.readline()

def parse_rule(rule_definition, parsed_rules, raw_rules):
	parsed_rule = ""
	for piece in str.split(rule_definition, " | "):
		for subrule_num in str.split(piece, " "):
			if str.isnumeric(subrule_num):
				if subrule_num not in parsed_rules:
					parsed_rules[subrule_num] = parse_rule(raw_rules[subrule_num], parsed_rules, raw_rules)
				parsed_subrule = parsed_rules[subrule_num]
				if "|" in parsed_subrule:
					parsed_subrule = f"({parsed_subrule})"
				parsed_rule += parsed_subrule
			else:
				parsed_rule += subrule_num.replace("\"", "")
		parsed_rule += "|"
	return parsed_rule[:-1] # Remove the "|" at the end, which I'm always appending

parsed_rules = {}
for rule_num, rule_def in rules.items():
	parsed_rules[rule_num] = parse_rule(rule_def, parsed_rules, rules)

num_of_messages_that_match_rule_0 = len([m for m in messages if re.fullmatch(f"{parsed_rules['0']}", m)])
print(num_of_messages_that_match_rule_0)
