#!/usr/bin/python3

T = int(input())
for t in range(T):
    S = input()
    a = 0
    b = 0
    c = 0
    for s in S:
        if s == "a":
            a+=1
        elif s == "b":
            b+=1
        elif s == "c":
            c+=1
    if a == len(S) or b == len(S) or c == len(S):
        print(len(S))
    elif a%2 == b%2 and a%2 == c%2:
        print(2)
    else:
        print(1)
