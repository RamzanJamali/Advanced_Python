from hello_parallel import square_parallel, square_serial
import numpy as np 
import cProfile

numbers_1 = np.array(range(10000000), dtype='double')
#cProfile.run("square_serial(numbers_1)")

numbers_2 = np.array(range(10000000), dtype='double')
#cProfile.run("square_parallel(numbers_2)")



from cevolve import c_evolve, c_evolve_openmp
from random import uniform

class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


# To simulate the particles
class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles


    # The second method utilizes cython for simulation        
    def evolve_cython(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        # nsteps = 1000 if dt = 0.01

        r_i = np.array([[p.x, p.y] for p in self.particles])
        ang_speed_i = np.array([p.ang_vel for p in self.particles])
        
        c_evolve(r_i, ang_speed_i, timestep, nsteps)
        
        for i, p in enumerate(self.particles):
            p.x, p.y = r_i[i]

    
    # The second method utilizes cython for simulation        
    def evolve_cython_openmp(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        # nsteps = 1000 if dt = 0.01

        r_i = np.array([[p.x, p.y] for p in self.particles])
        ang_speed_i = np.array([p.ang_vel for p in self.particles])
        
        c_evolve_openmp(r_i, ang_speed_i, timestep, nsteps)
        
        for i, p in enumerate(self.particles):
            p.x, p.y = r_i[i]


# To benchmark the different methods
def benchmark(npart=100, method='cython'):
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(npart)
    ]

    simulator = ParticleSimulator(particles)
    
    if method == 'cython':
        simulator.evolve_cython(0.1)
        
    elif method == 'openmp':
        simulator.evolve_cython_openmp(0.1)


cProfile.run("benchmark(10000, 'cython')")

cProfile.run("benchmark(10000, 'openmp')")