
# This program will simulate particles moving in a circular path at a constant speed. 
# The purpose of this simulation is to improve performance of python program.
class Particle:

    # To reduce memory usage add slots line.
    # Its limitation is that it prevents the addition of attributes other than the ones specified in __slots__ 
    __slots__ = ('x', 'y', 'ang_vel')

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel

# To simulate the particles
class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles

    # The profile decorator is added to check time consumption line by line
    # with line profiler
    # To use line_profiler add @profile to function
    # and use this command on command line:
    # path_to_kernprof.exe -l -v path_to_simulator.py
    # simplified: kernprof.exe -l -v simulator.py


    #@profile
    def evolve_fast(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        # nsteps = 1000 if dt = 0.01

        # Loop order is changed
        for p in self.particles:
            t_x_ang = timestep * p.ang_vel
            for i in range(nsteps):
                norm = (p.x**2 + p.y**2)**0.5
                p.x, p.y = (p.x - t_x_ang * p.y/norm, p.y + t_x_ang * p.x/norm)


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
        simulator.evolve_fast(0.01)
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

# This benchmark is to check how our code is performing
from random import uniform

def benchmark():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(1000)
    ]

    simulator = ParticleSimulator(particles)
    simulator.evolve_fast(0.1)
    

# to check memory usage run ipython (F5)
# Enter following commnands: 1. %load_ext memory_profiler
# 2. from simulator_v2 import benchmark_memory_2
# 3. %mprun -f benchmark_memory_2 benchmark_memory_2() 
@profile
def benchmark_memory_2():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(100000)
    ]

    simulator = ParticleSimulator(particles)
    simulator.evolve_fast(0.001)


if __name__ == '__main__':
    # test_visualize()
    pass