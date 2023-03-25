import asyncio

# The function is marked as "async" which means it can use "await" to suspend its execution while waiting for 
# an operation to complete. In this case, the function calls "asyncio.sleep(1.0)" to wait for 1 second, 
# and then prints the message "msg" to the console.

async def wait_and_print(msg):
    await asyncio.sleep(1.0)
    print("message: ", msg)

# creates an instance of the event loop using "asyncio.get_event_loop()". 
# It then runs the "wait_and_print" function using 'loop.run_until_complete(wait_and_print("Hello"))', 
# which schedules the coroutine to run on the event loop until it completes.

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_and_print("Hello"))