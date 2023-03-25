import time

# This code defines a 'Timer' class that takes a timeout value as input when it is initialized. 

class Timer:
    def __init__(self, timeout) -> None:
        self.timeout = timeout
        self.start = time.time()

    # The "done()" method of this class checks whether the time elapsed since the timer started is greater than the specified timeout. If it is, the "done()" method returns "True".
    def done(self) -> bool:
        return time.time() - self.start > self.timeout
    

if __name__ == "__main__":
    timer = Timer(1.0)
# The 'while True:' loop is used to repeatedly check whether the timer is done.
    while True:
        if timer.done():
            print("Timer is done!")
            break