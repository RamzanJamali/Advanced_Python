# Import time library to make program that delays responses similar to web requests.
import time

# Network request function will behave like a function request made to a website.
def network_request(number):
    time.sleep(1.0)
    return {"success": True, "result": number ** 2}

# Just like the response from a website
def fetch_square(number):
    response = network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))

# This behaves like a synchronous request(second request will start after finishing the first request)
fetch_square(2)
fetch_square(3)
fetch_square(4)