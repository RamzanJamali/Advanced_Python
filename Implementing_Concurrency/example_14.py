import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor

# This code uses "asyncio" and "requests" to fetch URLs asynchronously from a list using a "ThreadPoolExecutor". 
# It defines a synchronous function called "fetch_urls" that creates a list of coroutines that run "requests.get" 
# calls for each URL in the input list.

def fetch_urls(urls):
    return asyncio.gather(
        *[loop.run_in_executor(executor, requests.get, url) for url in urls]
    )

# The main section creates an instance of "ThreadPoolExecutor" and the event loop, and schedules 
# the "fetch_urls" function to run using "loop.run_until_complete". The code prints the list of responses 
# returned by "fetch_urls".

if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()

    responses = loop.run_until_complete(
        fetch_urls(
            [
                "http://www.google.com",
                "http://www.linkedin.com",
                "http://www.facebook.com"
            ]
        )
    )

    print(responses)

# The two code examples achieve the same result of fetching URLs asynchronously using "requests" and "asyncio". 
# However, there is a difference in how the URLs are fetched.

# The first code example defines an asynchronous function called "fetch_urls" that uses a for loop to 
# iterate over the input list of URLs and schedule the "requests.get" calls using "loop.run_in_executor". 
# This approach creates and awaits one coroutine for each URL, which can lead to blocking if there are many URLs to fetch.

# In contrast, the second code example defines a synchronous function called "fetch_urls" that uses a list 
# comprehension and "asyncio.gather" to create and await a single coroutine for all the URLs in the input list. 
# This approach is more efficient as it creates and awaits a single coroutine for all URLs, which avoids 
# blocking and enables better performance.