#!/usr/bin/python3

from math import log

T = int(input())
for t in range(T):
    A, B = map(int, input().split(" "))
    if A == B:
        print(A)
    else:
        R = 0
        for i in range(int(log(B, 2)) + 1):
            powi = 2**i
            if (B-A <= powi) and (A & powi != 0) and (B & powi != 0):
                R += powi
        print(R)
