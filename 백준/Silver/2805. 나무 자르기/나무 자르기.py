n,m = map(int,input().split())
l = list(reversed(sorted(list(map(int,input().split())))))
if n>2:
    ll = [(l[i-1]-l[i]) for i in range(1,n)]+[l[n-1]-0]
    sum = 0
    befsum = 0
    for i in range(n):
        befsum = sum
        sum+=ll[i]*(i+1)
        if sum>=m:
            break
    k = (m-befsum)//(i+1)
    if (m-befsum)%(i+1)==0:
        print(l[i]-k)
    else:
        print(l[i]-k-1)
elif n==2:
    m -=l[1]-l[0]
    k = m//2
    if m%2==0:
        print(l[0]-k)
    else:
        print(l[0]-k-1)
else:
    print(l[0]-m)
