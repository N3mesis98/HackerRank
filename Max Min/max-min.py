#!/usr/bin/python3

N = int(input())
K = int(input())
A = []
for i in range(N):
    A.append(int(input()))
A.sort()
minf = None
for i in range(N-K+1):
    f = A[i+K-1]-A[i]
    if minf == None or f < minf:
        minf = f
print(minf)
