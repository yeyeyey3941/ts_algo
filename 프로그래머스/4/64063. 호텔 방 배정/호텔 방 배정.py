import sys
sys.setrecursionlimit(4500)
d = dict()
def solution(k, room_number):
    for idx,i in enumerate(room_number):
        # print(i,d,room_number)
        sol = find(i)
        # print(i,d)
        room_number[idx] = sol
        union(sol,sol+1)
    return room_number

def find(x):
    if not x in d:
        d[x] = x
        return x
    elif d[x]==x:
        return x
    p = find(d[x])
    d[x] = p
    return d[x]
def union(a,b):
    a = find(a)
    b = find(b)
    d[a] = b