from utils import read_lines

sum_of_yes_questions = 0
sum_of_yes_questions_everyone = 0

questions_for_current_group = set()
questions_for_everyone_in_current_group = set()

new_group = True

for line in read_lines(6, include_blank_lines=True):
	if line == "":
		# print(questions_for_everyone_in_current_group)
		sum_of_yes_questions += len(questions_for_current_group)
		sum_of_yes_questions_everyone += len(questions_for_everyone_in_current_group)
		questions_for_current_group = set()
		new_group = True
	else:
		questions_for_current_group.update(char for char in line)
		if new_group:
			questions_for_everyone_in_current_group = set(line)
			new_group = False
		else:
			questions_for_everyone_in_current_group = questions_for_everyone_in_current_group.intersection(line)
		
# This is because there's no blank line after the last group so it doesn't get counted in the loop above
sum_of_yes_questions += len(questions_for_current_group)
sum_of_yes_questions_everyone += len(questions_for_everyone_in_current_group)

print(sum_of_yes_questions)
print(sum_of_yes_questions_everyone)