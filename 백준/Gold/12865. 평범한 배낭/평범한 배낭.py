import sys
input = sys.stdin.readline

n,k = map(int,input().split())

items = [0]*n

dp = [[0]*(k+1) for _ in range(n)]

for i in range(n):
    weight,value = map(int,input().split())
    items[i] = (weight,value)
items.sort(key = lambda x: (-x[0],x[1]/x[0]), reverse=True)

# print(items)

for i in range(items[0][0],k+1):
    dp[0][i] = items[0][1]

for i in range(1,n):
    weight,value = items[i]
    for j in range(weight,k+1):
        dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j] if i>0 else 0)
    for j in range(min(weight,k+1)):
        dp[i][j] = dp[i-1][j] if i>0 and j<=k else 0
print(max(dp[-1]))