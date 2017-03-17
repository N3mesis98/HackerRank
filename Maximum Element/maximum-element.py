#!/usr/bin/python3

N = int(input())
stack = []
maxstack = []
for i in range(N):
    Q = list(map(int, input().split(" ")))
    if Q[0] == 1:
        stack.append(Q[1])
        if len(maxstack) == 0 or maxstack[-1][0] < Q[1]:
            maxstack.append([Q[1], 1])
        elif maxstack[-1][0] == Q[1]:
            maxstack[-1][1] += 1
    elif Q[0] == 2:
        if stack[-1] == maxstack[-1][0]:
            if maxstack[-1][1] > 1:
                maxstack[-1][1] -= 1
            else:
                maxstack.pop()
        stack.pop()
    elif Q[0] == 3:
        print(maxstack[-1][0])
