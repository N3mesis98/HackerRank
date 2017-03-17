#!/usr/bin/python3

from math import log

def cumulated_xor(n):
    """Calcule 1 xor 2 xor 3 ... xor n"""
    if n <= 0:
        return 0
    else:
        r = 0
        # premier bit
        if (n % 4 == 1) or (n % 4 == 2):
            r = 1
        # le reste
        for i in range(1, int(log(n, 2))+1):
            powi = 2**i
            if (n % (powi * 2) >= powi) and (n % 2 == 0):
                r += powi
        return r

def cumulated_xor_step2(n):
    """Calcule n xor n-2 xor n-4 ..."""
    if n <= 0:
        return 0
    else:
        r = cumulated_xor(int(n / 2))
        r = r << 1 # shift left
        mask = (2 ** (int(log(n, 2))+1)) -1
        r = r & mask # remove the last bit
        r += ((n % 2 != 0) and ((n+1) % 4 != 0)) # add one if the number was odd one time over two
        return r

T = int(input())
for t in range(T):
    L, R = map(int, input().split(" "))    
    
    ## OK pour 1 <= L <= R <= 10**5
    #if ((R - L) + 1) % 2 == 0:
    #    print("even")
    #    r = 0
    #    for i in range(R, L, -2):
    #        r ^= i
    #    print(r)
    #else:
    #    print("odd")
    #    r = cumulated_xor(L)
    #    for i in range(L+2, R+1, 2):
    #        r ^= i
    #    print(r)

    # OK pour 1 <= L <= R <= 10**15
    if ((R - L) + 1) % 2 == 0:
        print(cumulated_xor_step2(R) ^ cumulated_xor_step2(L-1))
    else:
        print(cumulated_xor(L) ^ cumulated_xor_step2(R) ^ cumulated_xor_step2(L))
