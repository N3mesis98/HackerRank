#!/usr/bin/python3

from math import floor, log

bit_len = 32

def hamming_weight(n):
    """Nombre de 1 dans les nombres binaires entre 0 et n"""
    if n == 0:
        return 0

    elif n > 0:
        logn = floor(log(n, 2))
        hw = 0
        for i in range(logn + 1):
            powi = 2**i

            # nombre de 1 dans les cycles complets
            hw += floor((n+1) / (2*powi)) * powi

            # nombre de 1 dans le cycle courant (si il est incomplet)
            cycle_ratio = (n+1)/(2*powi) - floor((n+1)/(2*powi))
            if cycle_ratio > 0.5: # on a passé la phase avec des 0 uniquement
                cycle_ratio -= 0.5
                hw += int(cycle_ratio * (2*powi))
        return hw

    else:
        return bit_len * (-n) - hamming_weight(-n-1)

T = int(input())
for t in range(T):
    A, B = map(int, input().split(" "))
    if A == 0:
        print(hamming_weight(B))
    elif A > 0:
        print(hamming_weight(B) - hamming_weight(A-1))
    elif B == 0:
        print(hamming_weight(A))
    elif B < 0:
        print(hamming_weight(A) - hamming_weight(B+1))
    else:
        print(hamming_weight(A) + hamming_weight(B))
