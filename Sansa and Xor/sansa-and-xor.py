#!/usr/bin/python3

T = int(input())
for t in range(T):
    input() # number of element
    N = list(map(int, input().split(" ")))
    
    if len(N) % 2 == 0:
        print(0)
    else:
        r = N[0]
        for i in range(2, len(N), 2):
            r ^= N[i]

        print(r)
