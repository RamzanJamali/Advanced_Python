# The code imports the multiprocessing module and creates a Lock object to allow multiple processes 
# to safely access a shared resource.

# It then defines two classes, "Process" and "Locked_Process", that inherit from the 
# "multiprocessing.Process" class.

import multiprocessing

lock = multiprocessing.Lock()

# The Process class takes a counter parameter in its constructor and 
# increments it 1000 times in its run method.
class Process(multiprocessing.Process):
    def __init__(self, counter):
        super(Process, self).__init__()
        self.counter = counter

    
    def run(self):
        for i in range(1000):
            self.counter.value += 1


# The "main" function creates a shared "counter" value with the "multiprocessing.Value" method 
# and initializes it to 0. It creates four instances of the "Process" class and starts them. 
# The main process waits for all child processes to complete by calling "join" on each process 
# in the "processes" list. Finally, it prints the final value of the "counter".
def main():
    counter = multiprocessing.Value("i", lock=True)
    counter.value = 0

    processes = [Process(counter) for i in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print("counter ", counter.value)


# The "Locked_Process" class is similar to "Process" but takes an additional "lock" parameter in 
# its constructor. The "run" method of "Locked_Process" increments a shared "locked_counter" value 
# while acquiring and releasing the lock to ensure that only one process can access the shared 
# resource at a time.
class Locked_Process(multiprocessing.Process):
    def __init__(self, locked_counter, lock):
        super(Locked_Process, self).__init__()
        self.locked_counter = locked_counter
        self.lock = lock

    
    def run(self):
        for i in range(1000):
            with self.lock:
                self.locked_counter.value += 1



def locked_main():
    locked_counter = multiprocessing.Value("i", lock=True)
    locked_counter.value = 0

    locked_processes = [Locked_Process(locked_counter, lock) for i in range(4)]
    [lp.start() for lp in locked_processes]
    [lp.join() for lp in locked_processes]
    print("locked counter ", locked_counter.value)


if __name__ == "__main__":
    # You can see that "main()" function does not always count the value to 4000 and gives wrong calculation
    main()
    
    # "Locked_main()" calculates the value accurately 
    locked_main()