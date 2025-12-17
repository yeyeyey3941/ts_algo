import sys

input = sys.stdin.readline
n = int(input())

clap = 0
cards = [False]*(n+1)
for _ in range(n):
    now = int(input())
    if not cards[now-1]:
        clap += 1
    cards[now] = True
print(clap-1)
    

