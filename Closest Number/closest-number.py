#!/usr/bin/python3

from math import floor, ceil

T = int(input())
for t in range(T):
    a, b, x = map(int, input().split(" "))
    #multax = a / x
    multax = a**b / x
    if multax - floor(multax) > 0.5:
        multax = ceil(multax)
    else:
        multax = floor(multax)
        
    print(multax * x)
