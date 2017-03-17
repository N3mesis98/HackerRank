#!/usr/bin/python3

N, K = map(int, input().split(" "))
C = sorted(map(int, input().split(" ")), reverse=True)

sumC = 0
for i in range(int(N/K)+1):
    sumC += sum(C[K*i : min(K*(i+1), N)]) * (i+1)
    
print(sumC)
