# Handling Timeouts
import threading
import requests
import time

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

# Specifically, we can customize the delay time (in milliseconds) with a query argument in our GET
# request. For example, httpstat.us/200?sleep=20000 will return a response after
# a 20-second delay.
urls = [
    "http://httpstat.us/200",
    "http://httpstat.us/200?sleep=20000",
    "http://httpstat.us/400",
]

# The current time is recorded to measure the overall execution time.
start = time.time()

# A list comprehension is used to create multiple 'MyThread' instances, one for each URL in the 'urls' list.
threads = [MyThread(url) for url in urls]
for thread in threads:
    thread.start()
# The main thread waits for all the child threads to complete execution by 
# calling the 'join' method on each thread.
for thread in threads:
    thread.join()
for thread in threads:
    print(thread.result)

# The total execution time is calculated by subtracting the start time 
# from the current time, and it is printed with two decimal places.
print(f"Took {time.time() - start : .2f} seconds")

print("Done. ")