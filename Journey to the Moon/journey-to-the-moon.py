#!/usr/bin/python3

#------------------------------
# def
#------------------------------
def geoSum1(n):
    return (n/2)*(n-1)

#------------------------------
# main
#------------------------------
if __name__ == "__main__":
    tmp = input().split(" ")
    N = int(tmp[0])
    I = int(tmp[1])
    
    groups = []
    for i in range(I):
        tmp = input().split(" ")
        A = int(tmp[0])
        B = int(tmp[1])
        
        a = None
        b = None
        for i in range(len(groups)):
            if (A in groups[i]):
                a = i
            elif (B in groups[i]):
                b = i
        if a!=None and b!=None:
            groups[a] = set.union(groups[a], groups[b])
            del(groups[b])
        elif a==None and b==None:
            groups.append(set([A,B]))
        elif a==None:
            groups[b].add(A)
        else:
            groups[a].add(B)
    
    n = geoSum1(N)
    for group in groups:
        n -= geoSum1(len(group))

    print(int(n))
