#!/usr/bin/python3

## CLASSES ##
class Node:
    def __init__(self, id):
        self.id = id
        self.inarc = []
        self.outarc = []
        self.reachedfromstart = False
        self.reachedfromend1 = 0
        self.reachedfromend2 = 0
        self.incycle = False
        self.lock = False
        self.possibilities = 0
        
    def To(self, dest):
        for arc in self.outarc:
            if arc.dest == dest:
                return arc
        return None

class Arc:
    def __init__(self, src, dest):
        self.weight = 1
        self.src = src
        self.dest = dest
        src.outarc.append(self)
        dest.inarc.append(self)

## FUNCTIONS ##
def Wave(node):
    """depth-first search starting from the first node to detect cycles and reached nodes"""
    if node.lock:
        node.incycle = True
    if not node.reachedfromstart:
        node.reachedfromstart = True
        node.lock = True
        for outarc in node.outarc:
            Wave(outarc.dest)
        node.lock = False

def RWave1(node):
    """depth-first search starting from the end and counting the number of ancestor from the end
    return True if reached a cycle, False else"""
    if node.reachedfromstart:
        node.reachedfromend1 += 1
        if node.reachedfromend1 == 1:
            if node.incycle:
                return True
            else:
                for inarc in node.inarc:
                    if RWave1(inarc.src):
                        return True
    return False
        
def RWave2(node, curposs = 1):
    if node.reachedfromstart:
        node.possibilities = (node.possibilities + curposs) % (10**9)
        node.reachedfromend2 += 1
        if node.reachedfromend2 == node.reachedfromend1:
            for inarc in node.inarc:
                RWave2(inarc.src, (node.possibilities * inarc.weight) % (10**9))
    
## INPUT ##
N, M = map(int, input().split(" "))
nodes = []
for i in range(N):
    nodes.append(Node(i+1))
    
for i in range(M):
    srcid, destid = map(int, input().split(" "))
    src = nodes[srcid-1]
    dest = nodes[destid-1]
    existingarc = src.To(dest)
    if existingarc != None:
        existingarc.weight += 1
    else:
        Arc(src, dest)
        
## ALGORITHM ##            
Wave(nodes[0])
if (RWave1(nodes[-1])):
    print("INFINITE PATHS")
else:
    RWave2(nodes[-1])
    print(nodes[0].possibilities)
