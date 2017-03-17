#!/usr/bin/python3

class Node:
    def __init__(self, num, data):
        self.num = num
        self.data = data
        self.arcs = set()
        self.parent = None
        self.done = False
        self.treesum = data
        
    def __str__(self):
        return "{ num: "+str(self.num)+", data: "+str(self.data)+", parent: "+str(self.parent)+", arcs: "+str(self.arcs)+" }"
    
    def __repr__(self):
        return str(self.num)
        
N = int(input())
data = list(map(int, input().split(" ")))
total = sum(data)
nodes = [Node(i, data[i]) for i in range(N)]

for i in range(N-1):
    (u, v) = map(int, input().split(" "))
    nodes[u-1].arcs.add(nodes[v-1])
    nodes[v-1].arcs.add(nodes[u-1])
    
mini = total
stack = [nodes[0]]
while len(stack) > 0:
    curnode = stack[-1]
    if curnode.done:
        for child in curnode.arcs:
            curnode.treesum += child.treesum
        mini = min(mini, abs((total - curnode.treesum) - curnode.treesum))
        stack.pop()
    else:
        for child in curnode.arcs:
            child.parent = curnode
            child.arcs.discard(child.parent)
            stack.append(child)
        curnode.done = True
        
print(mini)
