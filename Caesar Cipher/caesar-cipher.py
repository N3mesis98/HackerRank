#!/usr/bin/python3

input()
S = input()
K = int(input())

encrypted = ""
for c in S:
    mini = None
    maxi = None
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        mini = ord("a")
        maxi = ord("z")
    elif ord(c) >= ord("A") and ord(c) <= ord("Z"):
        mini = ord("A")
        maxi = ord("Z")
    
    if mini == None or maxi == None:
        encrypted += c
    else:
        encrypted += chr((ord(c)-mini+K)%(maxi-mini+1) + mini)
        
print(encrypted)
