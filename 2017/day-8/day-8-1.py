
register = {}


def get_register_value(name):

    if name not in register:
        register[name] = 0

    return register[name]


with open('input.txt', 'r') as fp:
    inst = [x.rstrip().split(" ") for x in fp.read().split('\n')]

t = [x[1] for x in inst]

for i in inst:
    reg = i[0]
    instruction = i[1]
    value = int(i[2])

    if_reg = get_register_value(i[4])

    if eval("{}{}{}".format(if_reg, i[5], i[6])):
        if instruction == 'inc':
            if reg in register:
                register[reg] = register[reg] + value
            else:
                register[reg] = 0 + value
        elif instruction == 'dec':
            if reg in register:
                register[reg] = register[reg] - value
            else:
                register[reg] = 0 - value

print(max([v for k,v in register.items()]))
