# --- Day 20: Particle Swarm ---
# part 1 -


particles = {}
with open('input.txt', 'r') as fp:

    for c,line in enumerate(fp):
        particle = []
        line = line.rstrip().split(', ')

        for p in line:
            p = p.split(',')
            particle.append(int(p[0][3:]))
            particle.append(int(p[1]))
            particle.append(int(p[2][:-1]))
        particles[c] = particle


# For each particle, it provides the X, Y, and Z coordinates for the
# particle's position (p), velocity (v), and acceleration (a), each in the
# format <X,Y,Z>.

# Each tick, all particles are updated simultaneously. A particle's
# properties are updated in the following order:


for i in range(1000):

    for particle in particles:
        # [p(x,y,z), v(x,y,z), a(x,y,z)]
        #    0,1,2     3,4,5     6,7,8

        # Increase the X velocity by the X acceleration.
        particle[3] = particle[3] + particle[6]
        # Increase the Y velocity by the Y acceleration.
        particle[4] = particle[4] + particle[7]
        # Increase the Z velocity by the Z acceleration.
        particle[5] = particle[5] + particle[8]
        # Increase the X position by the X velocity.
        particles[0] = particles[0] + particles[3]
        # Increase the Y position by the Y velocity.
        particles[1] = particles[1] + particles[4]
        # Increase the Z position by the Z velocity.
        particles[2] = particles[2] + particles[5]

shortest = -1

for n,particle in particles.items():
    # Calculate

    x = abs(0 - particle[0])
    y = abs(0 - particle[1])
    z = abs(0 - particle[2])

    distance = x + y + z

    if distance >