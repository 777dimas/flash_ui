from io import StringIO
import sys

s = bytearray.fromhex("468530ed15d125708f")

s1 = list(s)

for i in s1:
    d = chr(i)
    a = str(print(d,end=''))


