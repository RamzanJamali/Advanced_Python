import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor

# This code uses "asyncio" and "requests" to fetch URLs asynchronously from a list. 
# It defines an asynchronous function called "fetch_urls" that loops through each URL, 
# scheduling a "requests.get" call in the "ThreadPoolExecutor".

async def fetch_urls(urls):
    responses = []
    for url in urls:
        responses.append(await loop.run_in_executor(executor, requests.get, url))

    return responses

# The "main" section creates an instance of the "ThreadPoolExecutor" and the event loop, and 
# schedules the "fetch_urls" function to run using "loop.run_until_complete". The code prints 
# the list of responses returned by "fetch_urls".

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