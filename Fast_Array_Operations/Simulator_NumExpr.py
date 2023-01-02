import numpy as np
import numexpr as ne
import cProfile

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

    # The first method utilizes numexpr for simulation
    def evolve_numexpr(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        # nsteps = 1000 if dt = 0.01
        for i in range(nsteps):
            for p in self.particles:
                # 1. Calculate the direction
                px = p.x
                py = p.y
                norm = ne.evaluate('(px**2 + py**2)**0.5')
                v_x = ne.evaluate("-py/norm")
                v_y = ne.evaluate("px/norm")

                # 2. Calculate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y
                # 3. repeat for all the timesteps 

        
    # The second method utilizes numpy for simulation
    def evolve_numpy(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        # nsteps = 1000 if dt = 0.01

        r_i = np.array([[p.x, p.y] for p in self.particles])
        ang_vel_i = np.array([p.ang_vel for p in self.particles])
        
        for i in range(nsteps):
            
            norm_ii = (r_i ** 2).sum(axis=1)
            norm_i = np.sqrt(norm_ii)
            v_i = r_i[:, [1, 0]]
            v_i[:, 0] *= -1
            v_i /= norm_i[:, np.newaxis]
            d_i = timestep * ang_vel_i[:, np.newaxis] * v_i
            r_i += d_i
            
            for i, p in enumerate(self.particles):
                p.x, p.y = r_i[i]

    # The third method is normal and is from chapter 1            
    def evolve_python(self, dt):
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

# This benchmark is to check how our code is performing
from random import uniform

def benchmark(npart=100, method='python'):
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(npart)
    ]

    simulator = ParticleSimulator(particles)

    if method == 'python':
        simulator.evolve_python(0.1)
        
    elif method == 'numpy':
        simulator.evolve_numpy(0.1)

    elif method == 'numexpr':
        simulator.evolve_numexpr(0.1)

if __name__ == '__main__':
    cProfile.run('benchmark(10, "numexpr")')
    pass

# To check performance use ipython: 
# %timeit benchmark(100, "python")
# and
# %timeit benchmark(100, "numpy")

# Result: You will see that numpy version is better for high number of particles.