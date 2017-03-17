#!/usr/bin/python3

def rotate(m, n, mmin, mmax, nmin, nmax):
    if (m == mmin) and (n != nmin):
        return (m, n-1)
    elif (n == nmin) and (m != mmax):
        return (m+1, n)
    elif (m == mmax) and (n != nmax):
        return (m, n+1)
    else: #(n == nmax) and (m != mmin)
        return (m-1, n)

M, N, R = map(int, input().split(" "))

imat = []
for m in range(M):
    imat.append(list(map(int, input().split(" "))))
                
rmat = [[0 for i in range(N)] for i in range(M)]
for i in range(int(min(M, N) / 2)):
    curM = M - i*2
    curN = N - i*2
    borderSize = 2*curM + 2*curN - 4  # -4 à cause des coins
    curR = R % borderSize
    
    m = n = i
    for j in range(curR):
        m, n = rotate(m, n, i, M-i-1, i, N-i-1)
    
    mi = ni = i
    for j in range(borderSize):
        rmat[m][n] = imat[mi][ni]
        m, n = rotate(m, n, i, M-i-1, i, N-i-1)
        mi, ni = rotate(mi, ni, i, M-i-1, i, N-i-1)
    
for line in rmat:
    print(" ".join(map(str, line)))
