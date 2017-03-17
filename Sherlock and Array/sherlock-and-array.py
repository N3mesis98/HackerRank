#!/usr/bin/python3

T = int(input())
for t in range(T):
    input()
    A = list(map(int, input().split(" ")))
    cumul = []
    for i in A:
        if len(cumul) == 0:
            cumul.append(i)
        else:
            cumul.append(cumul[-1]+i)
            
    for i in range(len(A)):
        if cumul[i]-A[i] == cumul[-1]-cumul[i]:
            print("YES")
            break
    else:
        print("NO")
