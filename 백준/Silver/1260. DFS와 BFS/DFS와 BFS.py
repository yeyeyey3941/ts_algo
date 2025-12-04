from collections import deque
n,m,s = map(int,input().split())
graph = {}
for i in range(m):
    a,b = map(int,input().split())
    if graph.get(a):
        graph[a].append(b)
    else:
        graph[a] = [b]
    if graph.get(b):
        graph[b].append(a)
    else:
        graph[b] = [a]
for i in graph.keys():
    graph[i].sort()
# print(graph)

def DFS(v,sol=[],visit=set()):
    sol.append(v)
    visit.add(v)
    if graph.get(v):
        possible = graph[v]
    else:
        return sol,visit
    for i in possible:
        if i in visit:
            pass
        else:
            sol,visit = DFS(i,sol,visit)
    return sol,visit

def BFS(v):
    queue = deque([v])
    sol = [];visit=set()
    while queue:
        x = queue.popleft()
        if not x in visit:
            sol.append(x);visit.add(x)
            if graph.get(x):
                possible = graph[x]
                for i in possible:
                    queue.append(i)
    return sol
bfs = BFS(s)
# print(graph)
dfs,_ = DFS(s)
print(" ".join(map(str,dfs)))
print(" ".join(map(str,bfs)))
#print(graph)