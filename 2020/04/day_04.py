# --- Day 4: Passport Processing ---
import re

with open('./input.txt') as fp:
    passports = [x.replace('\n', ' ').split() for x in fp.read().split('\n\n')]
    passports = [dict(y.split(':') for y in x) for x in passports]

valid_sets = [
    set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']),
    set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    ]

valid_1 = valid_2 = 0
for passport in passports:
    if any([set(passport.keys()) == x for x in valid_sets]):
        valid_1 += 1

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not (len(passport['byr']) == 4 and
                1920 <= int(passport['byr']) <= 2002):
            continue

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not (len(passport['iyr']) == 4 and
                2010 <= int(passport['iyr']) <= 2020):
            continue

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not (len(passport['eyr']) == 4 and
                2020 <= int(passport['eyr']) <= 2030):
            continue

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        height = re.match(r'(\d*)(cm|in)', passport['hgt'])
        if not height:
            continue
        height = list(height.groups())
        if not ((len(height) == 2 and height[0].isnumeric()) and
                ((height[1] == 'cm' and 150 <= int(height[0]) <= 193) or
                (height[1] == 'in' and 59 <= int(height[0]) <= 76))):
            continue

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not re.search(r'^#[0-9a-f]{6}$', passport['hcl']):
            continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not (len(passport['pid']) == 9 and passport['pid'].isnumeric()):
            continue

        # cid (Country ID) - ignored, missing or not.

        valid_2 += 1

print(f'Part 1: {valid_1}')
print(f'Part 2: {valid_2}')
