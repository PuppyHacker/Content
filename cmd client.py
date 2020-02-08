#client
import os
import socket

socketvar = socket.socket()

socketvar.connect(("127.0.0.1", 4442))

msg = raw_input("enter the commend")
while msg != "exit":
    socketvar.send(msg)
    mes2 = socketvar.recv(2048)
    print mes2
    msg = raw_input("enter the commend")
    socketvar.send(msg)





socketvar.close()
raw_input()
