from collections import deque
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    count = [0]*10
    n_th = 0
    queue = deque([(importance,index) for index,importance in enumerate(list(map(int,input().split())))])
    for i in queue:
        count[i[0]] += 1
    while True:
        if sum(count[queue[0][0]+1:])==0:
            curr = queue.popleft()
            count[curr[0]] -= 1
            if curr[1]==m:
                print(n_th+1)
                break
            n_th += 1
        else:
            queue.rotate(-1)