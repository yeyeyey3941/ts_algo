import sys
input = sys.stdin.readline

cost = 105.6
Q = int(input())
answer = [0]*Q
for i in range(Q):
    a,min = map(int,input().split())
    answer[i] = int((a*min*cost)//60000)
print("\n".join(map(str,answer[:Q])))