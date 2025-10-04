from sys import stdin
input = stdin.readline

n,m = map(int,input().split())

result = [0]*m
for i in range(m):
    value = input().split()
    
    result[i] = tuple([int(value[0]),int(value[1]),value[2]])

result.sort(key=lambda item:(item[1],item[0]))

print("".join(list(zip(*result))[2]))