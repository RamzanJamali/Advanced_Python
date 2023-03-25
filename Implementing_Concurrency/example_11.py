import asyncio

# The code defines two asynchronous functions - "network_request" and "fetch_square".

async def network_request(number):
    await asyncio.sleep(1.0)
    return {"success" : True, "result": number ** 2}


async def fetch_square(number):
    response = await network_request(number)
    if response["success"]:
        print("Number is: {}".format(response["result"]))

# The main section of the code demonstrates how to run the "fetch_square" function for input numbers sequentially or 
# concurrently using "loop.run_until_complete" and "asyncio.ensure_future", respectively. 
# The program waits for 1 second for each network request and prints the calculated square of the input numbers 
# to the console.

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # First example
    loop.run_until_complete(fetch_square(2))
    loop.run_until_complete(fetch_square(3))
    loop.run_until_complete(fetch_square(4))

    # Second example
    asyncio.ensure_future(fetch_square(5))
    asyncio.ensure_future(fetch_square(6))
    asyncio.ensure_future(fetch_square(7))
    # Hit Ctrl + C to stop the loop
    loop.run_forever()