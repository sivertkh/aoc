# --- Day 20: Particle Swarm ---
# part 1 - ok

particles = {}
with open('input.txt', 'r') as fp:
    for c, x in enumerate(fp):
        particle = []
        for p in x.rstrip().split(', '):
            p = p.split(',')
            particle.append(int(p[0][3:]))
            particle.append(int(p[1]))
            particle.append(int(p[2][:-1]))
        particles[c] = particle

# Over time, the particle with the smallest combined acceleration will always be closest to 000
pos = -1
acc = 100000
for c,v in particles.items():
    cacc = abs(v[6]) + abs(v[7]) + abs(v[8])

    if cacc < acc:
        acc = cacc
        pos = c
    elif pos == '-1':
        acc = cacc
        pos = c

print("particle: {}, acc: {}".format(pos, acc))
