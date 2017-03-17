#!/usr/bin/python3

class Disjoints:
    """Noeuds numérotés de 0 à N-1"""
    
    def __init__(self, N):
        self.parents = [None for i in range(N)]
        self.ranks = [0 for i in range(N)]
        self.cyclingarcs = 0
    
    def makeset(self, x):
        self.parents[x] = x
        #self.ranks[x] = 0
    
    def find(self, x):
        """None -> pas encore ajouté"""
        if (self.parents[x] != None) and (self.parents[x] != x):
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        if self.parents[x] == None:
            self.makeset(x)
        if self.parents[y] == None:
            self.makeset(y)
        
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.ranks[xroot] <= self.ranks[yroot]:
                self.parents[xroot] = yroot
                newroot = yroot
            else:
                self.parents[yroot] = xroot
                newroot = xroot
            if self.ranks[xroot] == self.ranks[yroot]:
                self.ranks[newroot] += 1
        else:
            self.cyclingarcs += 1
            
def sumn(n):
    """somme des n premiers entiers"""
    return int(n * (n + 1) / 2)

def sumn2(n):
    """somme des n premiers carrés"""
    return int(n * (n + 1) * (2*n + 1) / 6)
    
                
T = int(input())
for t in range(T):
    n, m = map(int, input().split(" "))
    disjoints = Disjoints(n)
    for i in range(m):
        x, y = map(lambda c:int(c)-1, input().split(" "))
        disjoints.union(x, y)
        
    ccs = {}
    for i in range(len(disjoints.parents)):
        root = disjoints.find(i)
        ccs[root] = ccs.setdefault(root, 0) + 1
        
    graphvalue = 0
    total = 0
    for cc in sorted(ccs.items(), key = lambda x:x[1], reverse = True):
        if cc[0] != None:
            # si on ajoute une composante connexe pour la première fois :
            #   on a une valeur du graphe de cc[1] * cc[1]-1    (n personnes ayant n-1 amis car pas ami avec eux même)
            #   le total lié à l'ajout successif des arcs est : 1*0 + 2*1 + 3*2 + 4*3 ...
            #       = (1+1)*1 + (2+1)*2 + (3+1)*3 ...
            #       = (1^2 + 1) + (2^2 + 2) + (3^2 + 3) ...
            #       = (1^2 + 2^2 + 3^2)  +  (1 + 2 + 3)
            #          ^n-1 premiers carrés  ^n-1 premiers entiers
            total += sumn(cc[1]-1) + sumn2(cc[1]-1)
            # mais si il existe déjà d'autres CC avant, on doit ajouter leur valeur à chaque fois
            total += graphvalue * (cc[1]-1)
            # et on met à jour la valeur du graphe
            graphvalue += cc[1] * (cc[1]-1)
    
    # enfin, on ajoute les arcs qui forment des cycles à la fin
    total += disjoints.cyclingarcs * graphvalue
    
    print(total)
