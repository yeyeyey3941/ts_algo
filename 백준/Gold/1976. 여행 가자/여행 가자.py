import sys
input = sys.stdin.readline

city_n = int(input())
m_cycle = int(input())
link = []

class union_find():

    def __init__(self,n):
        self.array = [i for i in range(n)]
    
    def union(self,a,b):
        a_top = self.find(a) # a 의 union 최상단
        b_top = self.find(b) # b 의 union 최상단
        if a_top!=b_top:
            self.array[b_top] = a_top # b의 union 최상단 값을 a의 최상단으로 묶음 -> find(b)를 수행하면 b->b.top ->a.top => b->a.top으로 업데이트
        self.find(b)
            
    def find(self,x):
        if self.array[x] != x:
            self.array[x] = self.find(self.array[x])
        return self.array[x]

union_array = union_find(city_n)
for i in range(city_n):
    link.append(list(map(int,input().split())))
    for j in range(i+1,city_n):
        if link[i][j]==1:
            union_array.union(i,j)
            # print("i,j union : ",union_array.array)

# print(union_array.array)

check = list(map(int,input().split()))
print("YES" if len(set([union_array.find(i-1) for i in check]))==1 else "NO")
