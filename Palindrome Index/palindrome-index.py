#!/usr/bin/python3

def palindrom(s, i=0, j=-1, k=-1):
    while i < j+len(s):
        if s[i] != s[j]:
            break
        i+=1
        j-=1
    else:
        return k # finished
    if k == -1:
        r = palindrom(s, i+1, j, i) # remove i
        if r != None:
            return r
        else:
            return palindrom(s, i, j-1, j+len(s)) # remove j
    else:
        return None # no solution on this branch    
    
    
T = int(input())
for t in range(T):
    s = input()
    print(palindrom(s)) # there is always at least a solution -> can't be None at this point
