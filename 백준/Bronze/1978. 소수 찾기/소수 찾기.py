n = int(input())
l = set([2,3,5,7])
for i in range(11,1000,2):
    for j in l:
        if i%j==0:
            break
    else:
        l.add(i)
check = map(int,input().split())
cnt = 0 
for i in check:
    if i in l:
        cnt+=1
print(cnt)