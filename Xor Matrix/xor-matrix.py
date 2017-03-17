#!/usr/bin/python3

from math import log, pow

(n, m) = map(int, input().split(" "))
frow = list(map(int, input().split(" ")))

while m > 1:
    jump = int(pow(2, int(log(m,2))))
    modjump = jump % (n*2)

    if modjump <= n:
        xorrange = [0, modjump]
    else:
        xorrange = [modjump-n, n]

    xored = 0
    for i in range(xorrange[0], xorrange[1]):
        xored = xored ^ frow[i]

    jumprow = [xored]
    for i in range(1, n):
        xored = jumprow[i-1]
        xored = xored ^ frow[(xorrange[0] + i-1)%n]
        xored = xored ^ frow[(xorrange[1] + i-1)%n]
        jumprow.append(xored)

    m = m - jump + 1
    frow = jumprow


print(" ".join(map(str, frow)))
