def mergesort(l):
    if len(l)==1:
        return l
    n,m = len(l),len(l)//2
    l1 = l[:m]
    l2 = l[m:]
    l1 = mergesort(l1)+[(0,0)]
    l2 = mergesort(l2)+[(0,0)]
    i1,i2 = 0,0
    for i in range(n):
        if l1[i1][0]>l2[i2][0]:
            l[i] = l1[i1]
            i1 += 1
            continue
        else:
            l[i] = l2[i2]
            CountArray[l2[i2][1]] -= (m-i1)#나보다 앞에있는 잡을수 있는 사람수
            i2 += 1
    return l
import sys
input = sys.stdin.readline
n = int(input())
l = []#기존 숫자 저장배열
CountArray = [0]*n
for i in range(n):
    l.append((int(input()),i))
mergesort(l)
for i in range(len(CountArray)):
    CountArray[i] += i+1
s = "\n".join(map(str,CountArray))
print(s)
