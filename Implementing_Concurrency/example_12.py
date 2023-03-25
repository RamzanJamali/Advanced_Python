# This Python code demonstrates how to use the "ThreadPoolExecutor" class to run functions in a separate thread pool
# and "asyncio" to integrate blocking I/O functions with asynchronous code.

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


executor = ThreadPoolExecutor(max_workers=3)


def wait_and_return(msg):
    time.sleep(1.0)
    return msg


# In the first example, the "wait_and_return function" is submitted to the "executor" thread pool using "executor.submit" 
# with the message "Hello, executor". The function is executed in a separate thread and returns a "Future" object 
# that represents the result of the function.

# First Example
print(executor.submit(wait_and_return, "Hello, executor"))

# In the second example, the event loop is created using "asyncio.get_event_loop()". 
# The "wait_and_return" function is scheduled to run in the thread pool using "loop.run_in_executor" with 
# the "executor" and the message "hello, asyncio executor". The function is executed in a separate thread, 
# and the event loop waits for the result using "loop.run_until_complete". The "run_in_executor" function 
# returns a "Future" object that represents the result of the function.

# Second Example
loop = asyncio.get_event_loop()
fut = loop.run_in_executor(executor, wait_and_return, "hello, asyncio executor")
print(fut)
print(loop.run_until_complete(fut))