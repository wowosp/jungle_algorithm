import sys

V, E=map(int,sys.stdin.readline().split())
edge=[]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edge.append((u-1, v-1, w))
    
    
parent = [i for i in range(V)] 


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))         

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y): 
        root_x = self.find(x)
        root_y = self.find(y)
        
        self.parent[root_x] = root_y

def kruskal(vertices, edges):
    uf = UnionFind(vertices)
    mst = [] 
    edges.sort(key=lambda x: x[2])  

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v): 
            uf.union(u, v)
            mst.append((u, v, weight))
            if len(mst) == vertices - 1: 
                break

    return mst


mst = kruskal(V, edge)
total_weight = sum(weight for _, _, weight in mst)
print(total_weight)

       