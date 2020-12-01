# --- Day 6: Universal Orbit Map ---
# Part 1 - ok

with open('./input.txt') as fp:
    orbits = {x[1]: x[0]
              for x in [x.split(')') for x in fp.read().split('\n') if x]}

nr_orbits = 0
for planet in orbits.keys():
    current_planet = planet
    while True:
        if current_planet == 'COM':
            break
        nr_orbits += 1
        current_planet = orbits[current_planet]

print(nr_orbits)
