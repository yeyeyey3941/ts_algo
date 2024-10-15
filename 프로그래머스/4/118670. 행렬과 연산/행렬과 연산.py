from collections import deque

def solution(rc: list, operations: list) -> list:
    answer = []
    y = len(rc);x = len(rc[0])
    left = deque([rc[i][0] for i in range(len(rc))])
    right = deque([rc[i][-1] for i in range(len(rc))])
    inner = deque([deque(rc[i][1:-1]) for i in range(len(rc))])
    

    def rotate(left, right, inner):
        top = inner.popleft()
        top.appendleft(left.popleft())
        right.appendleft(top.pop())
        inner.appendleft(top)
        
        bottom = inner.pop()
        bottom.append(right.pop())
        left.append(bottom.popleft())
        inner.append(bottom)
        
                
    def shift(left, right, inner,x,y):
        left.appendleft(left.pop())
        right.appendleft(right.pop())
        if x==2:
            pass
        else:
            inner.rotate(1)

    for i in operations:
        if i[0] == "R":
            rotate(left, right, inner)
        else:
            shift(left, right, inner,x,y)
        
        # for i in range(len(inner)):
        #     print(left[i],end=" ")
        #     print(*inner[i],end=" ")
        #     print(right[i])
        # print(f"letf:{left}, right:{right}, inner:{inner}")

    for i in range(len(left)):
        answer.append([left.popleft()]+list(inner.popleft())+[right.popleft()])

    return answer
