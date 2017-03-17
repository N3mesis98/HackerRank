#!/usr/bin/python3

from math import log

T = int(input())
for t in range(T):
    n = int(input())
    mask = (2**(int(log(n, 2))+1)) - 1
    print(~n & mask)
