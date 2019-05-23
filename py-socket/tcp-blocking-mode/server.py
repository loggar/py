import socket

s = socket.socket()

host = socket.gethostname()
port = 31010

s.bind((host, port))
s.listen(5)

print("Listen %s:%d" % (host, port))

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    while data:
        print(data)
        data = conn.recv(1024)
    print("Data Received")
    conn.close()
    break
