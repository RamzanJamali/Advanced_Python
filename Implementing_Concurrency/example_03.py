# This example implements complex callback function that returns nothing.
import time
import threading

# The on_done will replace the return of function, the result is stored using on_done function.
def network_request_async(number, on_done):

    def timer_done():
        on_done({"success": True,
                 "result": number ** 2
                 })
        
    timer = threading.Timer(1.0, timer_done)
    timer.start()

# To directly print return results
def on_done(result):
    print(result)

# To use network_request_async in fetch_square like in example 2, we need on_done callback function.
def fetch_square(number):
    def on_done(response):
        if response["success"]:
            print("Result is: {} ".format(response["result"]))

    network_request_async(number, on_done)


# Checking results
network_request_async(2, on_done)
network_request_async(3, on_done)
network_request_async(4, on_done)
print("After Submission")

fetch_square(2)
fetch_square(3)