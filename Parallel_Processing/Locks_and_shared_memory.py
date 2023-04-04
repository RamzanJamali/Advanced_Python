import multiprocessing

lock = multiprocessing.Lock()


class Process(multiprocessing.Process):
    def __init__(self, counter):
        super(Process, self).__init__()
        self.counter = counter

    
    def run(self):
        for i in range(1000):
            self.counter.value += 1

def main():
    counter = multiprocessing.Value("i", lock=True)
    counter.value = 0

    processes = [Process(counter) for i in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print("counter ", counter.value)



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
    main()
    locked_main()