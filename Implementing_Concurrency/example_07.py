import asyncio

# This code uses the asyncio library to schedule a callback function to be called after a delay of 1 second. 
# The "get_event_loop()" function is used to obtain the event loop for the current thread.

loop = asyncio.get_event_loop()

# The "callback()" function simply prints a message and then stops the event loop using the "stop()" method.
def callback():
    print("Hello, asyncio")
    loop.stop()

# The "call_later()" method is used to schedule the callback function to be called after 1 second. 
# The event loop is then started using the "run_forever()" method, which will block until the event loop is stopped. 
# When the callback function is called after the 1 second delay, it prints the message and stops the event loop, 
# causing the program to exit.
loop.call_later(1.0, callback)
loop.run_forever()