import sys

N= int(sys.stdin.readline())
tree={}
for i in range(N-1):
    u,v=map(int,sys.stdin.readline().split())
    if u not in tree:
        tree[u]=[]
    if v not in tree:
        tree[v]=[]
        
    tree[u].append(v)
    tree[v].append(u)
    
def find_parent(start):
    parent=[i for i in range(N+1)]
    visited=[False]*(N+1)
    stack=[]
    stack.append(start)
    visited[start]=True
    
    while stack:
        v=stack.pop()

        for i in tree.get(v,[]):
            if visited[i] == False:
                visited[i]=True
                stack.append(i)
                parent[i]=v
    return parent

result=find_parent(1)
for i in range(2,N+1):
    print(result[i])
                
    