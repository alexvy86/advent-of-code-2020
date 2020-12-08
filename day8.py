from utils import read_lines

accumulator = 0
executed_instructions = set()

instructions = read_lines(8)

current_instruction = 0

while current_instruction not in executed_instructions:
	executed_instructions.add(current_instruction)
	op, arg = instructions[current_instruction].split(" ")
	if op == "jmp":
		current_instruction += int(arg)
	elif op == "acc":
		accumulator += int(arg)
		current_instruction += 1
	elif op == "nop":
		current_instruction += 1

print(accumulator)