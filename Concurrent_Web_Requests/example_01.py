 # This line of code imports the requests library, which is used to send HTTP requests using Python.
import requests

# This line sets the URL variable to the URL of the website that we want to request data from.
url = 'http://www.google.com'

# This line sends a GET request to the specified URL using the requests library and 
# stores the response in the 'res' variable.
res = requests.get(url)

# This line prints the HTTP status code of the response, which can be used to determine if 
# the request was successful (status code 200) or if there was an error.
print(res.status_code)

# This line prints the headers of the response, which contain metadata about the response 
# such as the content type and encoding.
print(res.headers)

# This part opens a new file called 'google.html' in write mode using the 'with' statement, which 
# ensures that the file is properly closed when the block is exited. It  writes the text content 
# of the response to the 'google.html' file using the 'write' method of the file object.
with open('google.html', 'w') as f:
    f.write(res.text)

# This line prints 'Done.' to indicate that the script has finished executing.
print('Done.')