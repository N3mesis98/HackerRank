#!/usr/bin/python3

import math

nedge = lambda n,r:(pow(n,2) - n%r * pow(math.ceil(n/r),2) - (r - n%r) * pow(math.floor(n/r),2))/2
l = int(input())
for i in range(l):
    tmp = input().split(" ")
    n = int(tmp[0])
    m = int(tmp[1])
    r = math.ceil(1/(1-(2*m)/pow(n, 2)))
    
    while nedge(n,r) < m:
        r += 1
        
    while nedge(n,r-1) >= m:
        r -= 1
        
    print(r)
