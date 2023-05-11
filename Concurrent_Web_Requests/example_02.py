# Ping tests are quite common among web administrators, who usually have to manage a
# large number of websites simultaneously. It is a good tool to quickly identify pages that
# are unexpectedly unresponsive or down.

import requests


def ping(url):
    res = requests.get(url)
    print(f"{url}: {res.text}")


urls = [
    "http://httpstat.us/200",
    "http://httpstat.us/400",
    "http://httpstat.us/404",
    "http://httpstat.us/408",
    "http://httpstat.us/500",
    "http://httpstat.us/511"
]

# http://httpstat.us/200: 200 OK
# http://httpstat.us/400: 400 Bad Request
# http://httpstat.us/404: 404 Not Found
# http://httpstat.us/408: 408 Request Timeout
# http://httpstat.us/500: 500 Internal Server Error
# http://httpstat.us/511: 511 Network Authentication Required

for url in urls:
    ping(url)

print("Done. ")