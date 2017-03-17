#!/usr/bin/python3

def dichotomic_search(a, x, lb=None, ub=None):
    if len(a) == 0:
        return 0
    if lb == None:
        lb = 0
    if ub == None:
        ub = len(a)
    mid = int((lb+ub)/2)
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        if lb == ub-1:
            return ub
        else:
            return dichotomic_search(a, x, mid, ub)
    elif a[mid] > x:
        if lb == ub-1:
            return lb
        else:
            return dichotomic_search(a, x, lb, mid)    

T = int(input())
a = []
for t in range(T):
    c, x = input().split(" ")
    x = int(x)
    if c == "a":
        i = dichotomic_search(a, x)
        a.insert(i, x)
    elif len(a) == 0:
        print("Wrong!")
        continue
    else:
        i = dichotomic_search(a, x)
        if i>=len(a) or a[i]!=x:
            print("Wrong!")
            continue
        else:
            del(a[i])
    if len(a) == 0:
        print("Wrong!")
        continue
    elif len(a)%2 == 0:
        med = (a[int(len(a)/2)-1]+a[int(len(a)/2)])/2
    else:
        med = a[int(len(a)/2)]
    if med%1 == 0:
        print(int(med))
    else:
        print(med)
