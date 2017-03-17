#!/usr/bin/python3

N = int(input().split(" ")[0])

# read row by row
rows = list(input())
for i in range(N-1):
    line = list(input())
    rows = list(map(lambda x,y: x+y, rows, line))
            
text = "".join(rows)
# substitute multiple non-alpha chars between alpha chars by a single space
text = re.sub(r"(?<=\w)\W+(?=\w)", " ", text)

print(text)
