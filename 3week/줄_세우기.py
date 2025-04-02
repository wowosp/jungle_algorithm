import sys
from collections import deque

tree={}
N,M=map(int,sys.stdin.readline().split())
indegree=[0]*(N+1)


for i in range(M):
    u,v=map(int,sys.stdin.readline().split())
    if u not in tree:
        tree[u]=[]
    tree[u].append(v)
    indegree[v]+=1

def kahn(graph):
    global indegree
    
    result=[]
    queue = deque([i for i in range(1, N+1) if indegree[i] == 0])
    
    while queue:
        v = queue.popleft()
        result.append(v)
        
        for i in graph.get(v, []):
            indegree[i] -= 1
            if indegree[i]==0:
                queue.append(i)
    
    return result
    
print(*kahn(tree))

