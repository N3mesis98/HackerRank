#!/usr/bin/python3

N = int(input())
scores = list(map(int, input().split(" ")))
M = int(input())
alice = list(map(int, input().split(" ")))

compressed_scores = []
for score in scores:
    if (len(compressed_scores) == 0 or compressed_scores[-1] != score):
        compressed_scores.append(score)

i = len(compressed_scores) - 1
for cum_score in alice:
    while i >= 0 and cum_score > compressed_scores[i]:
        i -= 1
    if cum_score == compressed_scores[i]:
        print(i + 1)
    else:
        print(i + 2)
