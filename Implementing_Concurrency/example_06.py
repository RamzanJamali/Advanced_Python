import time


# This code builds upon the previous code example of the "Timer" class. 
# In addition to the "done()" method, a new method "on_timer_done()" 
# is defined to specify a callback function to be called when the timer is done.
class Timer:
    def __init__(self, timeout) -> None:
        self.timeout = timeout
        self.start = time.time()


    def done(self) -> bool:
        return time.time() - self.start > self.timeout
    

    def on_timer_done(self, callback):
        self.callback = callback


if __name__ == "__main__":

    # Single callback
    # The "while" loop repeatedly checks whether the timer is done, 
    # and when it is, the callback function is called and the loop is broken.

    timer = Timer(1.0)
    timer.on_timer_done(lambda: print("Timer is done!"))

    while True:
        if timer.done():
            timer.callback()
            break


    # Multiple callbacks
    # The "while" loop repeatedly checks whether each timer in the list is done, and when a timer is done, 
    # its corresponding callback function is called and the timer is removed from the list. 
    # The loop exits when there are no more timers left in the list.

    timers = []

    timer1 = Timer(1.0)
    timer1.on_timer_done(lambda: print("First timer is done!"))

    timer2 = Timer(2.0)
    timer2.on_timer_done(lambda: print("Second timer is done!"))

    timers.append(timer1)
    timers.append(timer2)

    while True:
        for timer in timers:
            if timer.done():
                timer.callback()
                timers.remove(timer)

        # if no more timers are left we exit the loop
        if len(timers) == 0:
            break