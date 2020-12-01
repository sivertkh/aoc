# --- Day 20: Particle Swarm ---
# part 2 - ok

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

print(len(particles))
for i in range(1000):

    # check for collisions

    known_pos = {}
    for c,particle in particles.items():

        pos = ",".join(str(x) for x in particle[:3])

        if pos in known_pos:
            known_pos[pos].append(c)
        else:
            known_pos[pos] = [c]

    for c,particle in particles.items():
        # [p(x,y,z), v(x,y,z), a(x,y,z)]
        #    0,1,2     3,4,5     6,7,8
        # Increase the X velocity by the X acceleration.
        particle[3] = particle[3] + particle[6]
        # Increase the Y velocity by the Y acceleration.
        particle[4] = particle[4] + particle[7]
        # Increase the Z velocity by the Z acceleration.
        particle[5] = particle[5] + particle[8]
        # Increase the X position by the X velocity.
        particle[0] = particle[0] + particle[3]
        # Increase the Y position by the Y velocity.
        particle[1] = particle[1] + particle[4]
        # Increase the Z position by the Z velocity.
        particle[2] = particle[2] + particle[5]

    for k,v in known_pos.items():
        if len(v) > 1:
            for j in v:
                del particles[j]

print(len(particles))
