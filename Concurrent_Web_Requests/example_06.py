# Handling Timeouts
import threading
import requests
import time

# The constant 'UPDATE_INTERVAL' is set to 0.01, representing the interval at which the main 
# thread checks for the completion of child threads.
UPDATE_INTERVAL = 0.01

# This code defines a custom thread class 'MyThread' that inherits from 'threading.Thread'. 
# Each thread instance is initialized with a URL and a 'result' variable. The 'run' method 
# is overridden to make an HTTP GET request to the given URL and store the 
# response in the 'result' variable.
class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.result = None 

    def run(self):
        res = requests.get(self.url)
        self.result = f"{self.url}: {res.text}"

# A function 'process_requests' is defined that takes a list of threads and an optional 'timeout' value 
# as parameters. The inner function 'alive_count' calculates the number of alive threads. The main loop 
# continuously checks the number of alive threads and the remaining timeout until either all threads 
# have completed or the timeout has elapsed. The function then prints the 'result' variable of each thread.
def process_requests(threads, timeout=5):
    def alive_count():
        alive = [1 if thread.is_alive() else 0 for thread in threads]
        return sum(alive)
    
    while alive_count() > 0 and timeout > 0:
        timeout -= UPDATE_INTERVAL
        time.sleep(UPDATE_INTERVAL)
    for thread in threads:
        print(thread.result)

# A list of URLs is defined, representing different HTTP endpoints. Some URLs include additional 
# parameters to simulate longer response times.
urls = [
    "http://httpstat.us/200",
    "http://httpstat.us/200?sleep=4000",
    "http://httpstat.us/200?sleep=20000",
    "http://httpstat.us/400",
]

# The current time is recorded to measure the overall execution time.
start = time.time()

# The list of MyThread instances is created using a list comprehension.
threads = [MyThread(url) for url in urls]
# The 'setDaemon(True)' method is called on each thread to set them as daemon threads, 
# which allows the program to exit even if they haven't finished.
for thread in threads:
    thread.setDaemon(True)
    thread.start()
# The threads are then started, and the 'process_requests' function is called to wait for the 
# threads to complete and print their results.
process_requests(threads)

# The total execution time is calculated and printed.
print(f"Took {time.time() - start : .2f} seconds")

print("Done. ")
# Resuming programming