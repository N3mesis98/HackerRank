#!/usr/bin/python3

mod = int(7+1e9)

T = int(input())
for t in range(T):
    M, N = map(int, input().split(" "))
    Cy = sorted(map(int, input().split(" ")))
    Cx = sorted(map(int, input().split(" ")))
    
    C = 0
    while len(Cx)>0 and len(Cy)>0:
        if Cx[-1] > Cy[-1]:
            C = (C+Cx.pop()*(M-len(Cy)))%mod
        else:
            C = (C+Cy.pop()*(N-len(Cx)))%mod

    C = (C+sum(Cx)*M)%mod
    C = (C+sum(Cy)*N)%mod
    
    print(C)
