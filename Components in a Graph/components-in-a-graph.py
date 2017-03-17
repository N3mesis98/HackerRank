#!/usr/bin/python3

def find(sets, x):
    if sets[x][0] != x:
        sets[x][0] = find(sets, sets[x][0])
    return sets[x][0]

def union(sets, x, y):
    xRoot = find(sets, x)
    yRoot = find(sets, y)
    
    if xRoot == yRoot:
        return
    
    if sets[xRoot][1] < sets[yRoot][1]:
        sets[xRoot][0] = sets[yRoot][0]
        sets[yRoot][2] += sets[xRoot][2]
    elif sets[xRoot][1] > sets[yRoot][1]:
        sets[yRoot][0] = sets[xRoot][0]
        sets[xRoot][2] += sets[yRoot][2]
    else:
        sets[yRoot][0] = sets[xRoot][0]
        sets[xRoot][1] += 1
        sets[xRoot][2] += sets[yRoot][2]

N = int(input())
sets = [[i, 0, 1] for i in range(2*N)] # [parent, rank, n]
for i in range(N):
    G, B = map(int, input().split(" "))
    union(sets, G-1, B-1)
    
mini = maxi = None
for i in range(len(sets)):
    curSize = sets[find(sets, i)][2]
    if curSize > 1:
        if (mini == None) or (mini > curSize):
            mini = curSize
        if (maxi == None) or (maxi < curSize):
            maxi = curSize
            
print(mini, maxi)
