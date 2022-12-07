
# This program will simulate particles moving in a circular path at a constant speed. 
# The purpose of this simulation is to improve performance of python program.
class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel

# To simulate the particles
class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        # nsteps = 1000 if dt = 0.01

        for i in range(nsteps):
            for p in self.particles:
                # 1. Calculate the direction
                norm = (p.x**2 + p.y**2)**0.5
                v_x = -p.y/norm
                v_y = p.x/norm

                # 2. Calculate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y
                # 3. repeat for all the timesteps 


# To visualize the simulation            
from matplotlib import pyplot as plt
from matplotlib import animation

def visualize(simulator):

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()

    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will run when animation starts
    def init():
        line.set_data([], [])
        return line, # comma is important

    def animate(i):
        # We let the particle evolve for 0.01 time units
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return line,

    # Call the animation function each 10 ms
    anim = animation.FuncAnimation(fig, animate, init_func=init, blit= True, interval = 10)
    plt.show()

# To visualize the particles
def test_visualize():
    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, 3)
    ]

    simulator = ParticleSimulator(particles)
    visualize(simulator)


if __name__ == '__main__':
    test_visualize()