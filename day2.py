from utils import read_lines
import re

numOfValidPasswords = 0
numOfValidPasswords2ndPolicy = 0

regex = re.compile(r"(?P<minTimes>\d+)\-(?P<maxTimes>\d+) (?P<character>\w)\: (?P<password>\w+)")
for x in read_lines(2):
    parsed = regex.match(x)
    minTimes = int(parsed.group('minTimes'))
    maxTimes = int(parsed.group('maxTimes'))
    character = parsed.group('character')
    password = parsed.group('password')

    numOfCharInPassword = len(re.findall(f"{character}", password))

    # print(f"{minTimes} {maxTimes} {character} {numOfCharInPassword} {password}")

    if minTimes <= numOfCharInPassword <= maxTimes:
        numOfValidPasswords += 1

    if (password[minTimes - 1] == character) ^ (password[maxTimes - 1] == character):
        numOfValidPasswords2ndPolicy += 1

print(numOfValidPasswords)
print(numOfValidPasswords2ndPolicy)