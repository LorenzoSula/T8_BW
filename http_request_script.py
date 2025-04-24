import http.client

# Get the host/IP of the target system from the user
host = input("Enter host/IP of target system: ")

# Get the port of the target system from the user, defaulting to 80 if no input is provided
port = input("Enter the port of target system (default: 80): ")
if port == '':
    port = 80
else:
    port = int(port)

# Get the path to be tested from the user, defaulting to "/phpMyAdmin/" if no input is provided
path = input("Enter the path to test (default: /phpMyAdmin/): ")
if path == '':
    path = "/phpMyAdmin/"

# List of HTTP methods to test
http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'TRACE', 'CONNECT']

print(f"\nTesting HTTP methods on {host}:{port}{path}\n")

# Loop through each HTTP method and test it
for method in http_methods:
    try:
        # Create a connection to the target host and port
        conn = http.client.HTTPConnection(host, port, timeout=5)
        
        # Send an HTTP request using the current method
        conn.request(method, path)
        
        # Get the response from the server
        response = conn.getresponse()
        
        # Print the HTTP status and reason
        print(f"{method:8} → {response.status} {response.reason}")
        
        # Close the connection
        conn.close()
    except Exception as e:
        # Print an error message if an exception occurs
        print(f"{method:8} → Error: {e}")
