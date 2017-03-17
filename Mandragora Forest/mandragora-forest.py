#!/usr/bin/python3

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        input() # N mandragora, but not needed
        H = sorted(list(map(lambda x:int(x), input().split(" ")))) # retrieve health list and sort ascending
        
        # reverse cumulated sum
        cumsum = [H[-1]]
        for j in range(-2, -(len(H)+1), -1):
            #cumsum.insert(0, cumsum[0]+H[j])
            cumsum.append(cumsum[-1]+H[j])
        cumsum.reverse()
        
        prod = map(lambda x,y: x*y, cumsum, range(1,len(H)+1))
        print(max(prod))
