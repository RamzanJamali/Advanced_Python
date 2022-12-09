from simulator import Particle, ParticleSimulator

def test_evolve(benchmark):
    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, 3)
    ]

    simulator = ParticleSimulator(particles)

    simulator.evolve(0.1)

    p0, p1, p2 = particles

    def fequal(a, b, eps=1e-5):
        return abs(a-b) < eps

    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)

    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)
    
    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)

    benchmark(simulator.evolve, 0.1)

# To run test using pytest run this command
# pytest test_simulator.py::test_evolve

# There are two ways to test the performance of this program by cProfile

# First import the required things
from simulator import benchmark
import cProfile

# Method 1: Run whole code
cProfile.run("benchmark()")

# Method 2 : To wrap it around the benchmark function
pr =cProfile.Profile()
pr.enable()
benchmark()
pr.disable()
pr.print_stats()


# To disassemble the evolve first comment the @profile in simulator
import dis

dis.dis(ParticleSimulator.evolve)