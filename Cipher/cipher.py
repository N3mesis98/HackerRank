#!/usr/bin/python3

N, K = map(int, input().split(" "))
cipher = input()

string = cipher[0]
for i in range(1, K):
    if cipher[i] == cipher[i-1]:
        string += "0"
    else:
        string += "1"
        
j = 0
for i in range(i+1, len(cipher)-K+1):
    if string[j] == "1":
        if cipher[i] == cipher[i-1]:
            string += "1"
        else:
            string += "0"
    else:
        if cipher[i] == cipher[i-1]:
            string += "0"
        else:
            string += "1"
    j += 1
        
print(string[0:N])
