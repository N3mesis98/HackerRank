#!/usr/bin/python3

from heapq import *

N = int(input())
# heap containing the first half of the list
# since heapq only allows for min-heap, we must store the opposite to have a max-heap
maxheap = []
# heap containing the last half of the list
minheap = []

for i in range(N):
    # insert the new element
    n = int(input())
    if len(minheap) == 0:
        heappush(minheap, n)
    elif len(maxheap) == len(minheap):
        if minheap[0] >= n:
            heappush(maxheap, -n)
        else:
            heappush(minheap, n)
    elif len(maxheap) < len(minheap):
        if minheap[0] < n:
            n = heapreplace(minheap, n)
        heappush(maxheap, -n)
    else:
        if -maxheap[0] > n:
            n = -heapreplace(maxheap, -n)
        heappush(minheap, n)
        
    # print the result
    r = 0
    if len(maxheap) == len(minheap):
        r = (-maxheap[0]+minheap[0]) / 2
    elif len(maxheap) < len(minheap):
        r = minheap[0]
    else:
        r = -maxheap[0]
    print("{:.1f}".format(r))
