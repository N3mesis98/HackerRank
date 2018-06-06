#!/usr/bin/python3

MAX=10**7

def sign(i):
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return 0

def itor(i):
    r = (i % 3) # from [1,8] to [0,2]
    r = (-1 if r==2 else r)
    return r

def itoc(i):
    c = (i // 3) # from [1,8] to [0,2]
    c = (-1 if c==2 else c)
    return c

def rctoi(r, c):
    i = 3*(2 if c==-1 else c) + (2 if r==-1 else r)
    return i

if __name__ == "__main__":
    N, K = map(int, input().split(" "))
    R, C = map(int, input().split(" "))
    scores = []

    # first iteration to init score for each direction without obstacles
    for i in range(1, 9):
        r = itor(i)
        c = itoc(i)
        
        rscore = MAX
        if r != 0:
            rscore = N*(r>0) - r*R - (r<0)
        cscore = MAX
        if c != 0:
            cscore = N*(c>0) - c*C - (c<0)
        scores.append(min(rscore, cscore))
        
    # second loop, reduce each score from the obstacles
    for k in range(K):
        kr, kc = map(int, input().split(" "))
        rkr = kr - R
        rkc = kc - C
        iscore = rctoi(sign(rkr), sign(rkc)) - 1
        
        if rkr == 0:
            scores[iscore] = min(scores[iscore], abs(rkc)-1)
        elif rkc == 0:
            scores[iscore] = min(scores[iscore], abs(rkr)-1)
        elif abs(rkr) == abs(rkc):
            scores[iscore] = min(scores[iscore], abs(rkc)-1)
        
    print(sum(scores))
