import os
import string

with open(r"D:\PP2\labs\lab6\dif-and-files\sometext.txt", "r", encoding="utf-8") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()