input = __import__('sys').stdin.readline

n,m = map(int,input().split())
p = []
for _ in range(m):
    p.append(int(input()))
p.sort(reverse=True)
maxima = 0 
for i in range(len(p)):
    cost = p[i] 
    if maxima <= p[i]*min(i+1,n):
        maxima = max(maxima,p[i]*min(i+1,n))
        max_cost = p[i]
print(max_cost, maxima)