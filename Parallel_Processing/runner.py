from hello_parallel import square_parallel, square_serial
import numpy as np 
import cProfile

numbers_1 = np.array(range(10000000), dtype='double')
cProfile.run("square_serial(numbers_1)")

numbers_2 = np.array(range(10000000), dtype='double')
cProfile.run("square_parallel(numbers_2)")
