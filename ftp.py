#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.16.70",21))
data = s.recv(1024)
print data
s.send("USER admin \r\n")
data = s.recv(1024)
print data
s.send("PASS 123456 \r\n")
data = s.recv(1024)
print data
s.send("QUIT \r\n")
s.close()
