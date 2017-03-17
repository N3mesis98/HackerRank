#!/usr/bin/python3

#------------------------------
# def
#------------------------------
def compute_shortest(shortcuts):
    pot = [[i, -1, False] for i in range(0,100)]
    pot[0][1] = 0
    
    min_key = lambda i: i[1]
    filter_def = lambda i: (not i[2]) and (i[1]>=0)
    
    cur = min(filter(filter_def, pot), key=min_key, default=None)
    while cur:
        for i in range(1,7):
            new_pos = cur[0]+i
            if new_pos in shortcuts:
                new_pos = shortcuts[new_pos]
            if new_pos<=99:
                if pot[new_pos][1] == -1:
                    pot[new_pos][1] = cur[1]+1
                else:
                    pot[new_pos][1] = min(pot[new_pos][1], cur[1]+1)
            
        cur[2] = True
        cur = min(filter(filter_def, pot), key=min_key, default=None)
    
    return pot[99][1]

#------------------------------
# main
#------------------------------
if __name__ == "__main__":
    ntest = int(input())
    for i in range(0, ntest):
        shortcuts = {}
        
        nladder = int(input())
        for j in range(0, nladder):
            splited = input().split(" ")
            shortcuts[int(splited[0])-1] = int(splited[1])-1
            
        nsnake = int(input())
        for j in range(0, nsnake):
            splited = input().split(" ")
            shortcuts[int(splited[0])-1] = int(splited[1])-1
            
        print(compute_shortest(shortcuts))
