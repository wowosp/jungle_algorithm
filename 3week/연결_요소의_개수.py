import sys
sys.setrecursionlimit(10**6)

N,M=map(int,sys.stdin.readline().split()) 
edge={}
visited = [False] * (N+1)

for i in range(M):
    u, v=map(int,sys.stdin.readline().split())
    if u not in edge:
        edge[u]=[]
    if v not in edge:
        edge[v]=[]
        
    edge[u].append(v)
    edge[v].append(u)
  
def dfs(start):
    visited[start]=True
    
    for i in edge.get(start, []):
        if not visited[i]:
            dfs(i)
            
count = 0            
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1 
    
print(count)