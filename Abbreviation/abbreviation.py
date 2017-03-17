#!/usr/bin/python3

import re

T = int(input())
for t in range(T):
    A = input()
    B = input() # target
    
    s = "^[a-z]*"
    for b in B:
        s += "["+b+b.lower()+"][a-z]*"
    s += "$"
    
    if re.match(s, A):
        print("YES")
    else:
        print("NO")
