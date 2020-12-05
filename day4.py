from utils import read_lines


def is_valid_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(field_name in passport for field_name in required_fields)


num_of_valid_passports = 0

passport = {}
for line in read_lines(4, include_blank_lines=True):
    if line == "":
        if is_valid_passport(passport):
            num_of_valid_passports += 1
        passport = {}
    else:
        for kv in line.split(" "):
            passport[kv.split(":")[0]] = kv.split(":")[1]

print(num_of_valid_passports)
