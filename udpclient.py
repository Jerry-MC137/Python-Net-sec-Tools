import socket

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 9997

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Send data
client.sendto(b"AAABBBCCC", (TARGET_HOST, TARGET_PORT))

# Reveive data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
