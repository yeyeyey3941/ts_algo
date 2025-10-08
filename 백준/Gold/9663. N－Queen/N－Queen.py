# 시간 최적화를 위해 visit 을 y값만두고 x는 배열의 인덱스 로 가져와서
n = int(input())

def check(visit_list,y)->bool:
    if y in visit_list:
        return False
    x = len(visit_list)
    for v in enumerate(visit_list):
        if abs(v[0]-x)==abs(v[1]-y):
            return False
    return True

def dfs(visit=[],x=0)->int:
    if len(visit)==n:
        return 1
    cnt = 0
    for i in range(n):
        if check(visit,i):
            visit.append(i)
            cnt += dfs(visit,x+1)
            visit.pop()
    return cnt

print(dfs())