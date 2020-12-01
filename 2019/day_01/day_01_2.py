# --- Day 1: The Tyranny of the Rocket Equation ---
# Part 2 - Ok

with open('./input.txt') as fp:
    modules = [(int(x)//3)-2 for x in fp.read().split('\n') if x]
    fule_req = sum(modules)

    while len(modules) > 0:
        fule = [(int(x)//3)-2 for x in modules]
        fule_filtered = [x for x in fule if x > 0]
        fule_req += sum(fule_filtered)
        modules = fule_filtered

    print(fule_req)
