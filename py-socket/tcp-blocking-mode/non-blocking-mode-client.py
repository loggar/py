import socket

sock = socket.socket()
host = socket.gethostname()

sock.connect((host, 31010))
sock.setblocking(0) # Now setting to non-blocking mode

data = b"Foo Bar" * 10*1024  # Send a lot of data to be sent
assert sock.send(data)  # Send data till true

print("Data sent")
