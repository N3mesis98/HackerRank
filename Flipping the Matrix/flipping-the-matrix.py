#!/usr/bin/python3

T = int(input())
for t in range(T):
    n = int(input())
    M = []
    for i in range(2*n):
        M.append(list(map(int, input().split(" "))))
        
    s = 0
    for i in range(n):
        for j in range(n):
            s += max(M[i][j], M[2*n-i-1][j], M[i][2*n-j-1], M[2*n-i-1][2*n-j-1])
    print(s)
