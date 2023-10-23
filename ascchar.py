#!/usr/bin/python

i=0
while i <= 127:
    if i < 16:
        print(hex(i).replace('0x','\\x0'), end='')
    else:
        print(hex(i).replace('0x','\\x'), end='')
    i += 1
