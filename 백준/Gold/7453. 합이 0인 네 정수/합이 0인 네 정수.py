import sys
from collections import Counter
n = int(sys.stdin.readline())
a,b,c,d = [],[],[],[]
for _ in range(n):
    a1,b1,c1,d1 = (map(int,sys.stdin.readline().split()))
    a.append(a1); b.append(b1);c.append(c1);d.append(d1)
l2 =[-v1-v2 for v1 in c for v2 in d]
counter = Counter(l2)
#print(counter)
cnt = 0
for i in range(len(l2)):
    k = a[i//n]+b[i%n]
    t = counter[k]
    cnt +=(t)
print(cnt)