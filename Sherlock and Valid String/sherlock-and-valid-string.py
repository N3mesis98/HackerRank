#!/usr/bin/python3

def ordindex(c):
    return ord(c)-ord("a")

S = input()
C = [0 for i in range(26)]
for c in S:
    C[ordindex(c)] += 1
C = list(filter(lambda x:x!=0, sorted(C)))
if (C[0] == C[-1]) or (C[1] == C[-1] and (C[0]+1 == C[1] or C[0]==1)) or (C[0] == C[-2] and C[-2]+1 == C[-1]):
    print("YES")
else:
    print("NO")
