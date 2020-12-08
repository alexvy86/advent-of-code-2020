from utils import read_lines

instructions = read_lines(8)

def execute(instructions):
	accumulator = 0
	executed_instructions = set()

	current_instruction = 0

	while current_instruction not in executed_instructions and current_instruction < len(instructions):
		executed_instructions.add(current_instruction)
		op, arg = instructions[current_instruction].split(" ")
		if op == "jmp":
			current_instruction += int(arg)
		elif op == "acc":
			accumulator += int(arg)
			current_instruction += 1
		elif op == "nop":
			current_instruction += 1
	
	return (accumulator, current_instruction in executed_instructions)

result, looped = execute(instructions)
print(f"{result} - looped: {looped}")

for i in range(len(instructions)):
	change_needs_test = False
	new_instructions = []
	if instructions[i].startswith("jmp"):
		new_instructions = instructions.copy()
		new_instructions[i] = new_instructions[i].replace("jmp", "nop")
		change_needs_test = True
	elif instructions[i].startswith("nop"):
		new_instructions = instructions.copy()
		new_instructions[i] = new_instructions[i].replace("nop", "jmp")
		change_needs_test = True

	if change_needs_test:
		result, looped = execute(new_instructions)
		if not looped:
			print(f"{result} - looped: {looped}, fixed instruction {i}")
			break