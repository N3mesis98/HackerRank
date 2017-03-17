#!/usr/bin/python3

N = int(input())
delay = list(map(int, input().split(" ")))
limit = [[] for i in range(N)]
unfinished = [0 for i in range(N)]

curunfinished = [False for i in range(N)]
sumcurunfinished = 0

for i in range(N):
    if delay[i] >= 1:
        limit[(i-delay[i]) % N].append(i)

i = 0
while (i < N) or (sumcurunfinished != 0):
    unfinished[i % N] += sumcurunfinished
    if curunfinished[i % N]:
        curunfinished[i % N] = False
        sumcurunfinished -= 1
    for j in limit[i % N]:
        curunfinished[j] = True
        sumcurunfinished += 1
    limit[i % N] = []
    i += 1
    
mini = unfinished[0]
miniindex = 0
for i in range(1, N):
    if mini > unfinished[i]:
        mini = unfinished[i]
        miniindex = i
        
print(miniindex+1)
