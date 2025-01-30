import sys
print = sys.stdout.write

N,K,Q =  map(int,input().split())

A = list(map(int,input().split())) # len(A) == N

X = list(map(int,input().split()))

subseqeuence = [1 if A[i] != K else 0 for i in range(N)]

A[0] = 1 if A[0] != K else 0
conti = 1 if A[0] == 1 else 0

for i in range(1,len(A)):
    if subseqeuence[i] == 0:
        A[i] = A[i-1]
        conti = 0
    else:
        conti += 1
        A[i] = A[i-1] + conti

for x in X:
    print(f"{A[x-1]}\n")
