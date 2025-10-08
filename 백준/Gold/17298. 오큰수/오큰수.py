# 공간 : O(2*n) : answer+stack
# 시간 : O(n) 
# 스택에 들어오게 되는 값이, 비교하는 현재보다 작다면 어차피 답의 목록이 아니기때문에 제거하면됨

n = int(input())
array = list(map(int,input().split()))

answer = [None] * n

stack = []

for i in range(n):
    last = array.pop()
    
    while stack and stack[-1]<=last:
        stack.pop()
    
    answer[n-1-i] = stack[-1] if stack else -1
    stack.append(last)

print(" ".join(map(str,answer)))
    