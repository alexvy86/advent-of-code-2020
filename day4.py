import re
from utils import read_lines

hgt_regex = re.compile(r"^(?P<num>\d*)(?P<unit>(?:cm|in)?)$")
hcl_regex = re.compile(r"^#[0-9a-f]{6}$")
ecl_regex = re.compile(r"^amb|blu|brn|gry|grn|hzl|oth$")
pid_regex = re.compile(r"^\d{9}$")


def is_valid_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(field_name in passport for field_name in required_fields)


def is_valid_passport_v2(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if not all(field_name in passport for field_name in required_fields):
        return False

    byr = int(passport["byr"])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(passport["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(passport["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    hgt_match = hgt_regex.match(passport["hgt"])
    if hgt_match.group('unit') == "":
        return False
    hgt_num = int(hgt_match.group('num'))
    if hgt_match.group('unit') == "cm" and (hgt_num < 150 or hgt_num > 193):
        return False
    if hgt_match.group('unit') == "in" and (hgt_num < 59 or hgt_num > 76):
        return False

    if not hcl_regex.match(passport["hcl"]):
        return False

    if not ecl_regex.match(passport["ecl"]):
        return False

    if not pid_regex.match(passport["pid"]):
        return False

    return True


num_of_valid_passports = 0
num_of_valid_passports_v2 = 0

passport = {}
for line in read_lines(4, include_blank_lines=True):
    if line == "":
        if is_valid_passport(passport):
            num_of_valid_passports += 1
        if is_valid_passport_v2(passport):
            num_of_valid_passports_v2 += 1
        passport = {}
    else:
        for kv in line.split(" "):
            passport[kv.split(":")[0]] = kv.split(":")[1]

print(num_of_valid_passports)
print(num_of_valid_passports_v2)
