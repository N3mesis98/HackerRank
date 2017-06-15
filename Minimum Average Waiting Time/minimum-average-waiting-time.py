#!/usr/bin/python3

from heapq import *

N = int(input())

commands = []
for i in range(N):
    t, l = map(int, input().split(" "))
    commands.append((t, l))
commands = sorted(commands)

totreat = []
time = 0
idx = 0
waittime = 0
while idx < len(commands):
    if (len(totreat) == 0) and (time < commands[idx][0]):
        time = commands[idx][0]
    
    print("Time: {}".format(time))
    
    i = 0
    while (idx+i < len(commands)) and (time >= commands[idx+i][0]):
        t, l = commands[idx+i]
        print("Client ({}, {}) arrived".format(t, l))
        heappush(totreat, (l, t))
        i += 1
    idx += i
        
    l, t = heappop(totreat)
    print("Client ({}, {}) treated".format(t, l))
    time += l
    waittime += (time - t)
    print()
    
while len(totreat) > 0:
    l, t = heappop(totreat)
    print("Client ({}, {}) treated".format(t, l))
    time += l
    waittime += (time - t)
    
print(int(waittime / len(commands)))
