#!/usr/bin/python3

import bisect

class Node:
    def __init__(self, n):
        self.n = n
        self.next = []
        self.prev = []
        self.nactivation = 0
    def arc(self, dest):
        self.next.append(dest)
        dest.prev.append(self)
    def __str__(self):
        return str(self.n)
    def __repr__(self):
        return str(self.n)
    def __lt__(self, other):
        # reverse order for bisect
        return self.n > other.n

if __name__ == "__main__":
    # build graph
    N = int(input())
    nodesdict = {}
    for i in range(N):
        input()
        prev = None
        for n in map(int, input().split(" ")):
            cur = nodesdict.get(n)
            if cur == None:
                cur = Node(n)
                nodesdict[n] = cur
            if prev != None:
                prev.arc(cur)
            prev = cur

    # init list with roots
    toprocess = []
    for node in nodesdict.values():
        if len(node.prev) == 0:
            bisect.insort(toprocess, node)
        
    # compute result
    R = []
    while len(toprocess) != 0:
        cur = toprocess.pop()
        R.append(str(cur.n))
        for node in cur.next:
            node.nactivation += 1
            if node.nactivation == len(node.prev):
                    bisect.insort(toprocess, node)

    print(" ".join(R))
