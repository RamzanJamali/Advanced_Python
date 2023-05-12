# To apply concurrency, we can simply use the threading module that we have been
# discussing to create separate threads to handle different web requests.

import threading
import requests
import time


def ping(url):
    res = requests.get(url)
    print(f"{url}: {res.text} \n")


urls = [
    "http://httpstat.us/200",
    "http://httpstat.us/400",
    "http://httpstat.us/404",
    "http://httpstat.us/408",
    "http://httpstat.us/500",
    "http://httpstat.us/524",
]

# we are including the sequential logic from the previous example to
# process our URL list so that we can compare the speed improvement when we apply
# threading to our ping test program.

start = time.time()
for url in urls:
    ping(url)

print(f"Sequential: {time.time() - start : .2f} seconds")

print()

# We are also creating a thread to ping each of the
# URLs in our URL list using the threading module; these threads will be executed
# independently from each other.

start = time.time()
threads = []
for url in urls:
    thread = threading.Thread(target=ping, args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()


print(f"Threading: {time.time() - start : .2f} seconds")