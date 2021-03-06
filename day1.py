import utils
from utils import read_lines

expenses = [int(x) for x in read_lines(1)]
numOfExpenses = len(expenses)

expense1 = 0
expense2 = 0

for currentIndex1 in range(0, numOfExpenses - 1):
    expense1 = expenses[currentIndex1]
    for currentIndex2 in range(currentIndex1 + 1, numOfExpenses):
        expense2 = expenses[currentIndex2]
        if expense1 + expense2 == 2020:
            break
    if expense1 + expense2 == 2020:
        break

print(expense1 * expense2)

expense1 = 0
expense2 = 0
expense3 = 0

for currentIndex1 in range(0, numOfExpenses - 2):
    expense1 = expenses[currentIndex1]
    for currentIndex2 in range(currentIndex1 + 1, numOfExpenses - 1):
        expense2 = expenses[currentIndex2]
        for currentIndex3 in range(currentIndex2 + 1, numOfExpenses):
            expense3 = expenses[currentIndex3]
            if expense1 + expense2 + expense3 == 2020:
                break
        if expense1 + expense2 + expense3 == 2020:
            break
    if expense1 + expense2 + expense3 == 2020:
        break

print(expense1 * expense2 * expense3)
