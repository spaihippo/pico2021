#!/usr/bin/python3

f = open("enc", "r")
str = f.read()
res = ""
for i in range(len(str)):
    first_ord = ord(str[i]) >> 8
    res += chr(first_ord)
    sec_ord = ord(str[i]) - (first_ord << 8)
    res += chr(sec_ord)
print(res)
f.close()