#!/usr/bin/python

i=0
while i <= 127:
    if i < 16:
        print hex(i).replace('0x','\\x0'),
    else:
        print hex(i).replace('0x','\\x'),
    i += 1
