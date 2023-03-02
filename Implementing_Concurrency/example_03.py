import time
import threading


def network_request_async(number, on_done):

    def timer_done():
        time.sleep(1.0)
        on_done({"success": True,
                 "result": number ** 2
                 })
        
    timer = threading.Timer(1.0, timer_done)
    timer.start()

def on_done(result):
    print(result)


def fetch_square(number):
    def on_done(response):
        if response["success"]:
            print("Result is: {}".format(response["result"]))

    network_request_async(number, on_done)

network_request_async(2, on_done)
network_request_async(3, on_done)
network_request_async(4, on_done)
print("After Submission")