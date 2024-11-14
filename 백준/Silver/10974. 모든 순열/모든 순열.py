import sys
sys.setrecursionlimit(10**6)
print = sys.stdout.write

n = int(input())

def factorial(current=[],remainder=list(range(1,n+1))):
    if remainder == []:
        print(' '.join(map(str,current))+'\n')
        return
    for i in remainder:
        factorial(current+[i], [j for j in remainder if j!=i])

factorial()