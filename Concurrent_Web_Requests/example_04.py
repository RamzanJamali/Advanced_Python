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


urls = [
    "http://httpstat.us/200",
    "http://httpstat.us/400",
    "http://httpstat.us/404",
    "http://httpstat.us/408",
    "http://httpstat.us/500",
    "http://httpstat.us/524",
]

start = time.time()

threads = [MyThread(url) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
for thread in threads:
    print(thread.result)

print(f"Took {time.time() - start : .2f} seconds")

print("Done. ")