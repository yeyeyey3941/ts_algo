n,m,k = map(int,input().split())
b = True
limit = 1;count=n
if n<m+k-1 or n>m*k:
    b = False
    print(-1)
if b:
    while True:
        m = m-1;count = count-k
        if m==0:
            for i in range(n,limit-1,-1):
                print(i,end=" ")
            break
        if count//m==0 or count<=0:
            for i in range(limit+k-1-(m-count),limit-1,-1):
                print(i,end=" ")
            for i in range(limit+k-(m-count),n+1):
                print(i,end=" ")
            break
        else:
            for i in range(limit+k-1,limit-1,-1):
                print(i,end=" ")
            limit = limit+k
    print()