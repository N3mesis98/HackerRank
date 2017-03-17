#!/usr/bin/python3

T = int(input())
for t in range(T):
    X = int(input())
    # somme des n premiers carrés : n(n + 1)(2n + 1) / 6 = (2n^3 + 3n^2 + n) / 6
    # https://www.les-suites.fr/somme-des-n-premiers-carres.htm
    
    # approximation en négligeant les degrés inférieurs dans le polynome
    # n <= (3X)^1/3
    n = int((3*X)**(1/3))
    while X < (2*n**3 + 3*n**2 + n)/6:
        n -= 1
    print(n)
