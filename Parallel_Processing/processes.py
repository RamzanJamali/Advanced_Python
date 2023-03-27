# This code can be used as a template to create and run multiple processes concurrently for tasks 
# such as parallel processing, threading, or other multiprocessing tasks.

import multiprocessing
import time

# The "Process" class has an initializer method that sets the ID of each process, and a "run" method 
# that defines what each process should do when started.
class Process(multiprocessing.Process):
    def __init__(self, id) -> None:
        super(Process, self).__init__()
        self.id = id

    # In this case, the "run" method sleeps for 1 second (using the "time.sleep()" function) and 
    # then prints a message that identifies the process with its assigned ID.
    def run(self):
        time.sleep(1)
        print("I'm the process with id {}".format(self.id))



def square(x):
    return x * x

# The program first defines a function called "map_test()" that initializes a multiprocessing.Pool object 
# and creates two different maps using the "pool.map()" and "pool.map_async()" methods to apply a "square" 
# function to a list of input values. The results of each map are printed to the console.
def map_test():
    pool = multiprocessing.Pool()

    inputs = [0, 1, 2, 3, 4]
    outputs = pool.map(square, inputs)
    print(outputs)

    outputs_async = pool.map_async(square, inputs)
    outputs = outputs_async.get()
    print(outputs)


if __name__ == '__main__':
    # Next, the code starts four processes by creating four instances of the "Process" class and calling 
    # their "start()" methods. These processes will run in parallel with the main process.
    processes = Process(1), Process(2), Process(3), Process(4),
    [p.start() for p in processes]

    # Finally, the "map_test()" function is called, which will run in the main process and utilize the 
    # multiprocessing.Pool object to perform parallel computation.
    map_test()