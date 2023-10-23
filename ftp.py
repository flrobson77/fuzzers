#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.50.102",21))
data = s.recv(1024)
print(data)
s.send(b"USER admin \r\n")
data = s.recv(1024)
print(data)
s.send(b"PASS 123456 \r\n")
data = s.recv(1024)
print(data)
s.send(b"QUIT \r\n")
s.close()
