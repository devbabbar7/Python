import requests

# Opens a conneciion (via urllib3), sends HTTP request, receives HTTP response, and closes the connection.
#response = requests.get("https://www.geeksforgeeks.org/")
# response = requests.get("https://www.google.com/")
# response = requests.get("https://www.york.ac.uk/teaching/cws/wws/webpage1.html")

# Timeout is the maximum amount of time (in seconds) that the request will wait for a response from the server before giving up and raising a Timeout exception.
response = requests.get("https://www.hdfcbank.com/", timeout = 5)

# In Sessions, connection, cookies and headers persists, we can have login sessions, performance improvement etc. 
# We use sessions when calling an API repeatedly, maintain login state, making many requests to the same host, and when we want to persist certain parameters across requests. Also in web scraping.
# session = requests.Session()
# response = session.get("https://www.hdfcbank.com/", timeout = 5)

# SSL Certificate Verification
# SSL certificate verification is a security feature that ensures that the server you are connecting to is the one it claims to be. 
# It does this by verifying the server's SSL certificate against a trusted certificate authority (CA).
# response = requests.get("https://www.geeksforgeeks.org/", verify='path/to/certfile')

# This will disable SSL certificate verification, which can be useful for testing purposes but is not recommended for production use.
# response = requests.get("https://www.geeksforgeeks.org/", verify=False) 

# Authentication
# Authentication is the process of verifying the identity of a user or client before allowing access to a resource.
# from requests.auth import HTTPBasicAuth
# response = requests.get("https://www.geeksforgeeks.org/", auth=HTTPBasicAuth('username', 'password'))

# Post Request
# A POST request is a type of HTTP request that is used to send data to a server to create or update a resource.
# payload = {'username': 'test', 'password': 'test123'}
# response = requests.post("https://httpbin.org/post", data=payload)
# print(response.text)

# 200 means the request was successful
print(response.status_code) # 200

# This will print the reason phrase associated with the status code. 
# For example, if the status code is 200, the reason phrase will be "OK".
print(response.reason) # OK

# It checks if the request was successful (status code 200-399) or if there was an error (status code 400 and above).
print(response.ok) # True

# This will print the time taken to get the response
# print(response.elapsed) # 0:00:00.123456

# This will print the HTML content of the page
# print(response.text)  # This will print the HTML content of the page as a string
# print(response.content) # This will print the raw bytes of the response content

# This will print the headers of the response as a dictionary
# print(response.headers)

# This will print the cookies set by the server
#print(response.cookies) 

# This will print the encoding of the response
# print(response.encoding) # utf-8

# This will print the URL of the response
# print(response.url) # https://www.geeksforgeeks.org/

# This will print whether the response is a permanent redirect or not
# A permanent redirect means that the resource has been moved to a new URL permanently, and the client should update its bookmarks or links to the new URL.
print(response.is_permanent_redirect)

# This will print whether the response is a redirect or not
# A redirect means that the resource has been moved to a new URL temporarily, and the client should continue to use the original URL for future requests.
print(response.is_redirect)

# This will print the links found in the HTML response content
# Returned as a dictionary where the keys are the link relation types (e.g., "next", "prev", "first", "last") and the values are the corresponding URLs.
print(response.links)

# This will close the connection to the server
# Closing the connection is important to free up resources on both the client and server side.
# This is not required when we use get() or post() methods, as they automatically close the connection after the request is completed. However, if we are using a session or making multiple requests to the same server, it is a good practice to close the connection when we are done.
response.close()
