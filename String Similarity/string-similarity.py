#!/usr/bin/python3

T = int(input())
for t in range(T):
    # use Z algorithm :
    #   - https://www.youtube.com/watch?v=CpZh4eF8QBw
    #   - http://codeforces.com/blog/entry/3107
    S = input()
    Z = [len(S)]
    L = 0 # left bound of the Z box
    R = 0 # right bound of the Z box
    for i in range(1, len(S)):
        if i > R:
            L = i
            R = i
            while (R < len(S)) and (S[R] == S[R-i]): # match while possible, beginning from L
                R += 1
            Z.append(R - L)
            R -= 1
        else:
            j = i-L # equivalent position beginning from 0
            if Z[j] < R-i+1:
                Z.append(Z[j])
            else:
                L = i
                while (R < len(S)) and (S[R] == S[R-i]):
                    R += 1
                Z.append(R - L)
                R -= 1
    print(sum(Z))
