#!/usr/bin/python3

from math import floor, ceil

N = int(input())

if N == 0:
    print(1)
    print("0 0 0")
elif N == 1:
    print(1)
    print("1 0 0")
elif N == 2:
    print(2)
    print("1 1 0")
    print("0 0 2")
elif N == 3:
    print(3)
    print("0 1 2")
    print("2 0 1")
    print("1 2 0")
elif N == 4:
    print(3)
    print("0 1 3")
    print("3 0 1")
    print("1 3 0")
else:
    # n23
    n23 = floor(N * 2/3) + 1
    print(n23)

    # mid
    mid = [-1, -1, -1]
    mid[0] = ceil(n23 / 2)
    mid[1] = 0
    mid[2] = N - mid[0] - mid[1]
    print(" ".join(map(str, mid)))

    # top
    top = [-1, -1, -1]
    top[0] = mid[0] - 1
    top[2] = int(mid[2] % 2 == 0)
    top[1] = N - top[0] - top[2]
    print(" ".join(map(str, top)))

    while top[0] > 0:
        top[0] -= 1
        top[1] -= 1
        top[2] += 2
        print(" ".join(map(str, top)))

    # bot
    bot = [-1, -1, -1]
    bot[0] = mid[0] + 1
    bot[1] = 1
    bot[2] = N - bot[0] - bot[1]
    print(" ".join(map(str, bot)))

    while bot[0] < n23 - 1:
        bot[0] += 1
        bot[1] += 1
        bot[2] -= 2
        print(" ".join(map(str, bot)))
