# Futures pattern added to keep the track of the results of asynchronous calls.
from concurrent.futures import Future
import threading

# we accept the callbacks and pass the results when they are ready
def network_request_async(number):
    future = Future()
    result = {
        "success": True,
        "result": number ** 2
    }
    timer = threading.Timer(1.0, lambda: future.set_result(result))
    timer.start()
    return future

# To attach a callback it is sufficient to pass a function to fut.add_done_callback method
def fetch_square(number):
    fut = network_request_async(number)

    def on_done_future(future):
        response = future.result()
        if response["success"]:
            print("Result is: {}".format(response["result"]))

    fut.add_done_callback(on_done_future)

print("start")
fetch_square(2)
print("end")