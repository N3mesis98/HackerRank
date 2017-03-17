#!/usr/bin/python3

from bisect import bisect_left, bisect_right

N, M = map(int, input().split(" "))
A = []
B = []
for i in range(N):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)
A.sort()
B.sort()

r = 0
for i in range(M):
    c, d = map(int, input().split(" "))
    before = bisect_left(B, c) # nombre d'intervals terminant avant le debut du courant
    after = N - bisect_right(A, d) # nombre d'intervals commencant après la fin du courant
    r += N - before - after
print(r)
