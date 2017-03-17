#!/usr/bin/python3

from math import ceil

T = int(input())
for t in range(T):
    n = int(input())
    n4 = ceil(n / 4)
    diff = 4*n4 - n
    if n4 >= diff * 2:
        print("Yes")
    else:
        print("No")
