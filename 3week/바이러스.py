import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
cumputer={}
visited=[False]*(N+1)
result=[]
for i in range(M):
    u, v=map(int,sys.stdin.readline().split())
    if u not in cumputer:
        cumputer[u]=[]
    if v not in cumputer:
        cumputer[v]=[]
        
    cumputer[u].append(v)
    cumputer[v].append(u)
    
def dfs(start):
    visited[start]=True
    result.append(start)
    
    for i in cumputer.get(start, []):
        if not visited[i]:
            dfs(i)
            
dfs(1)
print(len(result)-1)