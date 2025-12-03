_ = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print("YES" if (set(a)==set(b) and b[:len(a)]==a ) else "NO")