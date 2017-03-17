#!/usr/bin/python3

def walk(M, pos, end, wand=0):
    if pos == end:
        return wand
    possibilities = []
    if pos[0] > 0 and M[pos[0]-1][pos[1]] != "X":
        possibilities.append([pos[0]-1, pos[1]])
    if pos[0] < len(M)-1 and M[pos[0]+1][pos[1]] != "X":
        possibilities.append([pos[0]+1, pos[1]])
    if pos[1] > 0 and M[pos[0]][pos[1]-1] != "X":
        possibilities.append([pos[0], pos[1]-1])
    if pos[1] < len(M[0])-1 and M[pos[0]][pos[1]+1] != "X":
        possibilities.append([pos[0], pos[1]+1])
    
    if len(possibilities) == 0:
        return None
    elif len(possibilities) > 1:
        wand += 1
    
    M[pos[0]][pos[1]] = "X"
    for possibility in possibilities:
        newwand = walk(M, possibility, end, wand)
        if newwand != None:
            return newwand
    return None

T = int(input())
for t in range(T):
    (m, n) = map(int, input().split(" "))
    M = []
    pos = None
    end = None
    for i in range(m):
        row = list(input())
        for j in range(len(row)):
            if row[j] == "M":
                pos = [i, j]
            if row[j] == "*":
                end = [i, j]
        M.append(row)
    K = int(input())
    wand = walk(M, pos, end)
    if K == wand:
        print("Impressed")
    else:
        print("Oops!")
