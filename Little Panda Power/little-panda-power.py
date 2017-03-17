#!/usr/bin/python3

T = int(input())
for t in range(T):
    splited = input().split(" ")
    A = int(splited[0])
    B = int(splited[1])
    X = int(splited[2])
    
    if B >= 0: # simple power
        print(pow(A, B, X))
        # use built-in pow function that accept a third parameter for the modulo
        # really faster than doing (A**B) % X
    else:
        # compute the modular inverse (A^-1 mod X)
        t = 0
        r = X
        newt = 1
        newr = A
        while newr != 0:
            q = int(r / newr)
            (t, newt) = (newt, t - q * newt) 
            (r, newr) = (newr, r - q * newr)
        if r > 1:
            print("not invertible")
        if t < 0:
            t = t + X
        
        # now, power the modular inverse by |B| since A^-B mod X = (A^-1 mod X)^B
        print(pow(t, -B, X))
