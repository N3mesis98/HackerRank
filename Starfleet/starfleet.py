#!/usr/bin/python3

from bisect import bisect_left, bisect_right

#------------------------------ /!\ --------------------------------
# V, x and t can be ignored since the disrupt zone is infinite on X
#-------------------------------------------------------------------

SEGMENT=100
N, Q, V = map(int, input().split(" "))

poslist = []
freqlist = []
cumfreq = {}
for i in range(N):
    x, y, f = map(int, input().split(" "))
    poslist.append(y)
    freqlist.append(f)
    cumfreq[f] = 0

# separate into unique and duplicated frequencies
freqcount = {}
for i in range(len(poslist)):
    if freqlist[i] in freqcount:
        freqcount[freqlist[i]].append(poslist[i])
    else:
        freqcount[freqlist[i]] = [poslist[i]]
        
uniqposlist = []
dupfreqlist = []
dupposlist = []
dupaccum = []
for freq, pos in freqcount.items():
    if len(pos) == 1:
        uniqposlist += pos
    else:
        dupposlist += pos
        dupfreqlist += [freq for i in range(len(pos))]
        dupaccum += [None for i in range(len(pos))]
        
# sort
uniqposlist = sorted(uniqposlist)
if len(dupposlist) > 0:
    dupposlist, dupfreqlist = map(list, zip(*sorted(zip(dupposlist, dupfreqlist)))) # sort both by pos

# accumulate at every segment
freqcount = {}
for i in range(len(dupposlist)):
    if i % SEGMENT == 0:
        dupaccum[i] = dict(freqcount)
    if dupfreqlist[i] in freqcount:
        freqcount[dupfreqlist[i]] += 1
    else:
        freqcount[dupfreqlist[i]] = 1
# last accumulation with the total accumulation
dupaccum.append(dict(freqcount))
        
# solve
for q in range(Q):
    yu, yd, t = map(int, input().split(" "))
    
    # retrieve the max duplicated freq
    idxd = bisect_left(dupposlist, yd)
    idxu = bisect_right(dupposlist, yu)
    
    # calculate the accumulation at idxd and idxu from last segments
    dsegment = (idxd // SEGMENT) * SEGMENT
    daccum = dict(dupaccum[dsegment])
    for i in range(dsegment, idxd):
        if dupfreqlist[i] in daccum:
            daccum[dupfreqlist[i]] += 1
        else:
            daccum[dupfreqlist[i]] = 1
    
    usegment = (idxu // SEGMENT) * SEGMENT
    uaccum = dict(dupaccum[usegment])
    for i in range(usegment, idxu):
        if dupfreqlist[i] in uaccum:
            uaccum[dupfreqlist[i]] += 1
        else:
            uaccum[dupfreqlist[i]] = 1

    # compute the maximum freq
    maxi = 0
    for freq, count in uaccum.items():
        if freq in daccum.keys():
            if maxi < count - daccum[freq]:
                maxi = count - daccum[freq]
        else:
            if maxi < count:
                maxi = count
    if maxi > 0:
        print(maxi)
    elif bisect_left(uniqposlist, yd) != bisect_right(uniqposlist, yu):
        print(1)
    else:
        print(0)
