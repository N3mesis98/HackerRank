#!/usr/bin/python3

from math import log, floor

l = int(input())
r = int(input())

if (l == r):
    print(0)
else:
    logr = log(r, 2)
    if (logr.is_integer()):
        print(r ^ (r-1))
    else:
        logn = floor(logr)
        n = 2**logn
        if (n > l): # n and n-1 must be in [l,r]
            print(n ^ n-1)
        else:
            logn -= 1
            while (logn > 0):
                if (n + 2**logn > r):
                    pass # to big, n does not change
                else:
                    n += 2**logn
                    if (n > l):
                        break; # n and n-1 in [l,r] -> stop
                    
                logn -= 1
            print(n ^ n-1)
