import time
import threading

def wait_and_print(msg):
    time.sleep(1.0)
    print(msg)

def wait_and_print_async(msg):
    def callback():
        print(msg)

    timer = threading.Timer(1.0, callback)
    timer.start()


# Synchronous
wait_and_print("first call")
wait_and_print("second call")
print("after all")

# Asynchronous
wait_and_print_async("First call async")
wait_and_print_async("second call async")
print("after submission")