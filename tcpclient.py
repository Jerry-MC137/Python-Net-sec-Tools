import socket
target_host = "www.google.com"
target_port = 80

# create a socket object
# AF_INET param for setting standard IPv4 address
# SOCK_STREAM for indicating that this is a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive data
response = client.recv(4096)

print(response.decode())
client.close()


 #Some assumptions that have gone into the above code snippet include:
 # 1. Our connection will always be successful
 # 2. The server is always expecting us to send data first
 # 3. The server will always send us data back in a timely function.
 