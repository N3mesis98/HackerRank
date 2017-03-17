#!/usr/bin/python3

mod = 10**9 +7

def algo2(n):
    r = 0
    len1 = [0, 0, 0, 0, 0]
    len2even = 0
    len2odd = 0

    for i in range(len(n)-1, -1, -1):
        # len3
        if int(n[i]) % 2 == 0:
            r = (r + pow(2, i, mod) * (len2even % mod)) % mod
        else:
            r = (r + pow(2, i, mod) * (len2odd % mod)) % mod

        # len2
        for j in range(len(len1)):
            if len1[j] != 0:
                tmp = n[i] + str(j*2)
                if int(tmp) % 8 == 0:
                    r = (r + len1[j]) % mod
                    len2even += len1[j]
                elif (int(tmp)-4) % 8 == 0:
                    len2odd += len1[j]

        # len1
        if int(n[i]) % 2 == 0:
            len1[int(int(n[i])/2)] += 1
            if int(n[i]) % 8 == 0:
                r = (r + 1) % mod
    
    return r

input()
print(algo2(input()))
