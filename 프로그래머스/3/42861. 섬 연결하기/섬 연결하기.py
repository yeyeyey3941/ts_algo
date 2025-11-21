def solution(n, costs):
    cost_answer = 0
    count = 0 

    uf = union_find(n)

    costs.sort(key=lambda x: x[2])
    
    for v,w,cost in costs:
        if uf.find(v)!=uf.find(w):
            uf.union(v,w)
            cost_answer += cost
            count += 1
        
        if count == n-1:
            return cost_answer


class union_find():
    def __init__(self,n):
        self._parent = [i for i in range(n)]
    
    def find(self,x):
        if self._parent[x] == x:
            return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self,x,y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x<p_y:
            self._parent[y] = p_x
            self._parent[p_y]= p_x
        else:
            self._parent[x] = p_y
            self._parent[p_x]= p_y
        
    @property
    def parent(self):
        return self._parent