from utils import read_lines
from math import prod

def evaluate(expr):
	i = 0
	operator = "+"
	running_result = 0
	while i < len(expr):
		if expr[i] in ["+", "*"]:
			operator = expr[i]
			i += 1
			continue

		if expr[i] == ")":
			return (running_result, i + 1)

		if expr[i] == "(":
			next_number, consumed_chars = evaluate(expr[i+1:])
			i += consumed_chars
		else:
			next_number = int(expr[i])
		
		running_result = running_result + next_number if operator == "+" else running_result * next_number
	
		i += 1

	return (running_result, len(expr))

print(sum(evaluate(line.replace(" ", ""))[0] for line in read_lines(18)))
