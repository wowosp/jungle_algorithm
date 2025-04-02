import sys
from collections import deque

N, M, V=map(int,sys.stdin.readline().split())

edge={}


for i in range(M):
    u, v=map(int,sys.stdin.readline().split())
    if u not in edge:
        edge[u]=[]
    if v not in edge:
        edge[v]=[]
        
    edge[u].append(v)
    edge[v].append(u)
    
for key in edge:
    edge[key].sort()   
     
visited = [False] * (N+1)
   
def dfs(start):  
    visited[start]=True
    print(start, end=' ')
    
    for i in edge.get(start, []):
        if not visited[i]:
            dfs(i)
            
def dfs_stack(start):
    visit=set()
    stack=[start]
    visit.add(start)
    
    
    while stack:
        v=stack.pop()
        print(v, end=' ')
        for i in reversed(edge.get(v,[])):
            if i not in visit:
                visit.add(i)
                stack.append(i)
            
def bfs(start):
    visit= set()
    queue = deque([start])
    visit.add(start)
    
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        
        for i in edge.get(v, []):
            if i not in visit:
                visit.add(i)
                queue.append(i)
    
dfs(V)
print()
dfs_stack(V)
print()
bfs(V)
