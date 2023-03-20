import socket

TARGET_HOST = "www.google.com"
TARGET_PORT = 80

#create socket object
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((TARGET_HOST, TARGET_PORT))

#send data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print(response.decode())
client.close()