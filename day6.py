from utils import read_lines

sum_of_yes_questions = 0

questions_for_current_group = set()

for line in read_lines(6, include_blank_lines=True):
	if line == "":
		sum_of_yes_questions += len(questions_for_current_group)
		questions_for_current_group = set()
	else:
		questions_for_current_group.update(char for char in line)

# This is because there's no blank line after the last group so it doesn't get counted in the loop above
sum_of_yes_questions += len(questions_for_current_group)

print(sum_of_yes_questions)